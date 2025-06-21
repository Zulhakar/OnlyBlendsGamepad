import bpy
from bpy.types import Panel

class OnlyBlendsPanel():
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "OnlyBlends.Gamepad"


class GAMEPAD_PT_main_panel(OnlyBlendsPanel, Panel):
    """Main panel for gamepad loop controls"""
    bl_label = "Gamepad Loop Controller"
    bl_idname = "GAMEPAD_PT_main_panel"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        gamepad_props = scene.gamepad_loop_props

        # Checkboxes
        layout.prop(gamepad_props, "enable_gamepad_loop", toggle=True)

        layout.prop(gamepad_props, "enable_debug_popup", toggle=False)

        layout.prop(gamepad_props, "enable_debug_console", toggle=False)

        layout.prop(gamepad_props, "loop_interval")


class GAMEPAD_PT_sub(OnlyBlendsPanel, Panel):
    """Main panel for gamepad loop controls"""
    bl_label = "Gamepads"
    bl_idname = "GAMEPAD_PT_sub"
    bl_parent_id = "GAMEPAD_PT_main_panel"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        gamepad_props = scene.gamepad_loop_props
        layout.label(text="Status:")
        if gamepad_props.enable_gamepad_loop:
            layout.label(text="Gamepad Listener is RUNNING", icon='PLAY')
            layout.label(text=f"Iterations: {gamepad_props.iteration_count}")
        else:
            layout.label(text="Gamepad Listener is STOPPED", icon='PAUSE')
        layout.label(text=f"Number of Gamepads: {str(gamepad_props.gamepad_count)}")

def create_dynamic_controller_panel(c_name, label_name, gamepad_obj_name):

    def draw(self, context):
        layout = self.layout
        gamepad_reader_empty = bpy.data.objects.get(gamepad_obj_name)
        if gamepad_reader_empty is not None:
            controller_inputs = gamepad_reader_empty.items()
            box = layout.box()
            row = box.row()
            for key, value in controller_inputs:
                row = box.row()
                #row.prop(gamepad_reader_empty, f'["{key}"]',)
                row.label(text=f"{key}: {value}")
    DynamicPanelClass = type(c_name, (OnlyBlendsPanel, Panel, ), {
        "bl_label": label_name,
        "bl_idname": c_name,
        "bl_parent_id" : "GAMEPAD_PT_sub",
        "bl_options" : {'DEFAULT_CLOSED'},
        "draw": draw,
    })
    return DynamicPanelClass
