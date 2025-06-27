import bpy
from .nodegroup import create_nodegroup
from .gamepad_model import create_gamepad_geometrynode
class OnlyBlendsPanel():
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "OnlyBlends.Gamepad"



class GAMEPAD_PT_main_panel(OnlyBlendsPanel,  bpy.types.Panel):
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


class GAMEPAD_PT_sub(OnlyBlendsPanel,  bpy.types.Panel):
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

class CREATE_OT_model(bpy.types.Operator):
    bl_idname = "ob.create_gamepad_model_op"
    bl_label = "Create Gamepad Model"

    gamepad_name : bpy.props.StringProperty(name="Unknown")
    def execute(self, context):
        create_gamepad_geometrynode(self.gamepad_name)
        return {"FINISHED"}

class CREATE_OT_nodegroup(bpy.types.Operator):
    bl_idname = "ob.create_gamepad_nodegroup_op"
    bl_label = "Create Gamepad Nodegroup"

    gamepad_name : bpy.props.StringProperty(name="Unknown")
    def execute(self, context):
        create_nodegroup(self.gamepad_name)
        return {"FINISHED"}


def create_dynamic_controller_panel(c_name, name):

    def draw(self, context):
        layout = self.layout

        #scene = context.scene
        #gamepad_props = scene.gamepad_loop_props
        #layout.prop(gamepad_props, "create_gamepad_model", toggle=True)
        op_model = layout.operator("ob.create_gamepad_model_op", text="Create Gamepad Model")
        op_model.gamepad_name = name
        op = layout.operator( "ob.create_gamepad_nodegroup_op", text="Create Gamepad Nodegroups")
        op.gamepad_name = name
        gamepad_reader_empty = bpy.data.objects.get(name)
        if gamepad_reader_empty is not None:
            controller_inputs = gamepad_reader_empty.items()
            box = layout.box()
            row = box.row()
            for key, value in controller_inputs:
                row = box.row()
                #row.prop(gamepad_reader_empty, f'["{key}"]',)
                row.label(text=f"{key}: {value}")


    DynamicPanelClass = type(c_name, (OnlyBlendsPanel,  bpy.types.Panel, ), {
        "bl_label": name,
        "bl_idname": c_name,
        "bl_parent_id" : "GAMEPAD_PT_sub",
        "bl_options" : {'DEFAULT_CLOSED'},
        "draw": draw,
    })
    return DynamicPanelClass
