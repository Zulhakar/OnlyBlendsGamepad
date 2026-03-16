import bpy

STATE_KEY = "_ui_fullscreen_active"


def find_3d_view():
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            return area
    return None


def set_ui_visibility(override, visible):
    screen = bpy.context.screen
    if hasattr(screen, "show_statusbar"):
        screen.show_statusbar = visible
    if hasattr(screen, "show_topbar"):
        screen.show_topbar = visible
    bpy.context.space_data.region_3d.view_perspective = 'CAMERA'
    #bpy.ops.view3d.zoom_camera_1_to_1(override)


class VIEW3D_OT_toggle_ui_fullscreen(bpy.types.Operator):
    bl_idname = "view3d.toggle_ui_fullscreen"
    bl_label = "Toggle 3D View Fullscreen (UI-less)"

    def execute(self, context):
        wm = context.window_manager

        if wm.get(STATE_KEY):
            bpy.ops.view3d.exit_ui_fullscreen()
            return {'FINISHED'}

        area = find_3d_view()
        if not area:
            self.report({'ERROR'}, "No 3D Viewport found")
            return {'CANCELLED'}

        # Switch context to 3D view
        override = context.copy()
        override["area"] = area
        override["region"] = area.regions[-1]
        with context.temp_override(**override):
            bpy.ops.screen.screen_full_area(use_hide_panels=True)
            set_ui_visibility(override, False)

        wm[STATE_KEY] = True

        return {'FINISHED'}


class VIEW3D_OT_hide_cursor(bpy.types.Operator):
    bl_idname = "view3d.hide_cursor"
    bl_label = "Hide Cursor"

    def modal(self, context, event):
        if event.type == 'ESC':
            bpy.ops.wm.quit_blender()
            # context.window.cursor_modal_restore()
            #
            # if context.window_manager.get(STATE_KEY):
            #     #bpy.ops.screen.screen_full_area(use_hide_panels=False)
            #     bpy.ops.screen.back_to_previous()
            #     area = find_3d_view()
            #     if area:
            #         set_ui_visibility(area, True)
            #     context.window_manager[STATE_KEY] = False
            #
            # return {'CANCELLED'}
        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        context.window.cursor_modal_set('NONE')
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}


def set_scene_settings():
    bpy.context.preferences.view.show_splash = False
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            space = area.spaces.active
            space.overlay.show_overlays = False
            space.show_gizmo = False
            area.spaces.active.shading.type = 'RENDERED'
    bpy.context.scene.frame_set(0)
    bpy.ops.screen.animation_play()
    bpy.ops.view3d.hide_cursor('INVOKE_DEFAULT')
    bpy.ops.view3d.toggle_ui_fullscreen('INVOKE_DEFAULT')


def register():
    bpy.utils.register_class(VIEW3D_OT_toggle_ui_fullscreen)
    bpy.utils.register_class(VIEW3D_OT_hide_cursor)


def unregister():
    bpy.utils.unregister_class(VIEW3D_OT_toggle_ui_fullscreen)
    bpy.utils.unregister_class(VIEW3D_OT_hide_cursor)


if __name__ == "__main__":
    register()
    set_scene_settings()
