from bpy.utils import register_class
from bpy.utils import unregister_class
from .gamepad_node import GamepadStateNode
from .transform_object_node import TransformObjectNodeCnt

def register():
    register_class(GamepadStateNode)
    register_class(TransformObjectNodeCnt)


def unregister():
    unregister_class(GamepadStateNode)
    unregister_class(TransformObjectNodeCnt)