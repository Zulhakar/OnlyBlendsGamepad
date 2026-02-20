import bpy
from bpy.app.handlers import persistent
from bl_ui import node_add_menu

from .cnt.node_editor import register as register_node_editor
from .cnt.node_editor import unregister as unregister_node_editor
from .cnt.sockets.basic_sockets import register as register_basic_sockets
from .cnt.sockets.basic_sockets import unregister as unregister_basic_sockets
from .cnt.nodes import register as register_nodes
from .cnt.nodes import unregister as unregister_nodes
from .cnt.node_editor.menus import InputMenu, GroupMenu
from .nodes import register as register_obg_nodes
from .nodes import unregister as unregister_obg_nodes
from .config import OB_TREE_TYPE
from .nodes.gamepad_node import plug_and_play_poll

@persistent
def load_blend_file_job(file_name):
    for group in bpy.data.node_groups:
        for node in group.nodes:
            if hasattr(node, "refresh"):
                node.refresh()

class RealtimeMenu(bpy.types.Menu):
    bl_label = 'Realtime'
    bl_idname = 'RealtimeMenu'

    def draw(self, context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "RealtimeValueNode")
        node_add_menu.add_node_type(layout, "SceneInfoNodeCnt")
        node_add_menu.add_node_type(layout, "GamepadStateNode")
        node_add_menu.add_node_type(layout, "TransformObjectNodeCnt")
        node_add_menu.add_node_type(layout, "DuplicateObjectNode")


class UtilMenu(bpy.types.Menu):
    bl_label = 'Util'
    bl_idname = 'UtilMenu'

    def draw(self, context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "MathNodeCnt")
        node_add_menu.add_node_type(layout, "SwitchNodeCnt")
        node_add_menu.add_node_type(layout, "CompareAndBoolNodeCnt")


def draw_add_menu(self, context):
    layout = self.layout
    if context.space_data.tree_type != OB_TREE_TYPE:
        return
    layout.menu(InputMenu.bl_idname)
    layout.menu(GroupMenu.bl_idname)
    layout.menu(RealtimeMenu.bl_idname)
    layout.menu(UtilMenu.bl_idname)
    node_add_menu.add_node_type(layout, "ModifierNode")


def register():
    register_basic_sockets()
    register_nodes()
    register_obg_nodes()
    register_node_editor()
    bpy.utils.register_class(RealtimeMenu)
    bpy.utils.register_class(UtilMenu)
    bpy.types.NODE_MT_add.append(draw_add_menu)
    bpy.app.handlers.load_post.append(load_blend_file_job)


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
    bpy.utils.unregister_class(RealtimeMenu)
    bpy.utils.unregister_class(UtilMenu)
    bpy.app.handlers.load_post.remove(load_blend_file_job)
    unregister_util()
    if bpy.app.timers.is_registered(plug_and_play_poll):
        bpy.app.timers.unregister(plug_and_play_poll)
if __name__ == "__main__":
    register()
