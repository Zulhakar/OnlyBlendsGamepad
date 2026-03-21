import bpy
from bl_ui import node_add_menu

from .cnt.node_editor import register as register_node_editor
from .cnt.node_editor import unregister as unregister_node_editor
from .cnt.sockets import register as register_basic_sockets
from .cnt.sockets import unregister as unregister_basic_sockets
from .cnt.nodes import register as register_nodes
from .cnt.nodes import unregister as unregister_nodes
from .cnt.node_editor.menus import InputMenu, GroupMenu, RealtimeMenu, UtilMenu
from .nodes import register as register_obg_nodes
from .nodes import unregister as unregister_obg_nodes
from .config import OB_TREE_TYPE, APP_NAME_SHORT
from .nodes.gamepad_node import plug_and_play_poll
from .util.fullscreen_instance import BlenderSubprocessOperator, RenderSubprocessPanel


class GamepadMenu(bpy.types.Menu):
    bl_label = 'OB Gamepad'
    bl_idname = f'NODE_MT_{APP_NAME_SHORT}_ObGamepadMenu'

    def draw(self, context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GamepadStateNode")
        node_add_menu.add_node_type(layout, "TransformObjectNodeCnt")



def draw_add_menu(self, context):
    layout = self.layout
    if context.space_data.tree_type != OB_TREE_TYPE:
        return
    layout.menu(InputMenu.bl_idname)
    layout.menu(GroupMenu.bl_idname)
    layout.menu(RealtimeMenu.bl_idname)
    layout.menu(UtilMenu.bl_idname)
    node_add_menu.add_node_type(layout, "ModifierNode")
    layout.menu(GamepadMenu.bl_idname)

def register():
    bpy.utils.register_class(BlenderSubprocessOperator)
    bpy.utils.register_class(RenderSubprocessPanel)
    register_basic_sockets()
    register_nodes()
    register_obg_nodes()
    register_node_editor()
    bpy.utils.register_class(GamepadMenu)


    bpy.types.NODE_MT_add.append(draw_add_menu)


def unregister_util():
    from .globals import gamepad_thread_dict, gamepad_event_queue_dict, register_functions_dict
    import copy
    keys = list(register_functions_dict.keys())
    for key in keys:
        if bpy.app.timers.is_registered(register_functions_dict[key]):
            bpy.app.timers.unregister(register_functions_dict[key])
        del register_functions_dict[key]
    keys = list(gamepad_event_queue_dict.keys())
    for key in keys:
        del gamepad_event_queue_dict[key]
    keys = list(gamepad_thread_dict.keys())
    for key in keys:
        gamepad_thread_dict[key].let_it_run = False
        del gamepad_thread_dict[key]


def unregister():
    bpy.types.NODE_MT_add.remove(draw_add_menu)
    unregister_basic_sockets()
    unregister_obg_nodes()
    unregister_nodes()
    unregister_node_editor()
    bpy.utils.unregister_class(GamepadMenu)

    bpy.utils.unregister_class(BlenderSubprocessOperator)
    bpy.utils.unregister_class(RenderSubprocessPanel)

    unregister_util()
    if bpy.app.timers.is_registered(plug_and_play_poll):
        bpy.app.timers.unregister(plug_and_play_poll)
if __name__ == "__main__":
    register()
