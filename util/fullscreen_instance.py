import bpy
import subprocess
import os, platform
import tempfile
from pathlib import Path


def handle_userpref():
    config_dir = bpy.utils.user_resource('CONFIG')
    userpref_path = os.path.join(config_dir, "userpref.blend")

    # Ensure directory exists
    os.makedirs(config_dir, exist_ok=True)

    # Save preferences if file doesn't exist
    if not os.path.exists(userpref_path):
        print("userpref.blend not found. Creating default...")
        bpy.ops.wm.save_userpref()
    else:
        print("userpref.blend already exists.")


class BlenderSubprocessOperator(bpy.types.Operator):
    bl_idname = "obg.blender_subprocess"
    bl_label = "OnlyBlends"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        handle_userpref()

        script_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(script_dir, "full_screen.py")
        cmd = []
        cmd.append(bpy.app.binary_path)

        tmp_dir = tempfile.gettempdir()
        temp_file = os.path.join(tmp_dir, "obs_temp_file.blend")
        bpy.ops.wm.save_as_mainfile(filepath=str(temp_file), copy=True)

        cmd.append(temp_file)
        cmd.append("--window-fullscreen")
        cmd.append("-P")
        cmd.append(file_path)

        # cmd_line = subprocess.list2cmdline(cmd)
        result = subprocess.run(cmd, shell=False, text=True, capture_output=True)

        # result = subprocess.run(cmd_line, shell=True, text=True)
        try:
            self.report({'INFO'}, f"Success: {result.stdout}")
        except Exception as e:
            self.report({'ERROR'}, f"Exception: {str(e)}")
        return {'FINISHED'}


class RenderSubprocessPanel(bpy.types.Panel):
    bl_label = "OnlyBlends"
    bl_idname = "RENDER_PT_subprocess"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"
    bl_order = 0

    def draw(self, context):
        layout = self.layout
        layout.operator(BlenderSubprocessOperator.bl_idname, text="Start Game", icon="PLAY")


