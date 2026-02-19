import bpy
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


def unregister():
    bpy.types.NODE_MT_add.remove(draw_add_menu)
    unregister_basic_sockets()
    unregister_obg_nodes()
    unregister_nodes()
    unregister_node_editor()
    bpy.utils.unregister_class(RealtimeMenu)
    bpy.utils.unregister_class(UtilMenu)


if __name__ == "__main__":
    register()
