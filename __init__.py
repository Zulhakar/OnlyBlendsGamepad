import bpy
from bpy.props import BoolProperty, FloatProperty, IntProperty

from .pygame_helper import gamepad_listen_function
from .ui import GAMEPAD_PT_main_panel, GAMEPAD_PT_sub, CREATE_OT_model, CREATE_OT_nodegroup
from .gamepad_model import create_gamepad_geometrynode
from .nodegroup import create_nodegroup

class GamepadLoopProperties(bpy.types.PropertyGroup):
    """Property group for gamepad loop settings"""

    enable_debug_popup: BoolProperty(
        name="Enable Debug Popup Infos",
        description="Toggle to show Popup which displays Button Inputs",
        default=False
    )  # type: ignore

    enable_debug_console: BoolProperty(
        name="Enable Debug Console Infos",
        description="Toggle to output terminal infos",
        default=True
    )  # type: ignore


    enable_gamepad_loop: BoolProperty(
        name="Enable Gamepad Loop",
        description="Toggle gamepad loop functionality on/off",
        default=True,
        update=lambda self, context: update_gamepad_loop(self, context)
    )  # type: ignore



    loop_interval: FloatProperty(
        name="Interval (seconds)",
        description="Time interval between loop iterations",
        default=0.1,
        min=0.01,
        max=10.0,
        step=0.01
    )  # type: ignore

    gamepad_count: IntProperty(
        name="Gamepad Count",
        description=" Number of detected Gamepads",
        default=0
    )  # type: ignore
    iteration_count: IntProperty(
        name="Iterations",
        description="Number of iterations completed",
        default=0
    )  # type: ignore

class DetectedGamepadsProp(bpy.types.PropertyGroup):
    id: bpy.props.IntProperty(name="Id Property", default=0)
    pygame_id: bpy.props.IntProperty(name="Pygame Id Property", default=0)
    name: bpy.props.StringProperty(name="Gamepad Name", default="Unknown")
    type_name: bpy.props.StringProperty(name="Type Name", default="Unknown")
    panel_class_name: bpy.props.StringProperty(name="Panel Name", default="Unknown")

def update_gamepad_loop(self, context):
    """Called when the checkbox value changes"""
    if self.enable_gamepad_loop:
        if not bpy.app.timers.is_registered(gamepad_loop_iteration):
            self.iteration_count = 0  # Reset counter
            bpy.app.timers.register(gamepad_loop_iteration, first_interval=self.loop_interval)
    else:
        if bpy.app.timers.is_registered(gamepad_loop_iteration):
            bpy.app.timers.unregister(gamepad_loop_iteration)


def gamepad_loop_iteration():
    """
    The main loop function that gets called repeatedly
    Returns the interval for next call, or None to stop
    """
    scene = bpy.context.scene
    gamepad_loop_props = scene.gamepad_loop_props

    # Check if loop should continue
    if not gamepad_loop_props.enable_gamepad_loop:
        return None  # Stop

    gamepad_loop_props.iteration_count += 1

    # this runs on the main thread !!!
    gamepad_listen_function()

    # Force UI update
    for area in bpy.context.screen.areas:
        if area.type in ['VIEW_3D', 'PROPERTIES']:
            area.tag_redraw()


    return gamepad_loop_props.loop_interval


classes = [
    GamepadLoopProperties,
    DetectedGamepadsProp,
    GAMEPAD_PT_main_panel,
    GAMEPAD_PT_sub, CREATE_OT_model, CREATE_OT_nodegroup
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.gamepad_loop_props = bpy.props.PointerProperty(type=GamepadLoopProperties)
    bpy.types.Scene.detected_gamepads = bpy.props.CollectionProperty(type=DetectedGamepadsProp)

    bpy.app.timers.register(gamepad_loop_iteration, first_interval=0.1)


def unregister():
    if bpy.app.timers.is_registered(gamepad_loop_iteration):
        bpy.app.timers.unregister(gamepad_loop_iteration)
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    if hasattr(bpy.types.Scene, 'gamepad_loop_props'):
        del bpy.types.Scene.gamepad_loop_props


if __name__ == "__main__":
    register()
