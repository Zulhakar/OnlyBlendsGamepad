import bpy
from .constants import GAMEPAD_LABEL


def create_gamepad_nodegroup(input_type, obj_name):
    gamepad_reader_empty = bpy.data.objects.get(obj_name)
    node_group_name = obj_name + "_" + input_type
    controller_inputs = gamepad_reader_empty.items()

    gamepad_nodegroup_name = node_group_name
    gamepad_nodegroup = bpy.data.node_groups.get(gamepad_nodegroup_name)

    if gamepad_nodegroup is None:
        gamepad_nodegroup = bpy.data.node_groups.new(gamepad_nodegroup_name, 'GeometryNodeTree')

    output_node = None
    for node in gamepad_nodegroup.nodes:
        if node.type == 'GROUP_OUTPUT':
            output_node = node
            break

    if output_node is None:
        output_node = gamepad_nodegroup.nodes.new('NodeGroupOutput')
        output_node.location = (0, 0)

    for inputs in controller_inputs:
        if type(gamepad_reader_empty[inputs[0]]) == float or int or bool:
            if inputs[0].startswith(input_type):
                if bpy.app.version[0] == 3:
                    if inputs[0] not in gamepad_nodegroup.outputs:
                        gamepad_nodegroup.outputs.new("NodeSocketFloat", inputs[0])
                if bpy.app.version[0] == 4:
                    if inputs[0] not in gamepad_nodegroup.interface.items_tree:
                        gamepad_nodegroup.interface.new_socket(inputs[0], in_out="OUTPUT",
                                                               socket_type='NodeSocketFloat')

                output_socket = output_node.inputs[inputs[0]]
                fcurve = output_socket.driver_add('default_value')
                driver = fcurve.driver
                driver.type = 'AVERAGE'
                if len(driver.variables) == 0:
                    variable = driver.variables.new()
                else:
                    variable = driver.variables[0]
                variable.name = inputs[0]
                variable.type = 'SINGLE_PROP'
                targets = variable.targets[0]
                targets.id_type = 'OBJECT'
                targets.id = gamepad_reader_empty
                targets.data_path = f'["{inputs[0]}"]'
                driver.expression = 'var'


def create_nodegroup(obj_name):
    input_types = ("button", "dpad", "axis")
    for input_type in input_types:
        create_gamepad_nodegroup(input_type, obj_name)

