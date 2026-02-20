import bpy
import queue
import functools
import inputs

from ..cnt.nodes.basic_nodes import ConstantNodeCnt
from ..config import IS_DEBUG
from ..util.gamepad_state import GamepadState
from ..globals import gamepad_thread_dict, gamepad_event_queue_dict, register_functions_dict

UPDATE_INTERVAL = 0.001

def get_gamepad_device_path_enum_items(scene, context):
    import importlib
    importlib.reload(inputs)
    from inputs import devices
    items = [(None)]
    for i, device in enumerate(devices.gamepads):
        items.append((device._device_path, device.name, device.name))
    return items


def get_gamepad_from_device_path(device_path):
    import importlib
    importlib.reload(inputs)
    from inputs import devices
    for i, device in enumerate(devices.all_devices):
        if device._device_path == device_path:
            return device
    return None


def gamepad_event_loop(interval, gamepad_state_obj, gamepad_event_queue, node):
    events_dict = {}
    while not gamepad_event_queue.empty():
        event = gamepad_event_queue.get()
        if isinstance(event, str):
            node.clean_up_on_gamepad_disconnect(event)
            return None
        # performance boost
        if event.ev_type != "Sync" or event.ev_type != "Misc":
            events_dict[event.ev_type + "-" + event.code] = event
    #performance boost, only process last state
    for event in events_dict.values():
        gamepad_state_obj.process_event(event)
    return interval

def get_all_gamepad_nodes(except_node=None):
    all_gamepad_nodes = []
    for key, value in bpy.data.node_groups.items():
        for node in value.nodes:
            if node.bl_idname == "GamepadStateNode":
                if node != except_node:
                    all_gamepad_nodes.append(node)
    return all_gamepad_nodes

class GamepadStateNode(ConstantNodeCnt):
    '''Gamepad Node updates on change'''
    bl_label = "Gamepad"
    gamepad_device_path: bpy.props.EnumProperty(  # type: ignore
        name="Operation"
        , items=get_gamepad_device_path_enum_items
        , update=lambda self, context: self.gamepads_update()
    )
    previous_gamepad: bpy.props.StringProperty()
    # gamepad_node_id: bpy.props.StringProperty(name="Node ID")
    def clean_up_on_gamepad_disconnect(self, device_path):
        if IS_DEBUG:
            print("clean_up_on_gamepad_disconnect")
        if device_path in register_functions_dict:
            if bpy.app.timers.is_registered(register_functions_dict[device_path]):
                bpy.app.timers.unregister(register_functions_dict[device_path])
            del register_functions_dict[device_path]
        if device_path in gamepad_thread_dict:
            gamepad_thread_dict[device_path].let_it_run = False
            gamepad_thread_dict[device_path].nodes.remove(self)
            del gamepad_thread_dict[device_path]
        if device_path in gamepad_event_queue_dict:
            del gamepad_event_queue_dict[device_path]

    def clean_up(self, device_path):
        #alternative use GamepadState singleton to check if thread have to delete
        all_other_nodes = get_all_gamepad_nodes(self)
        is_last_node = True
        for node in all_other_nodes:
            if node.gamepad_device_path == device_path:
                is_last_node = False
        if device_path:
            if is_last_node:
                if device_path in register_functions_dict:
                    if bpy.app.timers.is_registered(register_functions_dict[device_path]):
                        bpy.app.timers.unregister(register_functions_dict[device_path])
                    del register_functions_dict[device_path]
                if device_path in gamepad_thread_dict:
                    gamepad_thread_dict[device_path].let_it_run = False
                    gamepad_thread_dict[device_path].nodes.remove(self)
                    del gamepad_thread_dict[device_path]
                if device_path in gamepad_event_queue_dict:
                    del gamepad_event_queue_dict[device_path]
            else:
                gamepad_thread_dict[device_path].nodes.remove(self)
        if IS_DEBUG:
            print("current globals:")
            for key in register_functions_dict.keys():
                print("register_functions_dict:")
                print(key)
            for key in gamepad_thread_dict.keys():
                print("gamepad_thread_dict:")
                print(key)
            for key in gamepad_event_queue_dict.keys():
                print("gamepad_event_queue_dict:")
                print(key)

    def gamepads_update(self):
        if IS_DEBUG:
            print("gamepad_device_path_update")
        if self.previous_gamepad:
            if self.previous_gamepad != self.gamepad_device_path:
                self.clean_up(self.previous_gamepad)
        self.previous_gamepad = self.gamepad_device_path
        if self.gamepad_device_path not in gamepad_event_queue_dict:
            gamepad_event_queue_dict[self.gamepad_device_path] = queue.Queue()
        if self.gamepad_device_path not in gamepad_thread_dict:
            gamepad_thread_dict[self.gamepad_device_path] = GamepadState(self,
                                                                 gamepad_event_queue_dict[self.gamepad_device_path],
                                                                 get_gamepad_from_device_path(self.gamepad_device_path))
            gamepad_thread_dict[self.gamepad_device_path].daemon = True
            gamepad_thread_dict[self.gamepad_device_path].start()
        else:
            gamepad_state = gamepad_thread_dict[self.gamepad_device_path]
            if self not in gamepad_state.nodes:
                gamepad_state.nodes.append(self)
        if self.gamepad_device_path not in register_functions_dict:
            register_functions_dict[self.gamepad_device_path] = functools.partial(gamepad_event_loop,
                                                                          UPDATE_INTERVAL,
                                                                          gamepad_thread_dict[self.gamepad_device_path],
                                                                          gamepad_event_queue_dict[
                                                                              self.gamepad_device_path], self)
            bpy.app.timers.register(register_functions_dict[self.gamepad_device_path], first_interval=UPDATE_INTERVAL)


    def draw_buttons(self, context, layout):
        layout.prop(self, "gamepad_device_path", text="")

    def init(self, context):
        self.outputs.new('NodeSocketStringCnt', "Button Key")
        self.outputs.new('NodeSocketFloatCnt', "Button Value")
        self.outputs.new('NodeSocketStringCnt', "D-Pad Key")
        self.outputs.new('NodeSocketFloatCnt', "D-Pad Value")
        self.outputs.new('NodeSocketStringCnt', "Axis Key")
        self.outputs.new('NodeSocketFloatCnt', "Axis Value")
        super().init(context)


    def socket_update(self, socket):
        if socket.is_output:
            for link in socket.links:
                link.to_socket.input_value = socket.input_value

    def free(self):
        super().free()
        self.clean_up(self.gamepad_device_path)

    def refresh(self):
        print(self.gamepad_device_path)
        if self.gamepad_device_path:
            self.gamepads_update()