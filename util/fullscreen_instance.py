import bpy
import subprocess
import os, platform
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
        os_type = platform.system()
        if os_type == 'Linux':
            cmd = f'chmod +x {file_path} | '
        else:
            cmd = ''
        cmd += f'{bpy.app.binary_path} '

        temp_dir = Path(bpy.app.tempdir)
        temp_file =  os.path.join(temp_dir, "obs_temp_blend_file.blend")
        bpy.ops.wm.save_as_mainfile(filepath=str(temp_file), copy=True)

        cmd += f'{temp_file} '

        cmd += f'--window-fullscreen -P {file_path}'

        print(cmd)
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
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


