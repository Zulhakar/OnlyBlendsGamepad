import bpy
import functools
import inputs
import os
import sys
import subprocess
import select
import json

from ..obc_custom_nodes.nodes.basic_nodes import ConstantNodeCnt
from ..config import IS_DEBUG
from ..globals import gamepad_process_dict, gamepad_state_dict, register_functions_dict, all_gamepads
from ..util.gamepad_state import init_state, process_event

UPDATE_INTERVAL = 0.001


def get_gamepad_device_path_enum_items(scene, context):
    import importlib
    try:
        importlib.reload(inputs)
    except Exception:
        pass
    from inputs import devices
    items = [(None)]
    for device in devices.gamepads:
        items.append((device._device_path, device.name, device.name))
    return items


def get_all_gamepad_nodes(except_node=None):
    nodes = []
    for ng in bpy.data.node_groups.values():
        for n in ng.nodes:
            if n.bl_idname == "GamepadStateNode" and n != except_node:
                nodes.append(n)
    return nodes


def plug_and_play_poll():
    import importlib
    try:
        importlib.reload(inputs)
    except Exception:
        pass
    from inputs import devices
    current = {g._device_path for g in devices.gamepads}
    diff = current - all_gamepads
    for dev in diff:
        for node in get_all_gamepad_nodes():
            if node.gamepad_device_path == dev:
                node.gamepads_update()
    all_gamepads.clear()
    all_gamepads.update(current)
    return 1.0


def register_plug_and_play_poll():
    if not bpy.app.timers.is_registered(plug_and_play_poll):
        bpy.app.timers.register(plug_and_play_poll, first_interval=1.0)


def _start_subprocess(device_path):
    script = os.path.join(os.path.dirname(__file__), "..", "util", "gamepad_reader.py")
    env = os.environ.copy()
    env["PYTHONUNBUFFERED"] = "1"
    proc = subprocess.Popen(
        [sys.executable, script, device_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True,
        bufsize=1,
        env=env,
    )
    os.set_blocking(proc.stdout.fileno(), False)   # non-blocking pipe
    return proc


def _poll_gamepad_process(device_path, node, interval=UPDATE_INTERVAL):
    proc = gamepad_process_dict.get(device_path)
    if proc is None:
        return None
    if proc.poll() is not None:
        node.clean_up_on_gamepad_disconnect(device_path)
        return None

    state = gamepad_state_dict.get(device_path)
    if not state:
        return interval

    # keep a small buffer per device
    buf = state.get("_buf", "")
    try:
        chunk = proc.stdout.read(4096)   # non-blocking because fd is set non-blocking
        if chunk:
            buf += chunk
    except BlockingIOError:
        pass
    except Exception:
        node.clean_up_on_gamepad_disconnect(device_path)
        return None

    # process complete lines only
    while "\n" in buf:
        line, buf = buf.split("\n", 1)
        if not line.strip():
            continue
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            # incomplete JSON, keep in buffer
            buf = line + "\n" + buf
            break
        process_event(state, ev, state.get("nodes", []))

    state["_buf"] = buf
    return interval


class GamepadStateNode(ConstantNodeCnt):
    bl_label = "Gamepad"
    bl_icon = "PLUGIN"
    gamepad_device_path: bpy.props.EnumProperty(
        name="Operation",
        items=get_gamepad_device_path_enum_items,
        update=lambda self, context: self.gamepads_update(),
    )
    previous_gamepad: bpy.props.StringProperty()

    def clean_up_on_gamepad_disconnect(self, device_path):
        if IS_DEBUG:
            print("clean_up_on_gamepad_disconnect")
        if device_path in register_functions_dict:
            if bpy.app.timers.is_registered(register_functions_dict[device_path]):
                bpy.app.timers.unregister(register_functions_dict[device_path])
            del register_functions_dict[device_path]
        proc = gamepad_process_dict.pop(device_path, None)
        if proc:
            try:
                proc.terminate()
                proc.wait(timeout=1)
            except Exception:
                proc.kill()
        gamepad_state_dict.pop(device_path, None)

    def clean_up(self, device_path):
        all_other = get_all_gamepad_nodes(self)
        is_last = True
        for n in all_other:
            if n.gamepad_device_path == device_path:
                is_last = False
                break
        if device_path:
            if is_last:
                if device_path in register_functions_dict:
                    if bpy.app.timers.is_registered(register_functions_dict[device_path]):
                        bpy.app.timers.unregister(register_functions_dict[device_path])
                    del register_functions_dict[device_path]
                proc = gamepad_process_dict.pop(device_path, None)
                if proc:
                    try:
                        proc.terminate()
                        proc.wait(timeout=1)
                    except Exception:
                        proc.kill()
                gamepad_state_dict.pop(device_path, None)
            else:
                state = gamepad_state_dict.get(device_path)
                if state and self in state.get("nodes", []):
                    state["nodes"].remove(self)
        if IS_DEBUG:
            print("current globals:")
            print(register_functions_dict.keys())
            print(gamepad_process_dict.keys())
            print(gamepad_state_dict.keys())

    def gamepads_update(self):
        if IS_DEBUG:
            print("gamepad_device_path_update")
        if self.previous_gamepad and self.previous_gamepad != self.gamepad_device_path:
            self.clean_up(self.previous_gamepad)
        self.previous_gamepad = self.gamepad_device_path

        if not self.gamepad_device_path:
            return

        if self.gamepad_device_path not in gamepad_process_dict:
            proc = _start_subprocess(self.gamepad_device_path)
            gamepad_process_dict[self.gamepad_device_path] = proc
            state = init_state()
            state["nodes"] = [self]
            gamepad_state_dict[self.gamepad_device_path] = state
            cb = functools.partial(_poll_gamepad_process, self.gamepad_device_path, self)
            register_functions_dict[self.gamepad_device_path] = cb
            bpy.app.timers.register(cb, first_interval=UPDATE_INTERVAL)
        else:
            state = gamepad_state_dict[self.gamepad_device_path]
            if self not in state.get("nodes", []):
                state.setdefault("nodes", []).append(self)

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
        register_plug_and_play_poll()

    def socket_update(self, socket):
        if socket.is_output:
            for link in socket.links:
                link.to_socket.input_value = socket.input_value

    def free(self):
        super().free()
        self.clean_up(self.gamepad_device_path)

    def refresh(self):
        if self.gamepad_device_path:
            self.gamepads_update()
        register_plug_and_play_poll()