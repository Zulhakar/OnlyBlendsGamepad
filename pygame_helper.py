import bpy
import pygame

pygame.init()
from .constants import *
from .main import create_gamepad_empty
from .ui import create_dynamic_controller_panel
from .nodegroup import create_nodegroup

register_classes_dyn = {}


def console_log(text):
    if bpy.context.scene.gamepad_loop_props.enable_debug_console:
        print(text)


def popup_info_log(text, joy_name):
    if bpy.context.scene.gamepad_loop_props.enable_debug_popup:
        def oops(self, context):
            self.layout.label(text=text)

        bpy.context.window_manager.popup_menu(oops, title=joy_name, icon='EVENT_MEDIASTOP')


def gamepad_listen_function():
    for event in pygame.event.get():
        if event.type == pygame.JOYDEVICEADDED:
            joy = pygame.joystick.Joystick(event.device_index)
            joy_id = joy.get_instance_id()

            message = f"Joystick {joy_id} connected"
            message2 = f"Name: {joy.get_name()}"

            console_log(message)
            console_log(message2)

            popup_info_log(message, message2)

            joy.init()
            #gamepad_count = bpy.context.scene.gamepad_loop_props.gamepad_count
            #create_nodegroup(gamepad_count)
            name = GAMEPAD_LABEL + str(joy_id)
            class_name =  PANEL_CLASS + str(joy_id)
            empty = create_gamepad_empty(name)
            get_joystick_state(joy, empty, joy_id)
            dynamic_panel_class = create_dynamic_controller_panel(class_name, name)
            bpy.utils.register_class(dynamic_panel_class)
            new_gamepad_prop = bpy.context.scene.detected_gamepads.add()
            new_gamepad_prop.name = name
            new_gamepad_prop.id = bpy.context.scene.gamepad_loop_props.gamepad_count
            new_gamepad_prop.pygame_id = joy_id
            new_gamepad_prop.panel_class_name = class_name
            new_gamepad_prop.type_name = joy.get_name()
            bpy.context.scene.gamepad_loop_props.gamepad_count = pygame.joystick.get_count()

            register_classes_dyn[class_name] = dynamic_panel_class

        if event.type == pygame.JOYDEVICEREMOVED:
            # del joysticks[event.instance_id]

            message = f"Joystick {event.instance_id} disconnected"

            console_log(f"Joystick {event.instance_id} disconnected")

            popup_info_log(message, "")


            gamepad_to_delete = None
            gamepad_to_delete_id = None
            i = 0
            for item in bpy.context.scene.detected_gamepads:
                if item.pygame_id == event.instance_id:
                    gamepad_to_delete = item
                    gamepad_to_delete_id = i
                    break
                i += 1

            class_name = gamepad_to_delete.panel_class_name
            bpy.utils.unregister_class(register_classes_dyn[class_name])
            del register_classes_dyn[class_name]
            bpy.data.objects.remove(bpy.data.objects.get(gamepad_to_delete.name))
            bpy.context.scene.detected_gamepads.remove(gamepad_to_delete_id)
            bpy.context.scene.gamepad_loop_props.gamepad_count = pygame.joystick.get_count()

        if event.type == pygame.JOYBUTTONDOWN:
            id = event.instance_id
            name = GAMEPAD_LABEL + str(id)
            empty = bpy.data.objects.get(name)
            empty["button_" + str(event.button)] = 1
            try:
                joy = pygame.joystick.Joystick(event.__dict__["joy"])
                joy_name = joy.get_name()

                message = f"Joystick {str(joy.get_instance_id())}: Button {str(event.button)} pressed"

                console_log(joy_name)
                console_log(message)

                popup_info_log(message, joy_name)
            except Exception as e:
                print(e)
                print("")

            if bpy.context.scene.gamepad_loop_props.enable_debug_popup:
                def oops(self, context):
                    self.layout.label(text="Joystick button pressed. " + str(event.button))

                bpy.context.window_manager.popup_menu(oops, title=joy_name + " Button Pressed", icon='EVENT_MEDIASTOP')

        if event.type == pygame.JOYBUTTONUP:
            id = event.instance_id
            name = GAMEPAD_LABEL + str(id)
            empty = bpy.data.objects.get(name)
            empty["button_" + str(event.button)] = 0
            try:
                joy = pygame.joystick.Joystick(event.__dict__["joy"])
                joy_name = joy.get_name()

                message = f"Joystick {str(joy.get_instance_id())}: Button {str(event.button)} released"

                console_log(joy_name)
                console_log(message)

                popup_info_log(message, joy_name)
            except Exception as e:
                print(e)
                print("")

        if event.type == pygame.JOYHATMOTION:
            id = event.instance_id
            hat_value = event.__dict__["value"]
            hat = event.__dict__["hat"]
            name = GAMEPAD_LABEL + str(id)
            try:
                joy = pygame.joystick.Joystick(event.__dict__["joy"])
                joy_name = joy.get_name()
                message = f"D_Pad_: {str(hat)} value: {str(hat_value)}"
                console_log(message)
                popup_info_log(message, joy_name)
                empty = bpy.data.objects.get(name)
                empty["dpad_x_" + str(hat)] = hat_value[0]
                empty["dpad_y_" + str(hat)] = hat_value[1]
            except Exception as e:
                print(e)
                print("")

        if event.type == pygame.JOYAXISMOTION:
            id = event.instance_id
            axis_value = event.__dict__["value"]
            axis = event.__dict__["axis"]
            name = GAMEPAD_LABEL + str(id)

            message = f"Axis {str(axis)}: {str(axis_value)}"
            console_log(name)
            console_log(message)
            popup_info_log(message, name)

            empty = bpy.data.objects.get(name)
            empty["axis_" + str(axis)] = axis_value

    for i in range(pygame.joystick.get_count()):
        joystick = pygame.joystick.Joystick(i)
        if not hasattr(joystick, "initialized"):
            joystick.init()
        name = GAMEPAD_LABEL + str(i)
        empty = bpy.data.objects.get(name)
        if empty is not None:
            empty.location = empty.location


def get_joystick_state(joystick, gamepad_reader_empty, id):
    name = joystick.get_name()
    gamepad_reader_empty["id"] = id
    gamepad_reader_empty["name"] = name

    power_level = joystick.get_power_level()
    gamepad_reader_empty["powerlevel"] = power_level

    axes = joystick.get_numaxes()
    for i in range(axes):
        axis = joystick.get_axis(i)
        gamepad_reader_empty["axis_" + str(i)] = axis

    buttons = joystick.get_numbuttons()
    for i in range(buttons):
        button = joystick.get_button(i)
        gamepad_reader_empty["button_" + str(i)] = True if button == 1 else 0

    hats = joystick.get_numhats()
    for i in range(hats):
        hat = joystick.get_hat(i)
        gamepad_reader_empty["dpad_x_" + str(i)] = hat[0]
        gamepad_reader_empty["dpad_y_" + str(i)] = hat[1]
