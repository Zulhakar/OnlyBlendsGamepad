import bpy


def create_gamepad_geometrynode(obj_name):

        mat = bpy.data.materials.new(name="Gamepad_Button_Material")
        mat.use_nodes = True

        # initialize Material node group
        def material_node_group():

                material = mat.node_tree
                # start with a clean node tree
                for node in material.nodes:
                        material.nodes.remove(node)
                material.color_tag = 'NONE'
                material.description = ""
                material.default_group_node_width = 140

                # material interface

                # initialize material nodes
                # node Material Output
                material_output = material.nodes.new("ShaderNodeOutputMaterial")
                material_output.name = "Material Output"
                material_output.is_active_output = True
                material_output.target = 'ALL'
                # Displacement
                material_output.inputs[2].default_value = (0.0, 0.0, 0.0)
                # Thickness
                material_output.inputs[3].default_value = 0.0

                # node Principled BSDF
                principled_bsdf = material.nodes.new("ShaderNodeBsdfPrincipled")
                principled_bsdf.name = "Principled BSDF"
                principled_bsdf.distribution = 'MULTI_GGX'
                principled_bsdf.subsurface_method = 'RANDOM_WALK'
                # Base Color
                principled_bsdf.inputs[0].default_value = (1.0, 0.18547192215919495, 0.015802454203367233, 1.0)
                # Metallic
                principled_bsdf.inputs[1].default_value = 0.2560606002807617
                # Roughness
                principled_bsdf.inputs[2].default_value = 0.4749999940395355
                # IOR
                principled_bsdf.inputs[3].default_value = 1.0
                # Alpha
                principled_bsdf.inputs[4].default_value = 1.0
                # Normal
                principled_bsdf.inputs[5].default_value = (0.0, 0.0, 0.0)
                # Diffuse Roughness
                principled_bsdf.inputs[7].default_value = 0.0
                # Subsurface Weight
                principled_bsdf.inputs[8].default_value = 0.0
                # Subsurface Radius
                principled_bsdf.inputs[9].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
                # Subsurface Scale
                principled_bsdf.inputs[10].default_value = 0.05000000074505806
                # Subsurface Anisotropy
                principled_bsdf.inputs[12].default_value = 0.0
                # Specular IOR Level
                principled_bsdf.inputs[13].default_value = 0.5
                # Specular Tint
                principled_bsdf.inputs[14].default_value = (1.0, 1.0, 1.0, 1.0)
                # Anisotropic
                principled_bsdf.inputs[15].default_value = 0.0
                # Anisotropic Rotation
                principled_bsdf.inputs[16].default_value = 0.0
                # Tangent
                principled_bsdf.inputs[17].default_value = (0.0, 0.0, 0.0)
                # Transmission Weight
                principled_bsdf.inputs[18].default_value = 0.0
                # Coat Weight
                principled_bsdf.inputs[19].default_value = 0.0
                # Coat Roughness
                principled_bsdf.inputs[20].default_value = 0.029999999329447746
                # Coat IOR
                principled_bsdf.inputs[21].default_value = 1.5
                # Coat Tint
                principled_bsdf.inputs[22].default_value = (1.0, 1.0, 1.0, 1.0)
                # Coat Normal
                principled_bsdf.inputs[23].default_value = (0.0, 0.0, 0.0)
                # Sheen Weight
                principled_bsdf.inputs[24].default_value = 0.0
                # Sheen Roughness
                principled_bsdf.inputs[25].default_value = 0.5
                # Sheen Tint
                principled_bsdf.inputs[26].default_value = (1.0, 1.0, 1.0, 1.0)
                # Emission Color
                principled_bsdf.inputs[27].default_value = (1.0, 1.0, 1.0, 1.0)
                # Emission Strength
                principled_bsdf.inputs[28].default_value = 0.0
                # Thin Film Thickness
                principled_bsdf.inputs[29].default_value = 0.0
                # Thin Film IOR
                principled_bsdf.inputs[30].default_value = 1.3300000429153442

                # Set locations
                material_output.location = (300.0, 300.0)
                principled_bsdf.location = (10.0, 300.0)

                # Set dimensions
                material_output.width, material_output.height = 140.0, 100.0
                principled_bsdf.width, principled_bsdf.height = 240.0, 100.0

                # initialize material links
                # principled_bsdf.BSDF -> material_output.Surface
                material.links.new(principled_bsdf.outputs[0], material_output.inputs[0])
                return material

        material = material_node_group()

        mat = bpy.data.materials.new(name="Gamepad_Case_Material")
        mat.use_nodes = True

        # initialize Case_Material node group
        def case_material_node_group():

                case_material = mat.node_tree
                # start with a clean node tree
                for node in case_material.nodes:
                        case_material.nodes.remove(node)
                case_material.color_tag = 'NONE'
                case_material.description = ""
                case_material.default_group_node_width = 140

                # case_material interface

                # initialize case_material nodes
                # node Material Output
                material_output = case_material.nodes.new("ShaderNodeOutputMaterial")
                material_output.name = "Material Output"
                material_output.is_active_output = True
                material_output.target = 'ALL'
                # Displacement
                material_output.inputs[2].default_value = (0.0, 0.0, 0.0)
                # Thickness
                material_output.inputs[3].default_value = 0.0

                # node Principled BSDF
                principled_bsdf = case_material.nodes.new("ShaderNodeBsdfPrincipled")
                principled_bsdf.name = "Principled BSDF"
                principled_bsdf.distribution = 'MULTI_GGX'
                principled_bsdf.subsurface_method = 'RANDOM_WALK'
                # Base Color
                principled_bsdf.inputs[0].default_value = (0.17287549376487732, 0.9196861982345581, 1.0, 1.0)
                # Metallic
                principled_bsdf.inputs[1].default_value = 0.2560606002807617
                # Roughness
                principled_bsdf.inputs[2].default_value = 0.4749999940395355
                # IOR
                principled_bsdf.inputs[3].default_value = 1.0
                # Alpha
                principled_bsdf.inputs[4].default_value = 1.0
                # Normal
                principled_bsdf.inputs[5].default_value = (0.0, 0.0, 0.0)
                # Diffuse Roughness
                principled_bsdf.inputs[7].default_value = 0.0
                # Subsurface Weight
                principled_bsdf.inputs[8].default_value = 0.0
                # Subsurface Radius
                principled_bsdf.inputs[9].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
                # Subsurface Scale
                principled_bsdf.inputs[10].default_value = 0.05000000074505806
                # Subsurface Anisotropy
                principled_bsdf.inputs[12].default_value = 0.0
                # Specular IOR Level
                principled_bsdf.inputs[13].default_value = 0.5
                # Specular Tint
                principled_bsdf.inputs[14].default_value = (1.0, 1.0, 1.0, 1.0)
                # Anisotropic
                principled_bsdf.inputs[15].default_value = 0.0
                # Anisotropic Rotation
                principled_bsdf.inputs[16].default_value = 0.0
                # Tangent
                principled_bsdf.inputs[17].default_value = (0.0, 0.0, 0.0)
                # Transmission Weight
                principled_bsdf.inputs[18].default_value = 0.0
                # Coat Weight
                principled_bsdf.inputs[19].default_value = 0.0
                # Coat Roughness
                principled_bsdf.inputs[20].default_value = 0.029999999329447746
                # Coat IOR
                principled_bsdf.inputs[21].default_value = 1.5
                # Coat Tint
                principled_bsdf.inputs[22].default_value = (1.0, 1.0, 1.0, 1.0)
                # Coat Normal
                principled_bsdf.inputs[23].default_value = (0.0, 0.0, 0.0)
                # Sheen Weight
                principled_bsdf.inputs[24].default_value = 0.0
                # Sheen Roughness
                principled_bsdf.inputs[25].default_value = 0.5
                # Sheen Tint
                principled_bsdf.inputs[26].default_value = (1.0, 1.0, 1.0, 1.0)
                # Emission Color
                principled_bsdf.inputs[27].default_value = (1.0, 1.0, 1.0, 1.0)
                # Emission Strength
                principled_bsdf.inputs[28].default_value = 0.0
                # Thin Film Thickness
                principled_bsdf.inputs[29].default_value = 0.0
                # Thin Film IOR
                principled_bsdf.inputs[30].default_value = 1.3300000429153442

                # Set locations
                material_output.location = (300.0, 300.0)
                principled_bsdf.location = (10.0, 300.0)

                # Set dimensions
                material_output.width, material_output.height = 140.0, 100.0
                principled_bsdf.width, principled_bsdf.height = 240.0, 100.0

                # initialize case_material links
                # principled_bsdf.BSDF -> material_output.Surface
                case_material.links.new(principled_bsdf.outputs[0], material_output.inputs[0])
                return case_material

        case_material = case_material_node_group()

        # initialize donut_gn node group
        def donut_gn_node_group():
                donut_gn = bpy.data.node_groups.new(type='GeometryNodeTree', name="Donut_GN")

                donut_gn.color_tag = 'NONE'
                donut_gn.description = ""
                donut_gn.default_group_node_width = 140

                donut_gn.is_modifier = True

                # donut_gn interface
                # Socket Geometry
                geometry_socket = donut_gn.interface.new_socket(name="Geometry", in_out='OUTPUT',
                                                                socket_type='NodeSocketGeometry')
                geometry_socket.attribute_domain = 'POINT'

                # Socket Geometry
                geometry_socket_1 = donut_gn.interface.new_socket(name="Geometry", in_out='INPUT',
                                                                  socket_type='NodeSocketGeometry')
                geometry_socket_1.attribute_domain = 'POINT'

                # Socket Radius
                radius_socket = donut_gn.interface.new_socket(name="Radius", in_out='INPUT',
                                                              socket_type='NodeSocketFloat')
                radius_socket.default_value = 0.08000005036592484
                radius_socket.min_value = 0.0
                radius_socket.max_value = 3.4028234663852886e+38
                radius_socket.subtype = 'DISTANCE'
                radius_socket.attribute_domain = 'POINT'

                # Socket Resolution
                resolution_socket = donut_gn.interface.new_socket(name="Resolution", in_out='INPUT',
                                                                  socket_type='NodeSocketInt')
                resolution_socket.default_value = 7
                resolution_socket.min_value = 3
                resolution_socket.max_value = 512
                resolution_socket.subtype = 'NONE'
                resolution_socket.attribute_domain = 'POINT'

                # Socket Radius2
                radius2_socket = donut_gn.interface.new_socket(name="Radius2", in_out='INPUT',
                                                               socket_type='NodeSocketFloat')
                radius2_socket.default_value = 0.7000000476837158
                radius2_socket.min_value = 0.0
                radius2_socket.max_value = 3.4028234663852886e+38
                radius2_socket.subtype = 'DISTANCE'
                radius2_socket.attribute_domain = 'POINT'

                # Socket Radius2 Resolution
                radius2_resolution_socket = donut_gn.interface.new_socket(name="Radius2 Resolution", in_out='INPUT',
                                                                          socket_type='NodeSocketInt')
                radius2_resolution_socket.default_value = 12
                radius2_resolution_socket.min_value = 3
                radius2_resolution_socket.max_value = 512
                radius2_resolution_socket.subtype = 'NONE'
                radius2_resolution_socket.attribute_domain = 'POINT'

                # initialize donut_gn nodes
                # node Group Input
                group_input = donut_gn.nodes.new("NodeGroupInput")
                group_input.name = "Group Input"

                # node Group Output
                group_output = donut_gn.nodes.new("NodeGroupOutput")
                group_output.name = "Group Output"
                group_output.is_active_output = True

                # node Curve Circle
                curve_circle = donut_gn.nodes.new("GeometryNodeCurvePrimitiveCircle")
                curve_circle.name = "Curve Circle"
                curve_circle.mode = 'RADIUS'

                # node Curve Circle.001
                curve_circle_001 = donut_gn.nodes.new("GeometryNodeCurvePrimitiveCircle")
                curve_circle_001.name = "Curve Circle.001"
                curve_circle_001.mode = 'RADIUS'

                # node Curve to Mesh
                curve_to_mesh = donut_gn.nodes.new("GeometryNodeCurveToMesh")
                curve_to_mesh.name = "Curve to Mesh"
                # Fill Caps
                curve_to_mesh.inputs[2].default_value = False

                # node Transform Geometry
                transform_geometry = donut_gn.nodes.new("GeometryNodeTransform")
                transform_geometry.name = "Transform Geometry"
                transform_geometry.mode = 'COMPONENTS'
                # Translation
                transform_geometry.inputs[1].default_value = (0.0, 0.0, 0.0)
                # Rotation
                transform_geometry.inputs[2].default_value = (0.0, 0.0, 0.0)
                # Scale
                transform_geometry.inputs[3].default_value = (2.0, 1.0, 1.0)

                # Set locations
                group_input.location = (-620.4600830078125, 218.19009399414062)
                group_output.location = (414.8641357421875, -5.447118759155273)
                curve_circle.location = (-274.27606201171875, 185.2822723388672)
                curve_circle_001.location = (-141.55148315429688, 338.8909912109375)
                curve_to_mesh.location = (158.71060180664062, 224.5258026123047)
                transform_geometry.location = (-68.90657043457031, 182.44686889648438)

                # Set dimensions
                group_input.width, group_input.height = 140.0, 100.0
                group_output.width, group_output.height = 140.0, 100.0
                curve_circle.width, curve_circle.height = 140.0, 100.0
                curve_circle_001.width, curve_circle_001.height = 140.0, 100.0
                curve_to_mesh.width, curve_to_mesh.height = 140.0, 100.0
                transform_geometry.width, transform_geometry.height = 140.0, 100.0

                # initialize donut_gn links
                # curve_circle.Curve -> transform_geometry.Geometry
                donut_gn.links.new(curve_circle.outputs[0], transform_geometry.inputs[0])
                # transform_geometry.Geometry -> curve_to_mesh.Profile Curve
                donut_gn.links.new(transform_geometry.outputs[0], curve_to_mesh.inputs[1])
                # curve_to_mesh.Mesh -> group_output.Geometry
                donut_gn.links.new(curve_to_mesh.outputs[0], group_output.inputs[0])
                # curve_circle_001.Curve -> curve_to_mesh.Curve
                donut_gn.links.new(curve_circle_001.outputs[0], curve_to_mesh.inputs[0])
                # group_input.Radius -> curve_circle.Radius
                donut_gn.links.new(group_input.outputs[1], curve_circle.inputs[4])
                # group_input.Resolution -> curve_circle.Resolution
                donut_gn.links.new(group_input.outputs[2], curve_circle.inputs[0])
                # group_input.Radius2 -> curve_circle_001.Radius
                donut_gn.links.new(group_input.outputs[3], curve_circle_001.inputs[4])
                # group_input.Radius2 Resolution -> curve_circle_001.Resolution
                donut_gn.links.new(group_input.outputs[4], curve_circle_001.inputs[0])
                return donut_gn

        donut_gn = donut_gn_node_group()

        # initialize joystick_gn node group
        def joystick_gn_node_group():
                joystick_gn = bpy.data.node_groups.new(type='GeometryNodeTree', name="Joystick_GN")

                joystick_gn.color_tag = 'NONE'
                joystick_gn.description = ""
                joystick_gn.default_group_node_width = 140

                joystick_gn.is_modifier = True

                # joystick_gn interface
                # Socket Geometry
                geometry_socket_2 = joystick_gn.interface.new_socket(name="Geometry", in_out='OUTPUT',
                                                                     socket_type='NodeSocketGeometry')
                geometry_socket_2.attribute_domain = 'POINT'

                # Socket Geometry
                geometry_socket_3 = joystick_gn.interface.new_socket(name="Geometry", in_out='INPUT',
                                                                     socket_type='NodeSocketGeometry')
                geometry_socket_3.attribute_domain = 'POINT'

                # Socket Segments
                segments_socket = joystick_gn.interface.new_socket(name="Segments", in_out='INPUT',
                                                                   socket_type='NodeSocketInt')
                segments_socket.default_value = 7
                segments_socket.min_value = 3
                segments_socket.max_value = 1024
                segments_socket.subtype = 'NONE'
                segments_socket.attribute_domain = 'POINT'

                # Socket Depth
                depth_socket = joystick_gn.interface.new_socket(name="Depth", in_out='INPUT',
                                                                socket_type='NodeSocketFloat')
                depth_socket.default_value = 1.7000000476837158
                depth_socket.min_value = 0.0
                depth_socket.max_value = 3.4028234663852886e+38
                depth_socket.subtype = 'DISTANCE'
                depth_socket.attribute_domain = 'POINT'

                # initialize joystick_gn nodes
                # node Group Input
                group_input_1 = joystick_gn.nodes.new("NodeGroupInput")
                group_input_1.name = "Group Input"

                # node Group Output
                group_output_1 = joystick_gn.nodes.new("NodeGroupOutput")
                group_output_1.name = "Group Output"
                group_output_1.is_active_output = True

                # node UV Sphere.001
                uv_sphere_001 = joystick_gn.nodes.new("GeometryNodeMeshUVSphere")
                uv_sphere_001.name = "UV Sphere.001"
                uv_sphere_001.hide = True
                # Rings
                uv_sphere_001.inputs[1].default_value = 16
                # Radius
                uv_sphere_001.inputs[2].default_value = 1.0

                # node Transform Geometry.001
                transform_geometry_001 = joystick_gn.nodes.new("GeometryNodeTransform")
                transform_geometry_001.name = "Transform Geometry.001"
                transform_geometry_001.hide = True
                transform_geometry_001.mode = 'COMPONENTS'
                # Translation
                transform_geometry_001.inputs[1].default_value = (0.0, 0.0, 0.0)
                # Rotation
                transform_geometry_001.inputs[2].default_value = (0.0, 0.0, 0.0)
                # Scale
                transform_geometry_001.inputs[3].default_value = (1.0, 1.0, 1.0)

                # node Cone
                cone = joystick_gn.nodes.new("GeometryNodeMeshCone")
                cone.name = "Cone"
                cone.hide = True
                cone.fill_type = 'NGON'
                # Side Segments
                cone.inputs[1].default_value = 1
                # Fill Segments
                cone.inputs[2].default_value = 1
                # Radius Top
                cone.inputs[3].default_value = 0.4099999964237213
                # Radius Bottom
                cone.inputs[4].default_value = 0.4000000059604645

                # node Join Geometry.001
                join_geometry_001 = joystick_gn.nodes.new("GeometryNodeJoinGeometry")
                join_geometry_001.name = "Join Geometry.001"
                join_geometry_001.hide = True

                # node Transform Geometry.002
                transform_geometry_002 = joystick_gn.nodes.new("GeometryNodeTransform")
                transform_geometry_002.name = "Transform Geometry.002"
                transform_geometry_002.hide = True
                transform_geometry_002.mode = 'COMPONENTS'
                # Translation
                transform_geometry_002.inputs[1].default_value = (0.0, 0.0, 0.5999999642372131)
                # Rotation
                transform_geometry_002.inputs[2].default_value = (0.0, 0.0, 0.0)
                # Scale
                transform_geometry_002.inputs[3].default_value = (1.0, 1.0, 1.0)

                # node Group.001
                group_001 = joystick_gn.nodes.new("GeometryNodeGroup")
                group_001.name = "Group.001"
                group_001.hide = True
                group_001.node_tree = donut_gn
                # Socket_2
                group_001.inputs[1].default_value = 0.08000005036592484
                # Socket_4
                group_001.inputs[3].default_value = 0.5700000524520874

                # node Join Geometry
                join_geometry = joystick_gn.nodes.new("GeometryNodeJoinGeometry")
                join_geometry.name = "Join Geometry"

                # node Transform Geometry.003
                transform_geometry_003 = joystick_gn.nodes.new("GeometryNodeTransform")
                transform_geometry_003.name = "Transform Geometry.003"
                transform_geometry_003.hide = True
                transform_geometry_003.mode = 'COMPONENTS'
                # Rotation
                transform_geometry_003.inputs[2].default_value = (0.0, 0.0, 0.0)
                # Scale
                transform_geometry_003.inputs[3].default_value = (1.0, 1.0, 1.0)

                # node Math.002
                math_002 = joystick_gn.nodes.new("ShaderNodeMath")
                math_002.name = "Math.002"
                math_002.hide = True
                math_002.operation = 'ADD'
                math_002.use_clamp = False
                # Value_001
                math_002.inputs[1].default_value = 0.5899999737739563

                # node Combine XYZ.001
                combine_xyz_001 = joystick_gn.nodes.new("ShaderNodeCombineXYZ")
                combine_xyz_001.name = "Combine XYZ.001"
                combine_xyz_001.hide = True
                # X
                combine_xyz_001.inputs[0].default_value = 0.0
                # Y
                combine_xyz_001.inputs[1].default_value = 0.0

                # Set locations
                group_input_1.location = (-889.3460693359375, 72.61325073242188)
                group_output_1.location = (557.906982421875, 222.90155029296875)
                uv_sphere_001.location = (-646.59912109375, -66.96932983398438)
                transform_geometry_001.location = (-438.66546630859375, -69.52670288085938)
                cone.location = (-649.1116943359375, 173.7689208984375)
                join_geometry_001.location = (-84.9557876586914, 174.65281677246094)
                transform_geometry_002.location = (-343.2873840332031, 181.1923370361328)
                group_001.location = (-645.0306396484375, 76.7733154296875)
                join_geometry.location = (255.43472290039062, 219.88165283203125)
                transform_geometry_003.location = (-110.77714538574219, 69.7738265991211)
                math_002.location = (-659.7962646484375, -1.2715530395507812)
                combine_xyz_001.location = (-467.7381896972656, 12.47930908203125)

                # Set dimensions
                group_input_1.width, group_input_1.height = 140.0, 100.0
                group_output_1.width, group_output_1.height = 140.0, 100.0
                uv_sphere_001.width, uv_sphere_001.height = 140.0, 100.0
                transform_geometry_001.width, transform_geometry_001.height = 140.0, 100.0
                cone.width, cone.height = 140.0, 100.0
                join_geometry_001.width, join_geometry_001.height = 140.0, 100.0
                transform_geometry_002.width, transform_geometry_002.height = 140.0, 100.0
                group_001.width, group_001.height = 140.0, 100.0
                join_geometry.width, join_geometry.height = 140.0, 100.0
                transform_geometry_003.width, transform_geometry_003.height = 140.0, 100.0
                math_002.width, math_002.height = 140.0, 100.0
                combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0

                # initialize joystick_gn links
                # uv_sphere_001.Mesh -> transform_geometry_001.Geometry
                joystick_gn.links.new(uv_sphere_001.outputs[0], transform_geometry_001.inputs[0])
                # transform_geometry_001.Geometry -> join_geometry_001.Geometry
                joystick_gn.links.new(transform_geometry_001.outputs[0], join_geometry_001.inputs[0])
                # cone.Mesh -> transform_geometry_002.Geometry
                joystick_gn.links.new(cone.outputs[0], transform_geometry_002.inputs[0])
                # transform_geometry_003.Geometry -> join_geometry.Geometry
                joystick_gn.links.new(transform_geometry_003.outputs[0], join_geometry.inputs[0])
                # group_001.Geometry -> transform_geometry_003.Geometry
                joystick_gn.links.new(group_001.outputs[0], transform_geometry_003.inputs[0])
                # group_input_1.Segments -> uv_sphere_001.Segments
                joystick_gn.links.new(group_input_1.outputs[1], uv_sphere_001.inputs[0])
                # group_input_1.Segments -> cone.Vertices
                joystick_gn.links.new(group_input_1.outputs[1], cone.inputs[0])
                # group_input_1.Segments -> group_001.Resolution
                joystick_gn.links.new(group_input_1.outputs[1], group_001.inputs[2])
                # group_input_1.Segments -> group_001.Radius2 Resolution
                joystick_gn.links.new(group_input_1.outputs[1], group_001.inputs[4])
                # group_input_1.Depth -> cone.Depth
                joystick_gn.links.new(group_input_1.outputs[2], cone.inputs[5])
                # group_input_1.Depth -> math_002.Value
                joystick_gn.links.new(group_input_1.outputs[2], math_002.inputs[0])
                # math_002.Value -> combine_xyz_001.Z
                joystick_gn.links.new(math_002.outputs[0], combine_xyz_001.inputs[2])
                # combine_xyz_001.Vector -> transform_geometry_003.Translation
                joystick_gn.links.new(combine_xyz_001.outputs[0], transform_geometry_003.inputs[1])
                # join_geometry.Geometry -> group_output_1.Geometry
                joystick_gn.links.new(join_geometry.outputs[0], group_output_1.inputs[0])
                # transform_geometry_002.Geometry -> join_geometry_001.Geometry
                joystick_gn.links.new(transform_geometry_002.outputs[0], join_geometry_001.inputs[0])
                # join_geometry_001.Geometry -> join_geometry.Geometry
                joystick_gn.links.new(join_geometry_001.outputs[0], join_geometry.inputs[0])
                return joystick_gn

        joystick_gn = joystick_gn_node_group()

        # initialize button_logic_gn node group
        def button_logic_gn_node_group():
                button_logic_gn = bpy.data.node_groups.new(type='GeometryNodeTree', name="Button_Logic_GN")

                button_logic_gn.color_tag = 'NONE'
                button_logic_gn.description = ""
                button_logic_gn.default_group_node_width = 140

                button_logic_gn.is_modifier = True

                # button_logic_gn interface
                # Socket Geometry
                geometry_socket_4 = button_logic_gn.interface.new_socket(name="Geometry", in_out='OUTPUT',
                                                                         socket_type='NodeSocketGeometry')
                geometry_socket_4.attribute_domain = 'POINT'

                # Socket Geometry
                geometry_socket_5 = button_logic_gn.interface.new_socket(name="Geometry", in_out='INPUT',
                                                                         socket_type='NodeSocketGeometry')
                geometry_socket_5.attribute_domain = 'POINT'

                # Socket Button Input
                button_input_socket = button_logic_gn.interface.new_socket(name="Button Input", in_out='INPUT',
                                                                           socket_type='NodeSocketFloat')
                button_input_socket.default_value = 0.5
                button_input_socket.min_value = -10000.0
                button_input_socket.max_value = 10000.0
                button_input_socket.subtype = 'NONE'
                button_input_socket.attribute_domain = 'POINT'

                # Socket Push Vector
                push_vector_socket = button_logic_gn.interface.new_socket(name="Push Vector", in_out='INPUT',
                                                                          socket_type='NodeSocketVector')
                push_vector_socket.default_value = (0.0, 0.0, 0.5)
                push_vector_socket.min_value = -10000.0
                push_vector_socket.max_value = 10000.0
                push_vector_socket.subtype = 'TRANSLATION'
                push_vector_socket.attribute_domain = 'POINT'

                # initialize button_logic_gn nodes
                # node Group Input
                group_input_2 = button_logic_gn.nodes.new("NodeGroupInput")
                group_input_2.name = "Group Input"

                # node Group Output
                group_output_2 = button_logic_gn.nodes.new("NodeGroupOutput")
                group_output_2.name = "Group Output"
                group_output_2.hide = True
                group_output_2.is_active_output = True

                # node Transform Geometry.002
                transform_geometry_002_1 = button_logic_gn.nodes.new("GeometryNodeTransform")
                transform_geometry_002_1.name = "Transform Geometry.002"
                transform_geometry_002_1.hide = True
                transform_geometry_002_1.mode = 'COMPONENTS'
                # Rotation
                transform_geometry_002_1.inputs[2].default_value = (0.0, 0.0, 0.0)
                # Scale
                transform_geometry_002_1.inputs[3].default_value = (1.0, 1.0, 1.0)

                # node Combine XYZ.002
                combine_xyz_002 = button_logic_gn.nodes.new("ShaderNodeCombineXYZ")
                combine_xyz_002.name = "Combine XYZ.002"
                combine_xyz_002.hide = True

                # node Math.002
                math_002_1 = button_logic_gn.nodes.new("ShaderNodeMath")
                math_002_1.name = "Math.002"
                math_002_1.hide = True
                math_002_1.operation = 'MULTIPLY'
                math_002_1.use_clamp = False
                # Value_001
                math_002_1.inputs[1].default_value = -0.09999996423721313

                # node Vector Math
                vector_math = button_logic_gn.nodes.new("ShaderNodeVectorMath")
                vector_math.name = "Vector Math"
                vector_math.hide = True
                vector_math.operation = 'MULTIPLY'

                # Set locations
                group_input_2.location = (-445.40362548828125, 434.5110168457031)
                group_output_2.location = (385.72454833984375, 388.6020812988281)
                transform_geometry_002_1.location = (227.1609649658203, 395.8033752441406)
                combine_xyz_002.location = (-101.93797302246094, 390.9135437011719)
                math_002_1.location = (-273.3974304199219, 379.93218994140625)
                vector_math.location = (47.08024597167969, 391.52923583984375)

                # Set dimensions
                group_input_2.width, group_input_2.height = 140.0, 100.0
                group_output_2.width, group_output_2.height = 140.0, 100.0
                transform_geometry_002_1.width, transform_geometry_002_1.height = 140.0, 100.0
                combine_xyz_002.width, combine_xyz_002.height = 140.0, 100.0
                math_002_1.width, math_002_1.height = 140.0, 100.0
                vector_math.width, vector_math.height = 140.0, 100.0

                # initialize button_logic_gn links
                # group_input_2.Button Input -> math_002_1.Value
                button_logic_gn.links.new(group_input_2.outputs[1], math_002_1.inputs[0])
                # transform_geometry_002_1.Geometry -> group_output_2.Geometry
                button_logic_gn.links.new(transform_geometry_002_1.outputs[0], group_output_2.inputs[0])
                # group_input_2.Geometry -> transform_geometry_002_1.Geometry
                button_logic_gn.links.new(group_input_2.outputs[0], transform_geometry_002_1.inputs[0])
                # group_input_2.Push Vector -> vector_math.Vector
                button_logic_gn.links.new(group_input_2.outputs[2], vector_math.inputs[1])
                # math_002_1.Value -> combine_xyz_002.X
                button_logic_gn.links.new(math_002_1.outputs[0], combine_xyz_002.inputs[0])
                # math_002_1.Value -> combine_xyz_002.Y
                button_logic_gn.links.new(math_002_1.outputs[0], combine_xyz_002.inputs[1])
                # math_002_1.Value -> combine_xyz_002.Z
                button_logic_gn.links.new(math_002_1.outputs[0], combine_xyz_002.inputs[2])
                # combine_xyz_002.Vector -> vector_math.Vector
                button_logic_gn.links.new(combine_xyz_002.outputs[0], vector_math.inputs[0])
                # vector_math.Vector -> transform_geometry_002_1.Translation
                button_logic_gn.links.new(vector_math.outputs[0], transform_geometry_002_1.inputs[1])
                return button_logic_gn

        button_logic_gn = button_logic_gn_node_group()

        # initialize d_pad_gn node group
        def d_pad_gn_node_group():
                d_pad_gn = bpy.data.node_groups.new(type='GeometryNodeTree', name="d_pad_GN")

                d_pad_gn.color_tag = 'NONE'
                d_pad_gn.description = ""
                d_pad_gn.default_group_node_width = 140

                d_pad_gn.is_modifier = True

                # d_pad_gn interface
                # Socket Geometry
                geometry_socket_6 = d_pad_gn.interface.new_socket(name="Geometry", in_out='OUTPUT',
                                                                  socket_type='NodeSocketGeometry')
                geometry_socket_6.attribute_domain = 'POINT'

                # Socket Geometry
                geometry_socket_7 = d_pad_gn.interface.new_socket(name="Geometry", in_out='INPUT',
                                                                  socket_type='NodeSocketGeometry')
                geometry_socket_7.attribute_domain = 'POINT'

                # Socket Depth
                depth_socket_1 = d_pad_gn.interface.new_socket(name="Depth", in_out='INPUT',
                                                               socket_type='NodeSocketFloat')
                depth_socket_1.default_value = 0.3999999761581421
                depth_socket_1.min_value = -10000.0
                depth_socket_1.max_value = 10000.0
                depth_socket_1.subtype = 'NONE'
                depth_socket_1.attribute_domain = 'POINT'

                # Socket Level
                level_socket = d_pad_gn.interface.new_socket(name="Level", in_out='INPUT', socket_type='NodeSocketInt')
                level_socket.default_value = 1
                level_socket.min_value = 0
                level_socket.max_value = 6
                level_socket.subtype = 'NONE'
                level_socket.attribute_domain = 'POINT'

                # Socket Level
                level_socket_1 = d_pad_gn.interface.new_socket(name="Level", in_out='INPUT',
                                                               socket_type='NodeSocketInt')
                level_socket_1.default_value = 1
                level_socket_1.min_value = 0
                level_socket_1.max_value = 6
                level_socket_1.subtype = 'NONE'
                level_socket_1.attribute_domain = 'POINT'

                # initialize d_pad_gn nodes
                # node Group Input
                group_input_3 = d_pad_gn.nodes.new("NodeGroupInput")
                group_input_3.name = "Group Input"

                # node Group Output
                group_output_3 = d_pad_gn.nodes.new("NodeGroupOutput")
                group_output_3.name = "Group Output"
                group_output_3.is_active_output = True

                # node Extrude Mesh
                extrude_mesh = d_pad_gn.nodes.new("GeometryNodeExtrudeMesh")
                extrude_mesh.name = "Extrude Mesh"
                extrude_mesh.mode = 'FACES'
                # Offset Scale
                extrude_mesh.inputs[3].default_value = -0.9999998807907104
                # Individual
                extrude_mesh.inputs[4].default_value = False

                # node Compare
                compare = d_pad_gn.nodes.new("FunctionNodeCompare")
                compare.name = "Compare"
                compare.data_type = 'INT'
                compare.mode = 'ELEMENT'
                compare.operation = 'EQUAL'
                # B_INT
                compare.inputs[3].default_value = 1

                # node Index
                index = d_pad_gn.nodes.new("GeometryNodeInputIndex")
                index.name = "Index"

                # node Combine XYZ
                combine_xyz = d_pad_gn.nodes.new("ShaderNodeCombineXYZ")
                combine_xyz.name = "Combine XYZ"
                # X
                combine_xyz.inputs[0].default_value = 0.0
                # Y
                combine_xyz.inputs[1].default_value = 1.0
                # Z
                combine_xyz.inputs[2].default_value = 0.0

                # node Cube
                cube = d_pad_gn.nodes.new("GeometryNodeMeshCube")
                cube.name = "Cube"
                # Vertices X
                cube.inputs[1].default_value = 2
                # Vertices Y
                cube.inputs[2].default_value = 2
                # Vertices Z
                cube.inputs[3].default_value = 2

                # node Repeat Input
                repeat_input = d_pad_gn.nodes.new("GeometryNodeRepeatInput")
                repeat_input.name = "Repeat Input"
                # node Repeat Output
                repeat_output = d_pad_gn.nodes.new("GeometryNodeRepeatOutput")
                repeat_output.name = "Repeat Output"
                repeat_output.active_index = 1
                repeat_output.inspection_index = 0
                repeat_output.repeat_items.clear()
                # Create item "Geometry"
                repeat_output.repeat_items.new('GEOMETRY', "Geometry")
                # Create item "Mesh"
                repeat_output.repeat_items.new('GEOMETRY', "Mesh")

                # node Extrude Mesh.001
                extrude_mesh_001 = d_pad_gn.nodes.new("GeometryNodeExtrudeMesh")
                extrude_mesh_001.name = "Extrude Mesh.001"
                extrude_mesh_001.mode = 'FACES'
                # Offset
                extrude_mesh_001.inputs[2].default_value = (0.0, 0.0, 0.0)
                # Offset Scale
                extrude_mesh_001.inputs[3].default_value = 0.9999998807907104
                # Individual
                extrude_mesh_001.inputs[4].default_value = False

                # node Compare.002
                compare_002 = d_pad_gn.nodes.new("FunctionNodeCompare")
                compare_002.name = "Compare.002"
                compare_002.data_type = 'INT'
                compare_002.mode = 'ELEMENT'
                compare_002.operation = 'EQUAL'
                # B_INT
                compare_002.inputs[3].default_value = 8

                # node Index.002
                index_002 = d_pad_gn.nodes.new("GeometryNodeInputIndex")
                index_002.name = "Index.002"

                # node Extrude Mesh.002
                extrude_mesh_002 = d_pad_gn.nodes.new("GeometryNodeExtrudeMesh")
                extrude_mesh_002.name = "Extrude Mesh.002"
                extrude_mesh_002.mode = 'FACES'
                # Offset
                extrude_mesh_002.inputs[2].default_value = (0.0, 0.0, 0.0)
                # Offset Scale
                extrude_mesh_002.inputs[3].default_value = 0.9999998807907104
                # Individual
                extrude_mesh_002.inputs[4].default_value = False

                # node Compare.003
                compare_003 = d_pad_gn.nodes.new("FunctionNodeCompare")
                compare_003.name = "Compare.003"
                compare_003.data_type = 'INT'
                compare_003.mode = 'ELEMENT'
                compare_003.operation = 'EQUAL'
                # B_INT
                compare_003.inputs[3].default_value = 7

                # node Index.003
                index_003 = d_pad_gn.nodes.new("GeometryNodeInputIndex")
                index_003.name = "Index.003"

                # node Extrude Mesh.003
                extrude_mesh_003 = d_pad_gn.nodes.new("GeometryNodeExtrudeMesh")
                extrude_mesh_003.name = "Extrude Mesh.003"
                extrude_mesh_003.mode = 'FACES'
                # Selection
                extrude_mesh_003.inputs[1].default_value = True
                # Offset
                extrude_mesh_003.inputs[2].default_value = (0.0, 0.0, 0.0)
                # Offset Scale
                extrude_mesh_003.inputs[3].default_value = -0.5
                # Individual
                extrude_mesh_003.inputs[4].default_value = True

                # node Compare.004
                compare_004 = d_pad_gn.nodes.new("FunctionNodeCompare")
                compare_004.name = "Compare.004"
                compare_004.data_type = 'INT'
                compare_004.mode = 'ELEMENT'
                compare_004.operation = 'EQUAL'
                # B_INT
                compare_004.inputs[3].default_value = 0

                # node Index.004
                index_004 = d_pad_gn.nodes.new("GeometryNodeInputIndex")
                index_004.name = "Index.004"

                # node Combine XYZ.002
                combine_xyz_002_1 = d_pad_gn.nodes.new("ShaderNodeCombineXYZ")
                combine_xyz_002_1.name = "Combine XYZ.002"
                # X
                combine_xyz_002_1.inputs[0].default_value = 1.0
                # Y
                combine_xyz_002_1.inputs[1].default_value = 1.0

                # node Subdivide Mesh
                subdivide_mesh = d_pad_gn.nodes.new("GeometryNodeSubdivideMesh")
                subdivide_mesh.name = "Subdivide Mesh"

                # Process zone input Repeat Input
                repeat_input.pair_with_output(repeat_output)
                # Iterations
                repeat_input.inputs[0].default_value = 2

                # Set locations
                group_input_3.location = (-926.5374145507812, 285.9710998535156)
                group_output_3.location = (1868.3955078125, 448.26495361328125)
                extrude_mesh.location = (-77.8603286743164, 426.1907043457031)
                compare.location = (-322.8431396484375, 133.90232849121094)
                index.location = (-508.02020263671875, 57.82164764404297)
                combine_xyz.location = (111.4140625, -16.468061447143555)
                cube.location = (-559.9576416015625, 367.74957275390625)
                repeat_input.location = (-268.8687438964844, 486.48333740234375)
                repeat_output.location = (144.17263793945312, 480.36346435546875)
                extrude_mesh_001.location = (576.6103515625, 455.05352783203125)
                compare_002.location = (387.4847106933594, 230.2265625)
                index_002.location = (280.2181091308594, -12.557048797607422)
                extrude_mesh_002.location = (865.3265991210938, 393.8542785644531)
                compare_003.location = (721.1157836914062, 131.95355224609375)
                index_003.location = (599.4863891601562, -99.76575469970703)
                extrude_mesh_003.location = (1095.9947509765625, 282.16546630859375)
                compare_004.location = (910.5386962890625, 76.8741455078125)
                index_004.location = (788.9093017578125, -154.84515380859375)
                combine_xyz_002_1.location = (-744.8878173828125, 275.7088928222656)
                subdivide_mesh.location = (1087.9937744140625, 502.4427490234375)

                # Set dimensions
                group_input_3.width, group_input_3.height = 140.0, 100.0
                group_output_3.width, group_output_3.height = 140.0, 100.0
                extrude_mesh.width, extrude_mesh.height = 140.0, 100.0
                compare.width, compare.height = 140.0, 100.0
                index.width, index.height = 140.0, 100.0
                combine_xyz.width, combine_xyz.height = 140.0, 100.0
                cube.width, cube.height = 140.0, 100.0
                repeat_input.width, repeat_input.height = 140.0, 100.0
                repeat_output.width, repeat_output.height = 140.0, 100.0
                extrude_mesh_001.width, extrude_mesh_001.height = 140.0, 100.0
                compare_002.width, compare_002.height = 140.0, 100.0
                index_002.width, index_002.height = 140.0, 100.0
                extrude_mesh_002.width, extrude_mesh_002.height = 140.0, 100.0
                compare_003.width, compare_003.height = 140.0, 100.0
                index_003.width, index_003.height = 140.0, 100.0
                extrude_mesh_003.width, extrude_mesh_003.height = 140.0, 100.0
                compare_004.width, compare_004.height = 140.0, 100.0
                index_004.width, index_004.height = 140.0, 100.0
                combine_xyz_002_1.width, combine_xyz_002_1.height = 140.0, 100.0
                subdivide_mesh.width, subdivide_mesh.height = 140.0, 100.0

                # initialize d_pad_gn links
                # index.Index -> compare.A
                d_pad_gn.links.new(index.outputs[0], compare.inputs[2])
                # compare.Result -> extrude_mesh.Selection
                d_pad_gn.links.new(compare.outputs[0], extrude_mesh.inputs[1])
                # combine_xyz.Vector -> extrude_mesh.Offset
                d_pad_gn.links.new(combine_xyz.outputs[0], extrude_mesh.inputs[2])
                # cube.Mesh -> repeat_input.Geometry
                d_pad_gn.links.new(cube.outputs[0], repeat_input.inputs[1])
                # repeat_input.Geometry -> extrude_mesh.Mesh
                d_pad_gn.links.new(repeat_input.outputs[1], extrude_mesh.inputs[0])
                # index_002.Index -> compare_002.A
                d_pad_gn.links.new(index_002.outputs[0], compare_002.inputs[2])
                # compare_002.Result -> extrude_mesh_001.Selection
                d_pad_gn.links.new(compare_002.outputs[0], extrude_mesh_001.inputs[1])
                # repeat_output.Geometry -> extrude_mesh_001.Mesh
                d_pad_gn.links.new(repeat_output.outputs[0], extrude_mesh_001.inputs[0])
                # index_003.Index -> compare_003.A
                d_pad_gn.links.new(index_003.outputs[0], compare_003.inputs[2])
                # compare_003.Result -> extrude_mesh_002.Selection
                d_pad_gn.links.new(compare_003.outputs[0], extrude_mesh_002.inputs[1])
                # extrude_mesh_001.Mesh -> extrude_mesh_002.Mesh
                d_pad_gn.links.new(extrude_mesh_001.outputs[0], extrude_mesh_002.inputs[0])
                # index_004.Index -> compare_004.A
                d_pad_gn.links.new(index_004.outputs[0], compare_004.inputs[2])
                # extrude_mesh_002.Mesh -> extrude_mesh_003.Mesh
                d_pad_gn.links.new(extrude_mesh_002.outputs[0], extrude_mesh_003.inputs[0])
                # combine_xyz_002_1.Vector -> cube.Size
                d_pad_gn.links.new(combine_xyz_002_1.outputs[0], cube.inputs[0])
                # group_input_3.Depth -> combine_xyz_002_1.Z
                d_pad_gn.links.new(group_input_3.outputs[1], combine_xyz_002_1.inputs[2])
                # extrude_mesh_002.Mesh -> subdivide_mesh.Mesh
                d_pad_gn.links.new(extrude_mesh_002.outputs[0], subdivide_mesh.inputs[0])
                # group_input_3.Level -> subdivide_mesh.Level
                d_pad_gn.links.new(group_input_3.outputs[3], subdivide_mesh.inputs[1])
                # subdivide_mesh.Mesh -> group_output_3.Geometry
                d_pad_gn.links.new(subdivide_mesh.outputs[0], group_output_3.inputs[0])
                # extrude_mesh.Mesh -> repeat_output.Geometry
                d_pad_gn.links.new(extrude_mesh.outputs[0], repeat_output.inputs[0])
                return d_pad_gn

        d_pad_gn = d_pad_gn_node_group()

        # initialize axis_1d_gn node group
        def axis_1d_gn_node_group():
                axis_1d_gn = bpy.data.node_groups.new(type='GeometryNodeTree', name="Axis_1D_GN")

                axis_1d_gn.color_tag = 'NONE'
                axis_1d_gn.description = ""
                axis_1d_gn.default_group_node_width = 140

                axis_1d_gn.is_modifier = True

                # axis_1d_gn interface
                # Socket Geometry
                geometry_socket_8 = axis_1d_gn.interface.new_socket(name="Geometry", in_out='OUTPUT',
                                                                    socket_type='NodeSocketGeometry')
                geometry_socket_8.attribute_domain = 'POINT'

                # Socket Geometry
                geometry_socket_9 = axis_1d_gn.interface.new_socket(name="Geometry", in_out='INPUT',
                                                                    socket_type='NodeSocketGeometry')
                geometry_socket_9.attribute_domain = 'POINT'

                # Socket Axis Input
                axis_input_socket = axis_1d_gn.interface.new_socket(name="Axis Input", in_out='INPUT',
                                                                    socket_type='NodeSocketFloat')
                axis_input_socket.default_value = 0.5
                axis_input_socket.min_value = -10000.0
                axis_input_socket.max_value = 10000.0
                axis_input_socket.subtype = 'NONE'
                axis_input_socket.attribute_domain = 'POINT'

                # Socket Direction / Scale
                direction___scale_socket = axis_1d_gn.interface.new_socket(name="Direction / Scale", in_out='INPUT',
                                                                           socket_type='NodeSocketFloat')
                direction___scale_socket.default_value = -0.20000000298023224
                direction___scale_socket.min_value = -10000.0
                direction___scale_socket.max_value = 10000.0
                direction___scale_socket.subtype = 'NONE'
                direction___scale_socket.attribute_domain = 'POINT'

                # Socket Switch
                switch_socket = axis_1d_gn.interface.new_socket(name="Switch", in_out='INPUT',
                                                                socket_type='NodeSocketBool')
                switch_socket.default_value = False
                switch_socket.attribute_domain = 'POINT'

                # initialize axis_1d_gn nodes
                # node Group Input
                group_input_4 = axis_1d_gn.nodes.new("NodeGroupInput")
                group_input_4.name = "Group Input"

                # node Group Output
                group_output_4 = axis_1d_gn.nodes.new("NodeGroupOutput")
                group_output_4.name = "Group Output"
                group_output_4.is_active_output = True

                # node Cube
                cube_1 = axis_1d_gn.nodes.new("GeometryNodeMeshCube")
                cube_1.name = "Cube"
                # Size
                cube_1.inputs[0].default_value = (1.7299997806549072, 1.499999761581421, 1.2000000476837158)
                # Vertices X
                cube_1.inputs[1].default_value = 2
                # Vertices Y
                cube_1.inputs[2].default_value = 2
                # Vertices Z
                cube_1.inputs[3].default_value = 2

                # node Transform Geometry
                transform_geometry_1 = axis_1d_gn.nodes.new("GeometryNodeTransform")
                transform_geometry_1.name = "Transform Geometry"
                transform_geometry_1.mode = 'COMPONENTS'
                # Rotation
                transform_geometry_1.inputs[2].default_value = (0.0, 0.0, 0.0)
                # Scale
                transform_geometry_1.inputs[3].default_value = (1.0, 1.0, 1.0)

                # node Combine XYZ
                combine_xyz_1 = axis_1d_gn.nodes.new("ShaderNodeCombineXYZ")
                combine_xyz_1.name = "Combine XYZ"
                # Y
                combine_xyz_1.inputs[1].default_value = 0.0
                # Z
                combine_xyz_1.inputs[2].default_value = 0.0

                # node Math
                math = axis_1d_gn.nodes.new("ShaderNodeMath")
                math.name = "Math"
                math.operation = 'MULTIPLY'
                math.use_clamp = False

                # node Switch
                switch = axis_1d_gn.nodes.new("GeometryNodeSwitch")
                switch.name = "Switch"
                switch.input_type = 'GEOMETRY'

                # Set locations
                group_input_4.location = (-662.5313720703125, -33.12626266479492)
                group_output_4.location = (117.24581146240234, -52.815486907958984)
                cube_1.location = (-630.844482421875, 437.41015625)
                transform_geometry_1.location = (-76.92967224121094, 422.2558898925781)
                combine_xyz_1.location = (-253.81678771972656, 200.67514038085938)
                math.location = (-406.927978515625, 70.11377716064453)
                switch.location = (-415.1772766113281, 344.00201416015625)

                # Set dimensions
                group_input_4.width, group_input_4.height = 140.0, 100.0
                group_output_4.width, group_output_4.height = 140.0, 100.0
                cube_1.width, cube_1.height = 140.0, 100.0
                transform_geometry_1.width, transform_geometry_1.height = 140.0, 100.0
                combine_xyz_1.width, combine_xyz_1.height = 140.0, 100.0
                math.width, math.height = 140.0, 100.0
                switch.width, switch.height = 140.0, 100.0

                # initialize axis_1d_gn links
                # transform_geometry_1.Geometry -> group_output_4.Geometry
                axis_1d_gn.links.new(transform_geometry_1.outputs[0], group_output_4.inputs[0])
                # combine_xyz_1.Vector -> transform_geometry_1.Translation
                axis_1d_gn.links.new(combine_xyz_1.outputs[0], transform_geometry_1.inputs[1])
                # math.Value -> combine_xyz_1.X
                axis_1d_gn.links.new(math.outputs[0], combine_xyz_1.inputs[0])
                # group_input_4.Axis Input -> math.Value
                axis_1d_gn.links.new(group_input_4.outputs[1], math.inputs[0])
                # group_input_4.Direction / Scale -> math.Value
                axis_1d_gn.links.new(group_input_4.outputs[2], math.inputs[1])
                # cube_1.Mesh -> switch.False
                axis_1d_gn.links.new(cube_1.outputs[0], switch.inputs[1])
                # group_input_4.Geometry -> switch.True
                axis_1d_gn.links.new(group_input_4.outputs[0], switch.inputs[2])
                # switch.Output -> transform_geometry_1.Geometry
                axis_1d_gn.links.new(switch.outputs[0], transform_geometry_1.inputs[0])
                # group_input_4.Switch -> switch.Switch
                axis_1d_gn.links.new(group_input_4.outputs[3], switch.inputs[0])
                return axis_1d_gn

        axis_1d_gn = axis_1d_gn_node_group()

        # initialize axis_2d_gn node group
        def axis_2d_gn_node_group():
                axis_2d_gn = bpy.data.node_groups.new(type='GeometryNodeTree', name="Axis_2D_GN")

                axis_2d_gn.color_tag = 'NONE'
                axis_2d_gn.description = ""
                axis_2d_gn.default_group_node_width = 140

                axis_2d_gn.is_modifier = True

                # axis_2d_gn interface
                # Socket Geometry
                geometry_socket_10 = axis_2d_gn.interface.new_socket(name="Geometry", in_out='OUTPUT',
                                                                     socket_type='NodeSocketGeometry')
                geometry_socket_10.attribute_domain = 'POINT'

                # Socket Geometry
                geometry_socket_11 = axis_2d_gn.interface.new_socket(name="Geometry", in_out='INPUT',
                                                                     socket_type='NodeSocketGeometry')
                geometry_socket_11.attribute_domain = 'POINT'

                # Socket X_axis_input
                x_axis_input_socket = axis_2d_gn.interface.new_socket(name="X_axis_input", in_out='INPUT',
                                                                      socket_type='NodeSocketFloat')
                x_axis_input_socket.default_value = 0.5
                x_axis_input_socket.min_value = -10000.0
                x_axis_input_socket.max_value = 10000.0
                x_axis_input_socket.subtype = 'NONE'
                x_axis_input_socket.attribute_domain = 'POINT'

                # Socket Y_axis_input
                y_axis_input_socket = axis_2d_gn.interface.new_socket(name="Y_axis_input", in_out='INPUT',
                                                                      socket_type='NodeSocketFloat')
                y_axis_input_socket.default_value = 0.5
                y_axis_input_socket.min_value = -10000.0
                y_axis_input_socket.max_value = 10000.0
                y_axis_input_socket.subtype = 'NONE'
                y_axis_input_socket.attribute_domain = 'POINT'

                # Socket X_scale
                x_scale_socket = axis_2d_gn.interface.new_socket(name="X_scale", in_out='INPUT',
                                                                 socket_type='NodeSocketFloat')
                x_scale_socket.default_value = 0.9999998807907104
                x_scale_socket.min_value = -10000.0
                x_scale_socket.max_value = 10000.0
                x_scale_socket.subtype = 'NONE'
                x_scale_socket.attribute_domain = 'POINT'

                # Socket Y_scale
                y_scale_socket = axis_2d_gn.interface.new_socket(name="Y_scale", in_out='INPUT',
                                                                 socket_type='NodeSocketFloat')
                y_scale_socket.default_value = -1.0
                y_scale_socket.min_value = -10000.0
                y_scale_socket.max_value = 10000.0
                y_scale_socket.subtype = 'NONE'
                y_scale_socket.attribute_domain = 'POINT'

                # initialize axis_2d_gn nodes
                # node Group Input
                group_input_5 = axis_2d_gn.nodes.new("NodeGroupInput")
                group_input_5.name = "Group Input"

                # node Group Output
                group_output_5 = axis_2d_gn.nodes.new("NodeGroupOutput")
                group_output_5.name = "Group Output"
                group_output_5.is_active_output = True

                # node Transform Geometry
                transform_geometry_2 = axis_2d_gn.nodes.new("GeometryNodeTransform")
                transform_geometry_2.name = "Transform Geometry"
                transform_geometry_2.hide = True
                transform_geometry_2.mode = 'COMPONENTS'
                # Translation
                transform_geometry_2.inputs[1].default_value = (0.0, 0.0, 0.0)
                # Scale
                transform_geometry_2.inputs[3].default_value = (1.0, 1.0, 1.0)

                # node Combine XYZ
                combine_xyz_2 = axis_2d_gn.nodes.new("ShaderNodeCombineXYZ")
                combine_xyz_2.name = "Combine XYZ"
                combine_xyz_2.hide = True
                # Z
                combine_xyz_2.inputs[2].default_value = 0.0

                # node Math
                math_1 = axis_2d_gn.nodes.new("ShaderNodeMath")
                math_1.name = "Math"
                math_1.hide = True
                math_1.operation = 'MULTIPLY'
                math_1.use_clamp = False

                # node Math.001
                math_001 = axis_2d_gn.nodes.new("ShaderNodeMath")
                math_001.name = "Math.001"
                math_001.hide = True
                math_001.operation = 'MULTIPLY'
                math_001.use_clamp = False

                # Set locations
                group_input_5.location = (-544.6334838867188, 156.63775634765625)
                group_output_5.location = (294.2889099121094, 138.58518981933594)
                transform_geometry_2.location = (131.7014617919922, 155.75350952148438)
                combine_xyz_2.location = (-40.74589157104492, 108.21852111816406)
                math_1.location = (-231.0360107421875, 117.06878662109375)
                math_001.location = (-234.11196899414062, 70.06074523925781)

                # Set dimensions
                group_input_5.width, group_input_5.height = 140.0, 100.0
                group_output_5.width, group_output_5.height = 140.0, 100.0
                transform_geometry_2.width, transform_geometry_2.height = 140.0, 100.0
                combine_xyz_2.width, combine_xyz_2.height = 140.0, 100.0
                math_1.width, math_1.height = 140.0, 100.0
                math_001.width, math_001.height = 140.0, 100.0

                # initialize axis_2d_gn links
                # math_1.Value -> combine_xyz_2.X
                axis_2d_gn.links.new(math_1.outputs[0], combine_xyz_2.inputs[0])
                # math_001.Value -> combine_xyz_2.Y
                axis_2d_gn.links.new(math_001.outputs[0], combine_xyz_2.inputs[1])
                # combine_xyz_2.Vector -> transform_geometry_2.Rotation
                axis_2d_gn.links.new(combine_xyz_2.outputs[0], transform_geometry_2.inputs[2])
                # group_input_5.Geometry -> transform_geometry_2.Geometry
                axis_2d_gn.links.new(group_input_5.outputs[0], transform_geometry_2.inputs[0])
                # transform_geometry_2.Geometry -> group_output_5.Geometry
                axis_2d_gn.links.new(transform_geometry_2.outputs[0], group_output_5.inputs[0])
                # group_input_5.X_axis_input -> math_1.Value
                axis_2d_gn.links.new(group_input_5.outputs[1], math_1.inputs[0])
                # group_input_5.Y_axis_input -> math_001.Value
                axis_2d_gn.links.new(group_input_5.outputs[2], math_001.inputs[0])
                # group_input_5.X_scale -> math_1.Value
                axis_2d_gn.links.new(group_input_5.outputs[3], math_1.inputs[1])
                # group_input_5.Y_scale -> math_001.Value
                axis_2d_gn.links.new(group_input_5.outputs[4], math_001.inputs[1])
                return axis_2d_gn

        axis_2d_gn = axis_2d_gn_node_group()

        # initialize d_pad_logic_gn node group
        def d_pad_logic_gn_node_group():
                d_pad_logic_gn = bpy.data.node_groups.new(type='GeometryNodeTree', name="D_Pad_Logic_GN")

                d_pad_logic_gn.color_tag = 'NONE'
                d_pad_logic_gn.description = ""
                d_pad_logic_gn.default_group_node_width = 140

                d_pad_logic_gn.is_modifier = True

                # d_pad_logic_gn interface
                # Socket Geometry
                geometry_socket_12 = d_pad_logic_gn.interface.new_socket(name="Geometry", in_out='OUTPUT',
                                                                         socket_type='NodeSocketGeometry')
                geometry_socket_12.attribute_domain = 'POINT'

                # Socket Geometry
                geometry_socket_13 = d_pad_logic_gn.interface.new_socket(name="Geometry", in_out='INPUT',
                                                                         socket_type='NodeSocketGeometry')
                geometry_socket_13.attribute_domain = 'POINT'

                # Socket X_Input_D_Pad
                x_input_d_pad_socket = d_pad_logic_gn.interface.new_socket(name="X_Input_D_Pad", in_out='INPUT',
                                                                           socket_type='NodeSocketFloat')
                x_input_d_pad_socket.default_value = 0.5
                x_input_d_pad_socket.min_value = -10000.0
                x_input_d_pad_socket.max_value = 10000.0
                x_input_d_pad_socket.subtype = 'NONE'
                x_input_d_pad_socket.attribute_domain = 'POINT'

                # Socket Y_Input_D_Pad
                y_input_d_pad_socket = d_pad_logic_gn.interface.new_socket(name="Y_Input_D_Pad", in_out='INPUT',
                                                                           socket_type='NodeSocketFloat')
                y_input_d_pad_socket.default_value = 0.5
                y_input_d_pad_socket.min_value = -10000.0
                y_input_d_pad_socket.max_value = 10000.0
                y_input_d_pad_socket.subtype = 'NONE'
                y_input_d_pad_socket.attribute_domain = 'POINT'

                # Socket X_Scale
                x_scale_socket_1 = d_pad_logic_gn.interface.new_socket(name="X_Scale", in_out='INPUT',
                                                                       socket_type='NodeSocketFloat')
                x_scale_socket_1.default_value = 0.12000000476837158
                x_scale_socket_1.min_value = -10000.0
                x_scale_socket_1.max_value = 10000.0
                x_scale_socket_1.subtype = 'NONE'
                x_scale_socket_1.attribute_domain = 'POINT'

                # Socket Y_Scale
                y_scale_socket_1 = d_pad_logic_gn.interface.new_socket(name="Y_Scale", in_out='INPUT',
                                                                       socket_type='NodeSocketFloat')
                y_scale_socket_1.default_value = 0.12000000476837158
                y_scale_socket_1.min_value = -10000.0
                y_scale_socket_1.max_value = 10000.0
                y_scale_socket_1.subtype = 'NONE'
                y_scale_socket_1.attribute_domain = 'POINT'

                # initialize d_pad_logic_gn nodes
                # node Group Input
                group_input_6 = d_pad_logic_gn.nodes.new("NodeGroupInput")
                group_input_6.name = "Group Input"

                # node Group Output
                group_output_6 = d_pad_logic_gn.nodes.new("NodeGroupOutput")
                group_output_6.name = "Group Output"
                group_output_6.hide = True
                group_output_6.is_active_output = True

                # node Transform Geometry.006
                transform_geometry_006 = d_pad_logic_gn.nodes.new("GeometryNodeTransform")
                transform_geometry_006.name = "Transform Geometry.006"
                transform_geometry_006.hide = True
                transform_geometry_006.mode = 'COMPONENTS'
                # Translation
                transform_geometry_006.inputs[1].default_value = (2.999999761581421, 1.999999761581421, 1.0)
                # Scale
                transform_geometry_006.inputs[3].default_value = (1.0, 1.0, 1.0)

                # node Combine XYZ
                combine_xyz_3 = d_pad_logic_gn.nodes.new("ShaderNodeCombineXYZ")
                combine_xyz_3.name = "Combine XYZ"
                combine_xyz_3.hide = True
                # Z
                combine_xyz_3.inputs[2].default_value = 0.0

                # node Math
                math_2 = d_pad_logic_gn.nodes.new("ShaderNodeMath")
                math_2.name = "Math"
                math_2.hide = True
                math_2.operation = 'MULTIPLY'
                math_2.use_clamp = False

                # node Math.001
                math_001_1 = d_pad_logic_gn.nodes.new("ShaderNodeMath")
                math_001_1.name = "Math.001"
                math_001_1.hide = True
                math_001_1.operation = 'MULTIPLY'
                math_001_1.use_clamp = False

                # Set locations
                group_input_6.location = (177.80894470214844, -95.1830062866211)
                group_output_6.location = (1021.6915283203125, 99.89913940429688)
                transform_geometry_006.location = (826.3712768554688, 103.74352264404297)
                combine_xyz_3.location = (656.8683471679688, -49.0809326171875)
                math_2.location = (428.06732177734375, -204.22250366210938)
                math_001_1.location = (425.8558349609375, -144.99774169921875)

                # Set dimensions
                group_input_6.width, group_input_6.height = 140.0, 100.0
                group_output_6.width, group_output_6.height = 140.0, 100.0
                transform_geometry_006.width, transform_geometry_006.height = 140.0, 100.0
                combine_xyz_3.width, combine_xyz_3.height = 140.0, 100.0
                math_2.width, math_2.height = 140.0, 100.0
                math_001_1.width, math_001_1.height = 140.0, 100.0

                # initialize d_pad_logic_gn links
                # combine_xyz_3.Vector -> transform_geometry_006.Rotation
                d_pad_logic_gn.links.new(combine_xyz_3.outputs[0], transform_geometry_006.inputs[2])
                # math_2.Value -> combine_xyz_3.Y
                d_pad_logic_gn.links.new(math_2.outputs[0], combine_xyz_3.inputs[1])
                # math_001_1.Value -> combine_xyz_3.X
                d_pad_logic_gn.links.new(math_001_1.outputs[0], combine_xyz_3.inputs[0])
                # transform_geometry_006.Geometry -> group_output_6.Geometry
                d_pad_logic_gn.links.new(transform_geometry_006.outputs[0], group_output_6.inputs[0])
                # group_input_6.Geometry -> transform_geometry_006.Geometry
                d_pad_logic_gn.links.new(group_input_6.outputs[0], transform_geometry_006.inputs[0])
                # group_input_6.X_Input_D_Pad -> math_001_1.Value
                d_pad_logic_gn.links.new(group_input_6.outputs[1], math_001_1.inputs[0])
                # group_input_6.Y_Input_D_Pad -> math_2.Value
                d_pad_logic_gn.links.new(group_input_6.outputs[2], math_2.inputs[0])
                # group_input_6.X_Scale -> math_001_1.Value
                d_pad_logic_gn.links.new(group_input_6.outputs[3], math_001_1.inputs[1])
                # group_input_6.Y_Scale -> math_2.Value
                d_pad_logic_gn.links.new(group_input_6.outputs[4], math_2.inputs[1])
                return d_pad_logic_gn

        d_pad_logic_gn = d_pad_logic_gn_node_group()

        # initialize start_select_button_gn node group
        def start_select_button_gn_node_group():
                start_select_button_gn = bpy.data.node_groups.new(type='GeometryNodeTree',
                                                                  name="Start_Select_Button_GN")

                start_select_button_gn.color_tag = 'NONE'
                start_select_button_gn.description = ""
                start_select_button_gn.default_group_node_width = 140

                start_select_button_gn.is_modifier = True

                # start_select_button_gn interface
                # Socket Geometry
                geometry_socket_14 = start_select_button_gn.interface.new_socket(name="Geometry", in_out='OUTPUT',
                                                                                 socket_type='NodeSocketGeometry')
                geometry_socket_14.attribute_domain = 'POINT'

                # Socket Geometry
                geometry_socket_15 = start_select_button_gn.interface.new_socket(name="Geometry", in_out='INPUT',
                                                                                 socket_type='NodeSocketGeometry')
                geometry_socket_15.attribute_domain = 'POINT'

                # initialize start_select_button_gn nodes
                # node Group Input
                group_input_7 = start_select_button_gn.nodes.new("NodeGroupInput")
                group_input_7.name = "Group Input"

                # node Group Output
                group_output_7 = start_select_button_gn.nodes.new("NodeGroupOutput")
                group_output_7.name = "Group Output"
                group_output_7.is_active_output = True

                # node Curve to Mesh
                curve_to_mesh_1 = start_select_button_gn.nodes.new("GeometryNodeCurveToMesh")
                curve_to_mesh_1.name = "Curve to Mesh"
                # Fill Caps
                curve_to_mesh_1.inputs[2].default_value = True

                # node Curve Circle
                curve_circle_1 = start_select_button_gn.nodes.new("GeometryNodeCurvePrimitiveCircle")
                curve_circle_1.name = "Curve Circle"
                curve_circle_1.mode = 'RADIUS'
                # Resolution
                curve_circle_1.inputs[0].default_value = 10
                # Radius
                curve_circle_1.inputs[4].default_value = 0.7000000476837158

                # node Transform Geometry
                transform_geometry_3 = start_select_button_gn.nodes.new("GeometryNodeTransform")
                transform_geometry_3.name = "Transform Geometry"
                transform_geometry_3.mode = 'COMPONENTS'
                # Translation
                transform_geometry_3.inputs[1].default_value = (0.0, 0.0, 0.0)
                # Rotation
                transform_geometry_3.inputs[2].default_value = (0.0, 0.0, 0.0)
                # Scale
                transform_geometry_3.inputs[3].default_value = (0.5, 1.399999976158142, 1.0)

                # node Mesh Line
                mesh_line = start_select_button_gn.nodes.new("GeometryNodeMeshLine")
                mesh_line.name = "Mesh Line"
                mesh_line.count_mode = 'TOTAL'
                mesh_line.mode = 'OFFSET'
                # Count
                mesh_line.inputs[0].default_value = 3
                # Start Location
                mesh_line.inputs[2].default_value = (0.0, 0.0, 0.0)
                # Offset
                mesh_line.inputs[3].default_value = (0.0, 0.0, 1.0)

                # node Mesh to Curve
                mesh_to_curve = start_select_button_gn.nodes.new("GeometryNodeMeshToCurve")
                mesh_to_curve.name = "Mesh to Curve"
                # Selection
                mesh_to_curve.inputs[1].default_value = True

                # node Transform Geometry.001
                transform_geometry_001_1 = start_select_button_gn.nodes.new("GeometryNodeTransform")
                transform_geometry_001_1.name = "Transform Geometry.001"
                transform_geometry_001_1.mode = 'COMPONENTS'
                # Translation
                transform_geometry_001_1.inputs[1].default_value = (0.0, 0.0, 0.0)
                # Rotation
                transform_geometry_001_1.inputs[2].default_value = (0.0, 0.0, 0.0)
                # Scale
                transform_geometry_001_1.inputs[3].default_value = (1.0, 1.0, 0.1300000548362732)

                # Set locations
                group_input_7.location = (-340.0, 0.0)
                group_output_7.location = (1091.3912353515625, 249.05201721191406)
                curve_to_mesh_1.location = (370.8960876464844, 252.18701171875)
                curve_circle_1.location = (-44.4378662109375, 37.83763122558594)
                transform_geometry_3.location = (135.99998474121094, 73.09017181396484)
                mesh_line.location = (-68.64918518066406, 346.1900939941406)
                mesh_to_curve.location = (139.3766632080078, 309.2354736328125)
                transform_geometry_001_1.location = (561.0657958984375, 256.5229187011719)

                # Set dimensions
                group_input_7.width, group_input_7.height = 140.0, 100.0
                group_output_7.width, group_output_7.height = 140.0, 100.0
                curve_to_mesh_1.width, curve_to_mesh_1.height = 140.0, 100.0
                curve_circle_1.width, curve_circle_1.height = 140.0, 100.0
                transform_geometry_3.width, transform_geometry_3.height = 140.0, 100.0
                mesh_line.width, mesh_line.height = 140.0, 100.0
                mesh_to_curve.width, mesh_to_curve.height = 140.0, 100.0
                transform_geometry_001_1.width, transform_geometry_001_1.height = 140.0, 100.0

                # initialize start_select_button_gn links
                # transform_geometry_3.Geometry -> curve_to_mesh_1.Profile Curve
                start_select_button_gn.links.new(transform_geometry_3.outputs[0], curve_to_mesh_1.inputs[1])
                # curve_circle_1.Curve -> transform_geometry_3.Geometry
                start_select_button_gn.links.new(curve_circle_1.outputs[0], transform_geometry_3.inputs[0])
                # mesh_line.Mesh -> mesh_to_curve.Mesh
                start_select_button_gn.links.new(mesh_line.outputs[0], mesh_to_curve.inputs[0])
                # mesh_to_curve.Curve -> curve_to_mesh_1.Curve
                start_select_button_gn.links.new(mesh_to_curve.outputs[0], curve_to_mesh_1.inputs[0])
                # curve_to_mesh_1.Mesh -> transform_geometry_001_1.Geometry
                start_select_button_gn.links.new(curve_to_mesh_1.outputs[0], transform_geometry_001_1.inputs[0])
                # transform_geometry_001_1.Geometry -> group_output_7.Geometry
                start_select_button_gn.links.new(transform_geometry_001_1.outputs[0], group_output_7.inputs[0])
                return start_select_button_gn

        start_select_button_gn = start_select_button_gn_node_group()

        # initialize gamepad_case_gn node group
        def gamepad_case_gn_node_group():
                gamepad_case_gn = bpy.data.node_groups.new(type='GeometryNodeTree', name="Gamepad_Case_GN")

                gamepad_case_gn.color_tag = 'NONE'
                gamepad_case_gn.description = ""
                gamepad_case_gn.default_group_node_width = 140

                gamepad_case_gn.is_modifier = True

                # gamepad_case_gn interface
                # Socket Geometry
                geometry_socket_16 = gamepad_case_gn.interface.new_socket(name="Geometry", in_out='OUTPUT',
                                                                          socket_type='NodeSocketGeometry')
                geometry_socket_16.attribute_domain = 'POINT'

                # Socket Geometry
                geometry_socket_17 = gamepad_case_gn.interface.new_socket(name="Geometry", in_out='INPUT',
                                                                          socket_type='NodeSocketGeometry')
                geometry_socket_17.attribute_domain = 'POINT'

                # Socket Size
                size_socket = gamepad_case_gn.interface.new_socket(name="Size", in_out='INPUT',
                                                                   socket_type='NodeSocketVector')
                size_socket.default_value = (0.6499999761581421, 1.0, 0.6000000238418579)
                size_socket.min_value = 0.0
                size_socket.max_value = 3.4028234663852886e+38
                size_socket.subtype = 'TRANSLATION'
                size_socket.attribute_domain = 'POINT'

                # Socket Offset Scale
                offset_scale_socket = gamepad_case_gn.interface.new_socket(name="Offset Scale", in_out='INPUT',
                                                                           socket_type='NodeSocketFloat')
                offset_scale_socket.default_value = 0.36000001430511475
                offset_scale_socket.min_value = -3.4028234663852886e+38
                offset_scale_socket.max_value = 3.4028234663852886e+38
                offset_scale_socket.subtype = 'NONE'
                offset_scale_socket.attribute_domain = 'POINT'

                # Socket X
                x_socket = gamepad_case_gn.interface.new_socket(name="X", in_out='INPUT', socket_type='NodeSocketFloat')
                x_socket.default_value = 0.0
                x_socket.min_value = -10000.0
                x_socket.max_value = 10000.0
                x_socket.subtype = 'NONE'
                x_socket.attribute_domain = 'POINT'

                # Socket Z
                z_socket = gamepad_case_gn.interface.new_socket(name="Z", in_out='INPUT', socket_type='NodeSocketFloat')
                z_socket.default_value = 0.0
                z_socket.min_value = -10000.0
                z_socket.max_value = 10000.0
                z_socket.subtype = 'NONE'
                z_socket.attribute_domain = 'POINT'

                # Socket Offset Scale
                offset_scale_socket_1 = gamepad_case_gn.interface.new_socket(name="Offset Scale", in_out='INPUT',
                                                                             socket_type='NodeSocketFloat')
                offset_scale_socket_1.default_value = 0.9599999189376831
                offset_scale_socket_1.min_value = -3.4028234663852886e+38
                offset_scale_socket_1.max_value = 3.4028234663852886e+38
                offset_scale_socket_1.subtype = 'NONE'
                offset_scale_socket_1.attribute_domain = 'POINT'

                # initialize gamepad_case_gn nodes
                # node Group Input
                group_input_8 = gamepad_case_gn.nodes.new("NodeGroupInput")
                group_input_8.name = "Group Input"

                # node Group Output
                group_output_8 = gamepad_case_gn.nodes.new("NodeGroupOutput")
                group_output_8.name = "Group Output"
                group_output_8.is_active_output = True

                # node Cube
                cube_2 = gamepad_case_gn.nodes.new("GeometryNodeMeshCube")
                cube_2.name = "Cube"
                cube_2.hide = True
                # Vertices X
                cube_2.inputs[1].default_value = 2
                # Vertices Y
                cube_2.inputs[2].default_value = 2
                # Vertices Z
                cube_2.inputs[3].default_value = 2

                # node Extrude Mesh
                extrude_mesh_1 = gamepad_case_gn.nodes.new("GeometryNodeExtrudeMesh")
                extrude_mesh_1.name = "Extrude Mesh"
                extrude_mesh_1.mode = 'FACES'
                # Offset
                extrude_mesh_1.inputs[2].default_value = (0.0, 0.0, 0.0)
                # Individual
                extrude_mesh_1.inputs[4].default_value = True

                # node Index
                index_1 = gamepad_case_gn.nodes.new("GeometryNodeInputIndex")
                index_1.name = "Index"
                index_1.hide = True

                # node Compare
                compare_1 = gamepad_case_gn.nodes.new("FunctionNodeCompare")
                compare_1.name = "Compare"
                compare_1.hide = True
                compare_1.data_type = 'INT'
                compare_1.mode = 'ELEMENT'
                compare_1.operation = 'EQUAL'
                # B_INT
                compare_1.inputs[3].default_value = 3

                # node Math
                math_3 = gamepad_case_gn.nodes.new("ShaderNodeMath")
                math_3.name = "Math"
                math_3.hide = True
                math_3.operation = 'ADD'
                math_3.use_clamp = False

                # node Compare.001
                compare_001 = gamepad_case_gn.nodes.new("FunctionNodeCompare")
                compare_001.name = "Compare.001"
                compare_001.hide = True
                compare_001.data_type = 'INT'
                compare_001.mode = 'ELEMENT'
                compare_001.operation = 'EQUAL'
                # B_INT
                compare_001.inputs[3].default_value = 1

                # node Set Position
                set_position = gamepad_case_gn.nodes.new("GeometryNodeSetPosition")
                set_position.name = "Set Position"
                # Position
                set_position.inputs[2].default_value = (0.0, 0.0, 0.0)

                # node Extrude Mesh.001
                extrude_mesh_001_1 = gamepad_case_gn.nodes.new("GeometryNodeExtrudeMesh")
                extrude_mesh_001_1.name = "Extrude Mesh.001"
                extrude_mesh_001_1.mode = 'FACES'
                # Offset
                extrude_mesh_001_1.inputs[2].default_value = (0.0, 0.0, 0.0)
                # Individual
                extrude_mesh_001_1.inputs[4].default_value = True

                # node Index.002
                index_002_1 = gamepad_case_gn.nodes.new("GeometryNodeInputIndex")
                index_002_1.name = "Index.002"
                index_002_1.hide = True

                # node Compare.002
                compare_002_1 = gamepad_case_gn.nodes.new("FunctionNodeCompare")
                compare_002_1.name = "Compare.002"
                compare_002_1.hide = True
                compare_002_1.data_type = 'INT'
                compare_002_1.mode = 'ELEMENT'
                compare_002_1.operation = 'EQUAL'
                # B_INT
                compare_002_1.inputs[3].default_value = 10

                # node Math.001
                math_001_2 = gamepad_case_gn.nodes.new("ShaderNodeMath")
                math_001_2.name = "Math.001"
                math_001_2.hide = True
                math_001_2.operation = 'ADD'
                math_001_2.use_clamp = False

                # node Compare.003
                compare_003_1 = gamepad_case_gn.nodes.new("FunctionNodeCompare")
                compare_003_1.name = "Compare.003"
                compare_003_1.hide = True
                compare_003_1.data_type = 'INT'
                compare_003_1.mode = 'ELEMENT'
                compare_003_1.operation = 'EQUAL'
                # B_INT
                compare_003_1.inputs[3].default_value = 9

                # node Combine XYZ
                combine_xyz_4 = gamepad_case_gn.nodes.new("ShaderNodeCombineXYZ")
                combine_xyz_4.name = "Combine XYZ"
                combine_xyz_4.hide = True
                # Y
                combine_xyz_4.inputs[1].default_value = 0.0

                # Set locations
                group_input_8.location = (-743.09033203125, 296.1776123046875)
                group_output_8.location = (948.0509643554688, 602.99462890625)
                cube_2.location = (-548.1709594726562, 365.1602783203125)
                extrude_mesh_1.location = (147.7870330810547, 499.41009521484375)
                index_1.location = (-404.812255859375, 355.3020324707031)
                compare_1.location = (-245.9753875732422, 345.1719970703125)
                math_3.location = (-65.70452880859375, 358.2687072753906)
                compare_001.location = (-244.8542022705078, 307.8743896484375)
                set_position.location = (406.64288330078125, 507.5856628417969)
                extrude_mesh_001_1.location = (650.682373046875, 598.3377685546875)
                index_002_1.location = (92.99666595458984, 586.12890625)
                compare_002_1.location = (273.04266357421875, 583.7130126953125)
                math_001_2.location = (448.8872375488281, 581.0923461914062)
                compare_003_1.location = (273.9136657714844, 540.6406860351562)
                combine_xyz_4.location = (126.16427612304688, 202.8453826904297)

                # Set dimensions
                group_input_8.width, group_input_8.height = 140.0, 100.0
                group_output_8.width, group_output_8.height = 140.0, 100.0
                cube_2.width, cube_2.height = 140.0, 100.0
                extrude_mesh_1.width, extrude_mesh_1.height = 140.0, 100.0
                index_1.width, index_1.height = 140.0, 100.0
                compare_1.width, compare_1.height = 140.0, 100.0
                math_3.width, math_3.height = 140.0, 100.0
                compare_001.width, compare_001.height = 140.0, 100.0
                set_position.width, set_position.height = 140.0, 100.0
                extrude_mesh_001_1.width, extrude_mesh_001_1.height = 140.0, 100.0
                index_002_1.width, index_002_1.height = 140.0, 100.0
                compare_002_1.width, compare_002_1.height = 140.0, 100.0
                math_001_2.width, math_001_2.height = 140.0, 100.0
                compare_003_1.width, compare_003_1.height = 140.0, 100.0
                combine_xyz_4.width, combine_xyz_4.height = 140.0, 100.0

                # initialize gamepad_case_gn links
                # cube_2.Mesh -> extrude_mesh_1.Mesh
                gamepad_case_gn.links.new(cube_2.outputs[0], extrude_mesh_1.inputs[0])
                # index_1.Index -> compare_1.A
                gamepad_case_gn.links.new(index_1.outputs[0], compare_1.inputs[2])
                # math_3.Value -> extrude_mesh_1.Selection
                gamepad_case_gn.links.new(math_3.outputs[0], extrude_mesh_1.inputs[1])
                # compare_1.Result -> math_3.Value
                gamepad_case_gn.links.new(compare_1.outputs[0], math_3.inputs[0])
                # compare_001.Result -> math_3.Value
                gamepad_case_gn.links.new(compare_001.outputs[0], math_3.inputs[1])
                # extrude_mesh_1.Mesh -> set_position.Geometry
                gamepad_case_gn.links.new(extrude_mesh_1.outputs[0], set_position.inputs[0])
                # extrude_mesh_1.Top -> set_position.Selection
                gamepad_case_gn.links.new(extrude_mesh_1.outputs[1], set_position.inputs[1])
                # index_002_1.Index -> compare_002_1.A
                gamepad_case_gn.links.new(index_002_1.outputs[0], compare_002_1.inputs[2])
                # math_001_2.Value -> extrude_mesh_001_1.Selection
                gamepad_case_gn.links.new(math_001_2.outputs[0], extrude_mesh_001_1.inputs[1])
                # compare_002_1.Result -> math_001_2.Value
                gamepad_case_gn.links.new(compare_002_1.outputs[0], math_001_2.inputs[0])
                # compare_003_1.Result -> math_001_2.Value
                gamepad_case_gn.links.new(compare_003_1.outputs[0], math_001_2.inputs[1])
                # set_position.Geometry -> extrude_mesh_001_1.Mesh
                gamepad_case_gn.links.new(set_position.outputs[0], extrude_mesh_001_1.inputs[0])
                # group_input_8.Size -> cube_2.Size
                gamepad_case_gn.links.new(group_input_8.outputs[1], cube_2.inputs[0])
                # group_input_8.Offset Scale -> extrude_mesh_1.Offset Scale
                gamepad_case_gn.links.new(group_input_8.outputs[2], extrude_mesh_1.inputs[3])
                # combine_xyz_4.Vector -> set_position.Offset
                gamepad_case_gn.links.new(combine_xyz_4.outputs[0], set_position.inputs[3])
                # group_input_8.X -> combine_xyz_4.X
                gamepad_case_gn.links.new(group_input_8.outputs[3], combine_xyz_4.inputs[0])
                # group_input_8.Z -> combine_xyz_4.Z
                gamepad_case_gn.links.new(group_input_8.outputs[4], combine_xyz_4.inputs[2])
                # index_1.Index -> compare_001.A
                gamepad_case_gn.links.new(index_1.outputs[0], compare_001.inputs[2])
                # extrude_mesh_001_1.Mesh -> group_output_8.Geometry
                gamepad_case_gn.links.new(extrude_mesh_001_1.outputs[0], group_output_8.inputs[0])
                # index_002_1.Index -> compare_003_1.A
                gamepad_case_gn.links.new(index_002_1.outputs[0], compare_003_1.inputs[2])
                # group_input_8.Offset Scale -> extrude_mesh_001_1.Offset Scale
                gamepad_case_gn.links.new(group_input_8.outputs[5], extrude_mesh_001_1.inputs[3])
                return gamepad_case_gn

        gamepad_case_gn = gamepad_case_gn_node_group()

        # initialize basic_gamepad node group
        def basic_gamepad_node_group():
                basic_gamepad = bpy.data.node_groups.new(type='GeometryNodeTree', name="Basic_Gamepad")

                basic_gamepad.color_tag = 'NONE'
                basic_gamepad.description = ""
                basic_gamepad.default_group_node_width = 140

                # basic_gamepad interface
                # Socket Mesh
                mesh_socket = basic_gamepad.interface.new_socket(name="Mesh", in_out='OUTPUT',
                                                                 socket_type='NodeSocketGeometry')
                mesh_socket.attribute_domain = 'POINT'

                # Socket Square Button
                square_button_socket = basic_gamepad.interface.new_socket(name="Square Button", in_out='INPUT',
                                                                          socket_type='NodeSocketFloat')
                square_button_socket.default_value = 0.5
                square_button_socket.min_value = -10000.0
                square_button_socket.max_value = 10000.0
                square_button_socket.subtype = 'NONE'
                square_button_socket.attribute_domain = 'POINT'

                # Socket Cross Button
                cross_button_socket = basic_gamepad.interface.new_socket(name="Cross Button", in_out='INPUT',
                                                                         socket_type='NodeSocketFloat')
                cross_button_socket.default_value = 0.5
                cross_button_socket.min_value = -10000.0
                cross_button_socket.max_value = 10000.0
                cross_button_socket.subtype = 'NONE'
                cross_button_socket.attribute_domain = 'POINT'

                # Socket Circle Button
                circle_button_socket = basic_gamepad.interface.new_socket(name="Circle Button", in_out='INPUT',
                                                                          socket_type='NodeSocketFloat')
                circle_button_socket.default_value = 0.5
                circle_button_socket.min_value = -10000.0
                circle_button_socket.max_value = 10000.0
                circle_button_socket.subtype = 'NONE'
                circle_button_socket.attribute_domain = 'POINT'

                # Socket Triangle Button
                triangle_button_socket = basic_gamepad.interface.new_socket(name="Triangle Button", in_out='INPUT',
                                                                            socket_type='NodeSocketFloat')
                triangle_button_socket.default_value = 0.5
                triangle_button_socket.min_value = -10000.0
                triangle_button_socket.max_value = 10000.0
                triangle_button_socket.subtype = 'NONE'
                triangle_button_socket.attribute_domain = 'POINT'

                # Socket L1 Button
                l1_button_socket = basic_gamepad.interface.new_socket(name="L1 Button", in_out='INPUT',
                                                                      socket_type='NodeSocketFloat')
                l1_button_socket.default_value = 0.5
                l1_button_socket.min_value = -10000.0
                l1_button_socket.max_value = 10000.0
                l1_button_socket.subtype = 'NONE'
                l1_button_socket.attribute_domain = 'POINT'

                # Socket  R1 Button
                _r1_button_socket = basic_gamepad.interface.new_socket(name=" R1 Button", in_out='INPUT',
                                                                       socket_type='NodeSocketFloat')
                _r1_button_socket.default_value = 0.5
                _r1_button_socket.min_value = -10000.0
                _r1_button_socket.max_value = 10000.0
                _r1_button_socket.subtype = 'NONE'
                _r1_button_socket.attribute_domain = 'POINT'

                # Socket Select Button
                select_button_socket = basic_gamepad.interface.new_socket(name="Select Button", in_out='INPUT',
                                                                          socket_type='NodeSocketFloat')
                select_button_socket.default_value = 0.5
                select_button_socket.min_value = -10000.0
                select_button_socket.max_value = 10000.0
                select_button_socket.subtype = 'NONE'
                select_button_socket.attribute_domain = 'POINT'

                # Socket Start Button
                start_button_socket = basic_gamepad.interface.new_socket(name="Start Button", in_out='INPUT',
                                                                         socket_type='NodeSocketFloat')
                start_button_socket.default_value = 0.5
                start_button_socket.min_value = -10000.0
                start_button_socket.max_value = 10000.0
                start_button_socket.subtype = 'NONE'
                start_button_socket.attribute_domain = 'POINT'

                # Socket L3 Button
                l3_button_socket = basic_gamepad.interface.new_socket(name="L3 Button", in_out='INPUT',
                                                                      socket_type='NodeSocketFloat')
                l3_button_socket.default_value = 0.5
                l3_button_socket.min_value = -10000.0
                l3_button_socket.max_value = 10000.0
                l3_button_socket.subtype = 'NONE'
                l3_button_socket.attribute_domain = 'POINT'

                # Socket R3 Button
                r3_button_socket = basic_gamepad.interface.new_socket(name="R3 Button", in_out='INPUT',
                                                                      socket_type='NodeSocketFloat')
                r3_button_socket.default_value = 0.5
                r3_button_socket.min_value = -10000.0
                r3_button_socket.max_value = 10000.0
                r3_button_socket.subtype = 'NONE'
                r3_button_socket.attribute_domain = 'POINT'

                # Socket L2 Bumper
                l2_bumper_socket = basic_gamepad.interface.new_socket(name="L2 Bumper", in_out='INPUT',
                                                                      socket_type='NodeSocketFloat')
                l2_bumper_socket.default_value = 0.5
                l2_bumper_socket.min_value = -10000.0
                l2_bumper_socket.max_value = 10000.0
                l2_bumper_socket.subtype = 'NONE'
                l2_bumper_socket.attribute_domain = 'POINT'

                # Socket R2 Bumper
                r2_bumper_socket = basic_gamepad.interface.new_socket(name="R2 Bumper", in_out='INPUT',
                                                                      socket_type='NodeSocketFloat')
                r2_bumper_socket.default_value = 0.5
                r2_bumper_socket.min_value = -10000.0
                r2_bumper_socket.max_value = 10000.0
                r2_bumper_socket.subtype = 'NONE'
                r2_bumper_socket.attribute_domain = 'POINT'

                # Socket L3 X_Axis
                l3_x_axis_socket = basic_gamepad.interface.new_socket(name="L3 X_Axis", in_out='INPUT',
                                                                      socket_type='NodeSocketFloat')
                l3_x_axis_socket.default_value = 0.5
                l3_x_axis_socket.min_value = -10000.0
                l3_x_axis_socket.max_value = 10000.0
                l3_x_axis_socket.subtype = 'NONE'
                l3_x_axis_socket.attribute_domain = 'POINT'

                # Socket L3 Y_Axis
                l3_y_axis_socket = basic_gamepad.interface.new_socket(name="L3 Y_Axis", in_out='INPUT',
                                                                      socket_type='NodeSocketFloat')
                l3_y_axis_socket.default_value = 0.5
                l3_y_axis_socket.min_value = -10000.0
                l3_y_axis_socket.max_value = 10000.0
                l3_y_axis_socket.subtype = 'NONE'
                l3_y_axis_socket.attribute_domain = 'POINT'

                # Socket R3 X_Axis
                r3_x_axis_socket = basic_gamepad.interface.new_socket(name="R3 X_Axis", in_out='INPUT',
                                                                      socket_type='NodeSocketFloat')
                r3_x_axis_socket.default_value = 0.5
                r3_x_axis_socket.min_value = -10000.0
                r3_x_axis_socket.max_value = 10000.0
                r3_x_axis_socket.subtype = 'NONE'
                r3_x_axis_socket.attribute_domain = 'POINT'

                # Socket R3 Y_Axis
                r3_y_axis_socket = basic_gamepad.interface.new_socket(name="R3 Y_Axis", in_out='INPUT',
                                                                      socket_type='NodeSocketFloat')
                r3_y_axis_socket.default_value = 0.5
                r3_y_axis_socket.min_value = -10000.0
                r3_y_axis_socket.max_value = 10000.0
                r3_y_axis_socket.subtype = 'NONE'
                r3_y_axis_socket.attribute_domain = 'POINT'

                # Socket D_Pad X
                d_pad_x_socket = basic_gamepad.interface.new_socket(name="D_Pad X", in_out='INPUT',
                                                                    socket_type='NodeSocketFloat')
                d_pad_x_socket.default_value = 0.5
                d_pad_x_socket.min_value = -10000.0
                d_pad_x_socket.max_value = 10000.0
                d_pad_x_socket.subtype = 'NONE'
                d_pad_x_socket.attribute_domain = 'POINT'

                # Socket D_Pad Y
                d_pad_y_socket = basic_gamepad.interface.new_socket(name="D_Pad Y", in_out='INPUT',
                                                                    socket_type='NodeSocketFloat')
                d_pad_y_socket.default_value = 0.5
                d_pad_y_socket.min_value = -10000.0
                d_pad_y_socket.max_value = 10000.0
                d_pad_y_socket.subtype = 'NONE'
                d_pad_y_socket.attribute_domain = 'POINT'

                # initialize basic_gamepad nodes
                # node Group Output
                group_output_9 = basic_gamepad.nodes.new("NodeGroupOutput")
                group_output_9.name = "Group Output"
                group_output_9.is_active_output = True

                # node Group Input
                group_input_9 = basic_gamepad.nodes.new("NodeGroupInput")
                group_input_9.name = "Group Input"

                # node Frame.007
                frame_007 = basic_gamepad.nodes.new("NodeFrame")
                frame_007.label = "Case"
                frame_007.name = "Frame.007"
                frame_007.label_size = 20
                frame_007.shrink = True

                # node Group.001
                group_001_1 = basic_gamepad.nodes.new("GeometryNodeGroup")
                group_001_1.name = "Group.001"
                group_001_1.hide = True
                group_001_1.node_tree = joystick_gn
                # Socket_7
                group_001_1.inputs[1].default_value = 12
                # Socket_8
                group_001_1.inputs[2].default_value = 0.7999999523162842

                # node Group.002
                group_002 = basic_gamepad.nodes.new("GeometryNodeGroup")
                group_002.name = "Group.002"
                group_002.hide = True
                group_002.node_tree = joystick_gn
                # Socket_7
                group_002.inputs[1].default_value = 12
                # Socket_8
                group_002.inputs[2].default_value = 0.7999999523162842

                # node Transform Geometry
                transform_geometry_4 = basic_gamepad.nodes.new("GeometryNodeTransform")
                transform_geometry_4.name = "Transform Geometry"
                transform_geometry_4.hide = True
                transform_geometry_4.mode = 'COMPONENTS'
                # Translation
                transform_geometry_4.inputs[1].default_value = (0.0, -3.299999952316284, 0.0)
                # Rotation
                transform_geometry_4.inputs[2].default_value = (0.0, 0.0, 0.0)
                # Scale
                transform_geometry_4.inputs[3].default_value = (1.0, 1.0, 1.0)

                # node Join Geometry
                join_geometry_1 = basic_gamepad.nodes.new("GeometryNodeJoinGeometry")
                join_geometry_1.name = "Join Geometry"

                # node Set Shade Smooth
                set_shade_smooth = basic_gamepad.nodes.new("GeometryNodeSetShadeSmooth")
                set_shade_smooth.name = "Set Shade Smooth"
                set_shade_smooth.domain = 'FACE'
                # Selection
                set_shade_smooth.inputs[1].default_value = True
                # Shade Smooth
                set_shade_smooth.inputs[2].default_value = False

                # node Set Material
                set_material = basic_gamepad.nodes.new("GeometryNodeSetMaterial")
                set_material.name = "Set Material"
                set_material.hide = True
                # Selection
                set_material.inputs[1].default_value = True
                if "Gamepad_Button_Material" in bpy.data.materials:
                        set_material.inputs[2].default_value = bpy.data.materials["Gamepad_Button_Material"]

                # node Group.004
                group_004 = basic_gamepad.nodes.new("GeometryNodeGroup")
                group_004.name = "Group.004"
                group_004.hide = True
                group_004.node_tree = button_logic_gn
                # Socket_11
                group_004.inputs[2].default_value = (0.0, 0.0, 0.4999999701976776)

                # node Group.005
                group_005 = basic_gamepad.nodes.new("GeometryNodeGroup")
                group_005.name = "Group.005"
                group_005.hide = True
                group_005.node_tree = button_logic_gn
                # Socket_11
                group_005.inputs[2].default_value = (0.0, 0.0, 0.4999999701976776)

                # node Cone
                cone_1 = basic_gamepad.nodes.new("GeometryNodeMeshCone")
                cone_1.name = "Cone"
                cone_1.hide = True
                cone_1.fill_type = 'NGON'
                # Vertices
                cone_1.inputs[0].default_value = 14
                # Side Segments
                cone_1.inputs[1].default_value = 4
                # Fill Segments
                cone_1.inputs[2].default_value = 1
                # Radius Top
                cone_1.inputs[3].default_value = 0.7799999713897705
                # Radius Bottom
                cone_1.inputs[4].default_value = 1.0
                # Depth
                cone_1.inputs[5].default_value = 0.2900000810623169

                # node Group.006
                group_006 = basic_gamepad.nodes.new("GeometryNodeGroup")
                group_006.name = "Group.006"
                group_006.hide = True
                group_006.node_tree = button_logic_gn

                # node Transform Geometry.001
                transform_geometry_001_2 = basic_gamepad.nodes.new("GeometryNodeTransform")
                transform_geometry_001_2.name = "Transform Geometry.001"
                transform_geometry_001_2.hide = True
                transform_geometry_001_2.mode = 'COMPONENTS'
                # Translation
                transform_geometry_001_2.inputs[1].default_value = (2.999999761581421, -5.5, 0.8399999737739563)
                # Rotation
                transform_geometry_001_2.inputs[2].default_value = (0.0, 0.0, 0.0)
                # Scale
                transform_geometry_001_2.inputs[3].default_value = (1.0, 1.0, 1.0)

                # node Group.007
                group_007 = basic_gamepad.nodes.new("GeometryNodeGroup")
                group_007.name = "Group.007"
                group_007.hide = True
                group_007.node_tree = button_logic_gn

                # node Transform Geometry.002
                transform_geometry_002_2 = basic_gamepad.nodes.new("GeometryNodeTransform")
                transform_geometry_002_2.name = "Transform Geometry.002"
                transform_geometry_002_2.hide = True
                transform_geometry_002_2.mode = 'COMPONENTS'
                # Translation
                transform_geometry_002_2.inputs[1].default_value = (7.0, -5.5, 0.8399999737739563)
                # Rotation
                transform_geometry_002_2.inputs[2].default_value = (0.0, 0.0, 0.0)
                # Scale
                transform_geometry_002_2.inputs[3].default_value = (1.0, 1.0, 1.0)

                # node Group.008
                group_008 = basic_gamepad.nodes.new("GeometryNodeGroup")
                group_008.name = "Group.008"
                group_008.hide = True
                group_008.node_tree = button_logic_gn

                # node Transform Geometry.003
                transform_geometry_003_1 = basic_gamepad.nodes.new("GeometryNodeTransform")
                transform_geometry_003_1.name = "Transform Geometry.003"
                transform_geometry_003_1.hide = True
                transform_geometry_003_1.mode = 'COMPONENTS'
                # Translation
                transform_geometry_003_1.inputs[1].default_value = (5.0, -7.0, 0.8399999737739563)
                # Rotation
                transform_geometry_003_1.inputs[2].default_value = (0.0, 0.0, 0.0)
                # Scale
                transform_geometry_003_1.inputs[3].default_value = (1.0, 1.0, 1.0)

                # node Group.009
                group_009 = basic_gamepad.nodes.new("GeometryNodeGroup")
                group_009.name = "Group.009"
                group_009.hide = True
                group_009.node_tree = button_logic_gn

                # node Transform Geometry.004
                transform_geometry_004 = basic_gamepad.nodes.new("GeometryNodeTransform")
                transform_geometry_004.name = "Transform Geometry.004"
                transform_geometry_004.hide = True
                transform_geometry_004.mode = 'COMPONENTS'
                # Translation
                transform_geometry_004.inputs[1].default_value = (5.0, -4.0, 0.8399999737739563)
                # Rotation
                transform_geometry_004.inputs[2].default_value = (0.0, 0.0, 0.0)
                # Scale
                transform_geometry_004.inputs[3].default_value = (1.0, 1.0, 1.0)

                # node Join Geometry.001
                join_geometry_001_1 = basic_gamepad.nodes.new("GeometryNodeJoinGeometry")
                join_geometry_001_1.name = "Join Geometry.001"
                join_geometry_001_1.hide = True

                # node Transform Geometry.005
                transform_geometry_005 = basic_gamepad.nodes.new("GeometryNodeTransform")
                transform_geometry_005.name = "Transform Geometry.005"
                transform_geometry_005.hide = True
                transform_geometry_005.mode = 'COMPONENTS'
                # Translation
                transform_geometry_005.inputs[1].default_value = (-1.5499999523162842, -1.5999999046325684,
                                                                  0.09999999403953552)
                # Rotation
                transform_geometry_005.inputs[2].default_value = (-0.22340214252471924, 0.0, 0.0)
                # Scale
                transform_geometry_005.inputs[3].default_value = (0.3499999940395355, 0.3499999940395355,
                                                                  0.800000011920929)

                # node Group.010
                group_010 = basic_gamepad.nodes.new("GeometryNodeGroup")
                group_010.name = "Group.010"
                group_010.hide = True
                group_010.node_tree = d_pad_gn
                # Socket_2
                group_010.inputs[1].default_value = 0.12999996542930603
                # Socket_3
                group_010.inputs[2].default_value = 1
                # Socket_4
                group_010.inputs[3].default_value = 0

                # node Transform Geometry.007
                transform_geometry_007 = basic_gamepad.nodes.new("GeometryNodeTransform")
                transform_geometry_007.name = "Transform Geometry.007"
                transform_geometry_007.hide = True
                transform_geometry_007.mode = 'COMPONENTS'
                # Translation
                transform_geometry_007.inputs[1].default_value = (4.499999523162842, 0.9999996423721313,
                                                                  -0.7599999308586121)
                # Rotation
                transform_geometry_007.inputs[2].default_value = (0.0, 0.0, 0.0)
                # Scale
                transform_geometry_007.inputs[3].default_value = (0.20000004768371582, 0.5000000596046448, 1.0)

                # node Group.013
                group_013 = basic_gamepad.nodes.new("GeometryNodeGroup")
                group_013.name = "Group.013"
                group_013.hide = True
                group_013.node_tree = axis_1d_gn
                # Socket_3
                group_013.inputs[2].default_value = -0.30000001192092896
                # Socket_4
                group_013.inputs[3].default_value = False

                # node Transform Geometry.008
                transform_geometry_008 = basic_gamepad.nodes.new("GeometryNodeTransform")
                transform_geometry_008.name = "Transform Geometry.008"
                transform_geometry_008.hide = True
                transform_geometry_008.mode = 'COMPONENTS'
                # Translation
                transform_geometry_008.inputs[1].default_value = (4.499999523162842, -5.0, -0.7599999308586121)
                # Rotation
                transform_geometry_008.inputs[2].default_value = (0.0, 0.0, 0.0)
                # Scale
                transform_geometry_008.inputs[3].default_value = (0.20000004768371582, 0.5000000596046448, 1.0)

                # node Group.015
                group_015 = basic_gamepad.nodes.new("GeometryNodeGroup")
                group_015.name = "Group.015"
                group_015.hide = True
                group_015.node_tree = axis_1d_gn
                # Socket_3
                group_015.inputs[2].default_value = -0.30000001192092896
                # Socket_4
                group_015.inputs[3].default_value = False

                # node Set Position
                set_position_1 = basic_gamepad.nodes.new("GeometryNodeSetPosition")
                set_position_1.name = "Set Position"
                set_position_1.hide = True
                # Selection
                set_position_1.inputs[1].default_value = True
                # Position
                set_position_1.inputs[2].default_value = (0.0, 0.0, 0.0)
                # Offset
                set_position_1.inputs[3].default_value = (0.0, 0.9999998807907104, 0.0)

                # node Group.016
                group_016 = basic_gamepad.nodes.new("GeometryNodeGroup")
                group_016.name = "Group.016"
                group_016.hide = True
                group_016.node_tree = axis_2d_gn
                # Socket_4
                group_016.inputs[3].default_value = 0.2999999225139618
                # Socket_5
                group_016.inputs[4].default_value = -0.30000007152557373

                # node Group.017
                group_017 = basic_gamepad.nodes.new("GeometryNodeGroup")
                group_017.name = "Group.017"
                group_017.hide = True
                group_017.node_tree = axis_2d_gn
                # Socket_4
                group_017.inputs[3].default_value = 0.2999999523162842
                # Socket_5
                group_017.inputs[4].default_value = -0.30000007152557373

                # node Group.018
                group_018 = basic_gamepad.nodes.new("GeometryNodeGroup")
                group_018.name = "Group.018"
                group_018.node_tree = d_pad_logic_gn
                # Socket_4
                group_018.inputs[3].default_value = 0.009999999776482582
                # Socket_5
                group_018.inputs[4].default_value = 0.009999999776482582

                # node Group.019
                group_019 = basic_gamepad.nodes.new("GeometryNodeGroup")
                group_019.name = "Group.019"
                group_019.hide = True
                group_019.node_tree = button_logic_gn
                # Socket_11
                group_019.inputs[2].default_value = (0.0, 0.0, 0.9999999403953552)

                # node Transform Geometry.006
                transform_geometry_006_1 = basic_gamepad.nodes.new("GeometryNodeTransform")
                transform_geometry_006_1.name = "Transform Geometry.006"
                transform_geometry_006_1.hide = True
                transform_geometry_006_1.mode = 'COMPONENTS'
                # Translation
                transform_geometry_006_1.inputs[1].default_value = (2.999999761581421, -0.8000003099441528,
                                                                    0.8399999737739563)
                # Rotation
                transform_geometry_006_1.inputs[2].default_value = (0.0, 0.0, 0.0)
                # Scale
                transform_geometry_006_1.inputs[3].default_value = (1.0, 1.0, 1.0)

                # node Join Geometry.002
                join_geometry_002 = basic_gamepad.nodes.new("GeometryNodeJoinGeometry")
                join_geometry_002.name = "Join Geometry.002"
                join_geometry_002.hide = True

                # node Group.020
                group_020 = basic_gamepad.nodes.new("GeometryNodeGroup")
                group_020.name = "Group.020"
                group_020.hide = True
                group_020.node_tree = button_logic_gn
                # Socket_11
                group_020.inputs[2].default_value = (0.0, 0.0, 0.9999998807907104)

                # node Transform Geometry.009
                transform_geometry_009 = basic_gamepad.nodes.new("GeometryNodeTransform")
                transform_geometry_009.name = "Transform Geometry.009"
                transform_geometry_009.hide = True
                transform_geometry_009.mode = 'COMPONENTS'
                # Translation
                transform_geometry_009.inputs[1].default_value = (2.999999761581421, -4.099999904632568,
                                                                  0.8399999737739563)
                # Rotation
                transform_geometry_009.inputs[2].default_value = (0.0, 0.0, 0.0)
                # Scale
                transform_geometry_009.inputs[3].default_value = (1.0, 1.0, 1.0)

                # node Group.021
                group_021 = basic_gamepad.nodes.new("GeometryNodeGroup")
                group_021.name = "Group.021"
                group_021.hide = True
                group_021.node_tree = start_select_button_gn

                # node Transform Geometry.010
                transform_geometry_010 = basic_gamepad.nodes.new("GeometryNodeTransform")
                transform_geometry_010.name = "Transform Geometry.010"
                transform_geometry_010.hide = True
                transform_geometry_010.mode = 'COMPONENTS'
                # Translation
                transform_geometry_010.inputs[1].default_value = (-1.2999999523162842, 1.5, 0.08999989926815033)
                # Rotation
                transform_geometry_010.inputs[2].default_value = (0.0, 0.0, 0.0)
                # Scale
                transform_geometry_010.inputs[3].default_value = (0.5899999737739563, 0.6100000143051147, 1.0)

                # node Group.022
                group_022 = basic_gamepad.nodes.new("GeometryNodeGroup")
                group_022.name = "Group.022"
                group_022.hide = True
                group_022.node_tree = button_logic_gn
                # Socket_11
                group_022.inputs[2].default_value = (0.4999999701976776, 0.0, 0.0)

                # node Transform Geometry.011
                transform_geometry_011 = basic_gamepad.nodes.new("GeometryNodeTransform")
                transform_geometry_011.name = "Transform Geometry.011"
                transform_geometry_011.hide = True
                transform_geometry_011.mode = 'COMPONENTS'
                # Translation
                transform_geometry_011.inputs[1].default_value = (2.999999761581421, -0.8000003099441528,
                                                                  0.8399999737739563)
                # Rotation
                transform_geometry_011.inputs[2].default_value = (0.10471975058317184, 0.0, 0.19198621809482574)
                # Scale
                transform_geometry_011.inputs[3].default_value = (1.0, 1.0, 1.0)

                # node Join Geometry.003
                join_geometry_003 = basic_gamepad.nodes.new("GeometryNodeJoinGeometry")
                join_geometry_003.name = "Join Geometry.003"
                join_geometry_003.hide = True

                # node Group.023
                group_023 = basic_gamepad.nodes.new("GeometryNodeGroup")
                group_023.name = "Group.023"
                group_023.hide = True
                group_023.node_tree = button_logic_gn
                # Socket_11
                group_023.inputs[2].default_value = (0.4999999701976776, 0.0, 0.0)

                # node Transform Geometry.012
                transform_geometry_012 = basic_gamepad.nodes.new("GeometryNodeTransform")
                transform_geometry_012.name = "Transform Geometry.012"
                transform_geometry_012.hide = True
                transform_geometry_012.mode = 'COMPONENTS'
                # Translation
                transform_geometry_012.inputs[1].default_value = (2.999999761581421, -11.19999885559082,
                                                                  0.8399999737739563)
                # Rotation
                transform_geometry_012.inputs[2].default_value = (-0.10471975803375244, 0.0, -0.19198620319366455)
                # Scale
                transform_geometry_012.inputs[3].default_value = (1.0, 1.0, 1.0)

                # node Transform Geometry.013
                transform_geometry_013 = basic_gamepad.nodes.new("GeometryNodeTransform")
                transform_geometry_013.name = "Transform Geometry.013"
                transform_geometry_013.hide = True
                transform_geometry_013.mode = 'COMPONENTS'
                # Translation
                transform_geometry_013.inputs[1].default_value = (-0.600000262260437, 4.199999809265137,
                                                                  -0.030000030994415283)
                # Rotation
                transform_geometry_013.inputs[2].default_value = (0.0, 0.0, 0.0)
                # Scale
                transform_geometry_013.inputs[3].default_value = (0.699999988079071, 0.699999988079071, 1.0)

                # node Cube
                cube_3 = basic_gamepad.nodes.new("GeometryNodeMeshCube")
                cube_3.name = "Cube"
                cube_3.hide = True
                # Size
                cube_3.inputs[0].default_value = (0.30000007152557373, 2.1999998092651367, 0.6000000238418579)
                # Vertices X
                cube_3.inputs[1].default_value = 2
                # Vertices Y
                cube_3.inputs[2].default_value = 2
                # Vertices Z
                cube_3.inputs[3].default_value = 2

                # node Join Geometry.004
                join_geometry_004 = basic_gamepad.nodes.new("GeometryNodeJoinGeometry")
                join_geometry_004.name = "Join Geometry.004"
                join_geometry_004.hide = True

                # node Transform Geometry.014
                transform_geometry_014 = basic_gamepad.nodes.new("GeometryNodeTransform")
                transform_geometry_014.name = "Transform Geometry.014"
                transform_geometry_014.hide = True
                transform_geometry_014.mode = 'COMPONENTS'
                # Translation
                transform_geometry_014.inputs[1].default_value = (-2.799999952316284, 2.1999998092651367,
                                                                  0.4999999701976776)
                # Rotation
                transform_geometry_014.inputs[2].default_value = (0.0, 0.0, 0.0)
                # Scale
                transform_geometry_014.inputs[3].default_value = (1.0, 1.0, 1.0)

                # node Group.024
                group_024 = basic_gamepad.nodes.new("GeometryNodeGroup")
                group_024.name = "Group.024"
                group_024.node_tree = gamepad_case_gn
                # Socket_2
                group_024.inputs[1].default_value = (3.3500001430511475, 4.5, 1.8999998569488525)
                # Socket_3
                group_024.inputs[2].default_value = 2.059999942779541
                # Socket_4
                group_024.inputs[3].default_value = -0.3999999761581421
                # Socket_5
                group_024.inputs[4].default_value = 0.4999999701976776
                # Socket_6
                group_024.inputs[5].default_value = 1.859999656677246

                # node Join Geometry.005
                join_geometry_005 = basic_gamepad.nodes.new("GeometryNodeJoinGeometry")
                join_geometry_005.name = "Join Geometry.005"

                # node Join Geometry.006
                join_geometry_006 = basic_gamepad.nodes.new("GeometryNodeJoinGeometry")
                join_geometry_006.name = "Join Geometry.006"
                join_geometry_006.hide = True

                # node Transform Geometry.015
                transform_geometry_015 = basic_gamepad.nodes.new("GeometryNodeTransform")
                transform_geometry_015.name = "Transform Geometry.015"
                transform_geometry_015.hide = True
                transform_geometry_015.mode = 'COMPONENTS'
                # Translation
                transform_geometry_015.inputs[1].default_value = (-0.5999999642372131, 1.4999998807907104,
                                                                  0.19999998807907104)
                # Rotation
                transform_geometry_015.inputs[2].default_value = (0.0, 0.0, 0.0)
                # Scale
                transform_geometry_015.inputs[3].default_value = (1.0, 1.0, 1.0)

                # node Frame.001
                frame_001 = basic_gamepad.nodes.new("NodeFrame")
                frame_001.label = "Top Shoulder"
                frame_001.name = "Frame.001"
                frame_001.label_size = 20
                frame_001.shrink = True

                # node Frame.002
                frame_002 = basic_gamepad.nodes.new("NodeFrame")
                frame_002.label = "Select Start"
                frame_002.name = "Frame.002"
                frame_002.label_size = 20
                frame_002.shrink = True

                # node Frame.003
                frame_003 = basic_gamepad.nodes.new("NodeFrame")
                frame_003.label = "Joysticks"
                frame_003.name = "Frame.003"
                frame_003.label_size = 20
                frame_003.shrink = True

                # node Frame.004
                frame_004 = basic_gamepad.nodes.new("NodeFrame")
                frame_004.label = "D-Pad"
                frame_004.name = "Frame.004"
                frame_004.label_size = 20
                frame_004.shrink = True

                # node Frame.005
                frame_005 = basic_gamepad.nodes.new("NodeFrame")
                frame_005.label = "Main Buttons"
                frame_005.name = "Frame.005"
                frame_005.label_size = 20
                frame_005.shrink = True

                # node Transform Geometry.016
                transform_geometry_016 = basic_gamepad.nodes.new("GeometryNodeTransform")
                transform_geometry_016.name = "Transform Geometry.016"
                transform_geometry_016.hide = True
                transform_geometry_016.mode = 'COMPONENTS'
                # Translation
                transform_geometry_016.inputs[1].default_value = (-1.5999999046325684, 2.799999713897705,
                                                                  -3.18999981880188)
                # Rotation
                transform_geometry_016.inputs[2].default_value = (0.20525071024894714, 0.0, 0.0)
                # Scale
                transform_geometry_016.inputs[3].default_value = (0.6100000143051147, 0.6100000143051147,
                                                                  4.199999809265137)

                # node Frame.006
                frame_006 = basic_gamepad.nodes.new("NodeFrame")
                frame_006.label = "Shoulder Down"
                frame_006.name = "Frame.006"
                frame_006.label_size = 20
                frame_006.shrink = True

                # node Subdivide Mesh
                subdivide_mesh_1 = basic_gamepad.nodes.new("GeometryNodeSubdivideMesh")
                subdivide_mesh_1.name = "Subdivide Mesh"
                # Level
                subdivide_mesh_1.inputs[1].default_value = 0

                # node Set Material.001
                set_material_001 = basic_gamepad.nodes.new("GeometryNodeSetMaterial")
                set_material_001.name = "Set Material.001"
                # Selection
                set_material_001.inputs[1].default_value = True
                if "Gamepad_Case_Material" in bpy.data.materials:
                        set_material_001.inputs[2].default_value = bpy.data.materials["Gamepad_Case_Material"]

                # node Vector
                vector = basic_gamepad.nodes.new("FunctionNodeInputVector")
                vector.label = "Push Intensity"
                vector.name = "Vector"
                vector.hide = True
                vector.vector = (0.0, 0.0, 1.5)

                # node Subdivide Mesh.001
                subdivide_mesh_001 = basic_gamepad.nodes.new("GeometryNodeSubdivideMesh")
                subdivide_mesh_001.name = "Subdivide Mesh.001"
                # Level
                subdivide_mesh_001.inputs[1].default_value = 3

                # node Subdivision Surface
                subdivision_surface = basic_gamepad.nodes.new("GeometryNodeSubdivisionSurface")
                subdivision_surface.name = "Subdivision Surface"
                subdivision_surface.boundary_smooth = 'ALL'
                subdivision_surface.uv_smooth = 'PRESERVE_BOUNDARIES'
                # Level
                subdivision_surface.inputs[1].default_value = 1
                # Edge Crease
                subdivision_surface.inputs[2].default_value = 0.0
                # Vertex Crease
                subdivision_surface.inputs[3].default_value = 0.0
                # Limit Surface
                subdivision_surface.inputs[4].default_value = True

                # Set parents
                group_001_1.parent = frame_003
                group_002.parent = frame_003
                transform_geometry_4.parent = frame_003
                group_004.parent = frame_003
                group_005.parent = frame_003
                cone_1.parent = frame_005
                group_006.parent = frame_005
                transform_geometry_001_2.parent = frame_005
                group_007.parent = frame_005
                transform_geometry_002_2.parent = frame_005
                group_008.parent = frame_005
                transform_geometry_003_1.parent = frame_005
                group_009.parent = frame_005
                transform_geometry_004.parent = frame_005
                join_geometry_001_1.parent = frame_005
                transform_geometry_005.parent = frame_005
                group_010.parent = frame_004
                transform_geometry_007.parent = frame_006
                group_013.parent = frame_006
                transform_geometry_008.parent = frame_006
                group_015.parent = frame_006
                set_position_1.parent = frame_004
                group_016.parent = frame_003
                group_017.parent = frame_003
                group_018.parent = frame_004
                group_019.parent = frame_002
                transform_geometry_006_1.parent = frame_002
                join_geometry_002.parent = frame_002
                group_020.parent = frame_002
                transform_geometry_009.parent = frame_002
                group_021.parent = frame_002
                transform_geometry_010.parent = frame_002
                group_022.parent = frame_001
                transform_geometry_011.parent = frame_001
                join_geometry_003.parent = frame_001
                group_023.parent = frame_001
                transform_geometry_012.parent = frame_001
                transform_geometry_013.parent = frame_001
                cube_3.parent = frame_001
                join_geometry_004.parent = frame_006
                transform_geometry_014.parent = frame_006
                group_024.parent = frame_007
                join_geometry_006.parent = frame_003
                transform_geometry_015.parent = frame_003
                transform_geometry_016.parent = frame_004
                set_material_001.parent = frame_007
                vector.parent = frame_005
                subdivide_mesh_001.parent = frame_007
                subdivision_surface.parent = frame_007

                # Set locations
                group_output_9.location = (2453.234130859375, 336.42669677734375)
                group_input_9.location = (-1148.1995849609375, 764.806884765625)
                frame_007.location = (815.0, -181.0)
                group_001_1.location = (32.870147705078125, -94.96408081054688)
                group_002.location = (29.668609619140625, -153.84573364257812)
                transform_geometry_4.location = (615.4302978515625, -228.00885009765625)
                join_geometry_1.location = (1267.8240966796875, 263.46392822265625)
                set_shade_smooth.location = (2012.9913330078125, 314.8740234375)
                set_material.location = (1497.1663818359375, 229.35906982421875)
                group_004.location = (403.99810791015625, -44.916290283203125)
                group_005.location = (405.11944580078125, -74.17141723632812)
                cone_1.location = (72.73434448242188, -54.8897705078125)
                group_006.location = (313.8408508300781, -103.35693359375)
                transform_geometry_001_2.location = (510.4046630859375, -110.80126953125)
                group_007.location = (312.08209228515625, -196.732177734375)
                transform_geometry_002_2.location = (518.7489013671875, -206.230712890625)
                group_008.location = (330.1180419921875, -150.2503662109375)
                transform_geometry_003_1.location = (526.728515625, -164.477783203125)
                group_009.location = (297.91143798828125, -56.4739990234375)
                transform_geometry_004.location = (539.96923828125, -64.95458984375)
                join_geometry_001_1.location = (780.0707397460938, -222.3817138671875)
                transform_geometry_005.location = (970.937255859375, -234.6827392578125)
                group_010.location = (29.763702392578125, -44.91435623168945)
                transform_geometry_007.location = (209.8976287841797, -65.143798828125)
                group_013.location = (29.897552490234375, -45.143798828125)
                transform_geometry_008.location = (213.1587677001953, -114.6273193359375)
                group_015.location = (33.15869140625, -94.62744140625)
                set_position_1.location = (226.92990112304688, -62.98117446899414)
                group_016.location = (214.28311157226562, -105.93081665039062)
                group_017.location = (211.44046020507812, -174.97909545898438)
                group_018.location = (416.4246520996094, -78.29653930664062)
                group_019.location = (366.33074951171875, -54.43304443359375)
                transform_geometry_006_1.location = (583.501708984375, -68.2291259765625)
                join_geometry_002.location = (824.5194091796875, -68.5579833984375)
                group_020.location = (360.2851867675781, -113.75494384765625)
                transform_geometry_009.location = (586.2691040039062, -131.08404541015625)
                group_021.location = (30.0487060546875, -45.24298095703125)
                transform_geometry_010.location = (1004.3412475585938, -114.43359375)
                group_022.location = (371.4463195800781, -74.64727783203125)
                transform_geometry_011.location = (588.6173706054688, -88.44329833984375)
                join_geometry_003.location = (829.6351928710938, -88.77215576171875)
                group_023.location = (365.4006652832031, -133.96917724609375)
                transform_geometry_012.location = (582.5717163085938, -147.76519775390625)
                transform_geometry_013.location = (1009.4566040039062, -134.64776611328125)
                cube_3.location = (29.6588134765625, -44.88885498046875)
                join_geometry_004.location = (433.15869140625, -114.6273193359375)
                transform_geometry_014.location = (633.15966796875, -114.6273193359375)
                group_024.location = (30.05670166015625, -40.03900146484375)
                join_geometry_005.location = (1756.6243896484375, 271.8934326171875)
                join_geometry_006.location = (792.7122802734375, -187.36575317382812)
                transform_geometry_015.location = (983.0201416015625, -200.70932006835938)
                frame_001.location = (-349.0, 1002.0)
                frame_002.location = (-347.0, 752.0)
                frame_003.location = (-340.0, 319.0)
                frame_004.location = (-341.0, 3.0)
                frame_005.location = (-328.0, 1317.0)
                transform_geometry_016.location = (611.91552734375, -82.84461975097656)
                frame_006.location = (-216.0, 514.0)
                subdivide_mesh_1.location = (2222.36865234375, 338.8022155761719)
                set_material_001.location = (643.0771484375, -51.17120361328125)
                vector.location = (30.39007568359375, -143.8323974609375)
                subdivide_mesh_001.location = (238.82568359375, -47.17242431640625)
                subdivision_surface.location = (433.184326171875, -47.78106689453125)

                # Set dimensions
                group_output_9.width, group_output_9.height = 140.0, 100.0
                group_input_9.width, group_input_9.height = 140.0, 100.0
                frame_007.width, frame_007.height = 813.0, 338.0
                group_001_1.width, group_001_1.height = 140.0, 100.0
                group_002.width, group_002.height = 140.0, 100.0
                transform_geometry_4.width, transform_geometry_4.height = 140.0, 100.0
                join_geometry_1.width, join_geometry_1.height = 140.0, 100.0
                set_shade_smooth.width, set_shade_smooth.height = 140.0, 100.0
                set_material.width, set_material.height = 140.0, 100.0
                group_004.width, group_004.height = 140.0, 100.0
                group_005.width, group_005.height = 140.0, 100.0
                cone_1.width, cone_1.height = 140.0, 100.0
                group_006.width, group_006.height = 140.0, 100.0
                transform_geometry_001_2.width, transform_geometry_001_2.height = 140.0, 100.0
                group_007.width, group_007.height = 140.0, 100.0
                transform_geometry_002_2.width, transform_geometry_002_2.height = 140.0, 100.0
                group_008.width, group_008.height = 140.0, 100.0
                transform_geometry_003_1.width, transform_geometry_003_1.height = 140.0, 100.0
                group_009.width, group_009.height = 140.0, 100.0
                transform_geometry_004.width, transform_geometry_004.height = 140.0, 100.0
                join_geometry_001_1.width, join_geometry_001_1.height = 140.0, 100.0
                transform_geometry_005.width, transform_geometry_005.height = 140.0, 100.0
                group_010.width, group_010.height = 140.0, 100.0
                transform_geometry_007.width, transform_geometry_007.height = 140.0, 100.0
                group_013.width, group_013.height = 140.0, 100.0
                transform_geometry_008.width, transform_geometry_008.height = 140.0, 100.0
                group_015.width, group_015.height = 140.0, 100.0
                set_position_1.width, set_position_1.height = 140.0, 100.0
                group_016.width, group_016.height = 140.0, 100.0
                group_017.width, group_017.height = 140.0, 100.0
                group_018.width, group_018.height = 140.0, 100.0
                group_019.width, group_019.height = 140.0, 100.0
                transform_geometry_006_1.width, transform_geometry_006_1.height = 140.0, 100.0
                join_geometry_002.width, join_geometry_002.height = 140.0, 100.0
                group_020.width, group_020.height = 140.0, 100.0
                transform_geometry_009.width, transform_geometry_009.height = 140.0, 100.0
                group_021.width, group_021.height = 140.0, 100.0
                transform_geometry_010.width, transform_geometry_010.height = 140.0, 100.0
                group_022.width, group_022.height = 140.0, 100.0
                transform_geometry_011.width, transform_geometry_011.height = 140.0, 100.0
                join_geometry_003.width, join_geometry_003.height = 140.0, 100.0
                group_023.width, group_023.height = 140.0, 100.0
                transform_geometry_012.width, transform_geometry_012.height = 140.0, 100.0
                transform_geometry_013.width, transform_geometry_013.height = 140.0, 100.0
                cube_3.width, cube_3.height = 140.0, 100.0
                join_geometry_004.width, join_geometry_004.height = 140.0, 100.0
                transform_geometry_014.width, transform_geometry_014.height = 140.0, 100.0
                group_024.width, group_024.height = 140.0, 100.0
                join_geometry_005.width, join_geometry_005.height = 140.0, 100.0
                join_geometry_006.width, join_geometry_006.height = 140.0, 100.0
                transform_geometry_015.width, transform_geometry_015.height = 140.0, 100.0
                frame_001.width, frame_001.height = 1179.0, 203.0
                frame_002.width, frame_002.height = 1174.0, 186.0
                frame_003.width, frame_003.height = 1153.0, 283.0
                frame_004.width, frame_004.height = 782.0, 292.0
                frame_005.width, frame_005.height = 1141.0, 290.0
                transform_geometry_016.width, transform_geometry_016.height = 140.0, 100.0
                frame_006.width, frame_006.height = 803.0, 170.0
                subdivide_mesh_1.width, subdivide_mesh_1.height = 140.0, 100.0
                set_material_001.width, set_material_001.height = 140.0, 100.0
                vector.width, vector.height = 140.0, 100.0
                subdivide_mesh_001.width, subdivide_mesh_001.height = 140.0, 100.0
                subdivision_surface.width, subdivision_surface.height = 150.0, 100.0

                # initialize basic_gamepad links
                # set_shade_smooth.Geometry -> subdivide_mesh_1.Mesh
                basic_gamepad.links.new(set_shade_smooth.outputs[0], subdivide_mesh_1.inputs[0])
                # group_022.Geometry -> transform_geometry_011.Geometry
                basic_gamepad.links.new(group_022.outputs[0], transform_geometry_011.inputs[0])
                # group_024.Geometry -> subdivide_mesh_001.Mesh
                basic_gamepad.links.new(group_024.outputs[0], subdivide_mesh_001.inputs[0])
                # group_007.Geometry -> transform_geometry_002_2.Geometry
                basic_gamepad.links.new(group_007.outputs[0], transform_geometry_002_2.inputs[0])
                # vector.Vector -> group_008.Push Vector
                basic_gamepad.links.new(vector.outputs[0], group_008.inputs[2])
                # cone_1.Mesh -> group_007.Geometry
                basic_gamepad.links.new(cone_1.outputs[0], group_007.inputs[0])
                # group_005.Geometry -> transform_geometry_4.Geometry
                basic_gamepad.links.new(group_005.outputs[0], transform_geometry_4.inputs[0])
                # group_010.Geometry -> set_position_1.Geometry
                basic_gamepad.links.new(group_010.outputs[0], set_position_1.inputs[0])
                # group_008.Geometry -> transform_geometry_003_1.Geometry
                basic_gamepad.links.new(group_008.outputs[0], transform_geometry_003_1.inputs[0])
                # join_geometry_1.Geometry -> set_material.Geometry
                basic_gamepad.links.new(join_geometry_1.outputs[0], set_material.inputs[0])
                # transform_geometry_012.Geometry -> join_geometry_003.Geometry
                basic_gamepad.links.new(transform_geometry_012.outputs[0], join_geometry_003.inputs[0])
                # group_001_1.Geometry -> group_016.Geometry
                basic_gamepad.links.new(group_001_1.outputs[0], group_016.inputs[0])
                # join_geometry_003.Geometry -> transform_geometry_013.Geometry
                basic_gamepad.links.new(join_geometry_003.outputs[0], transform_geometry_013.inputs[0])
                # group_002.Geometry -> group_017.Geometry
                basic_gamepad.links.new(group_002.outputs[0], group_017.inputs[0])
                # vector.Vector -> group_009.Push Vector
                basic_gamepad.links.new(vector.outputs[0], group_009.inputs[2])
                # cone_1.Mesh -> group_008.Geometry
                basic_gamepad.links.new(cone_1.outputs[0], group_008.inputs[0])
                # cone_1.Mesh -> group_009.Geometry
                basic_gamepad.links.new(cone_1.outputs[0], group_009.inputs[0])
                # group_009.Geometry -> transform_geometry_004.Geometry
                basic_gamepad.links.new(group_009.outputs[0], transform_geometry_004.inputs[0])
                # cube_3.Mesh -> group_022.Geometry
                basic_gamepad.links.new(cube_3.outputs[0], group_022.inputs[0])
                # cube_3.Mesh -> group_023.Geometry
                basic_gamepad.links.new(cube_3.outputs[0], group_023.inputs[0])
                # group_006.Geometry -> transform_geometry_001_2.Geometry
                basic_gamepad.links.new(group_006.outputs[0], transform_geometry_001_2.inputs[0])
                # transform_geometry_008.Geometry -> join_geometry_004.Geometry
                basic_gamepad.links.new(transform_geometry_008.outputs[0], join_geometry_004.inputs[0])
                # set_position_1.Geometry -> group_018.Geometry
                basic_gamepad.links.new(set_position_1.outputs[0], group_018.inputs[0])
                # transform_geometry_001_2.Geometry -> join_geometry_001_1.Geometry
                basic_gamepad.links.new(transform_geometry_001_2.outputs[0], join_geometry_001_1.inputs[0])
                # join_geometry_004.Geometry -> transform_geometry_014.Geometry
                basic_gamepad.links.new(join_geometry_004.outputs[0], transform_geometry_014.inputs[0])
                # join_geometry_001_1.Geometry -> transform_geometry_005.Geometry
                basic_gamepad.links.new(join_geometry_001_1.outputs[0], transform_geometry_005.inputs[0])
                # group_019.Geometry -> transform_geometry_006_1.Geometry
                basic_gamepad.links.new(group_019.outputs[0], transform_geometry_006_1.inputs[0])
                # group_013.Geometry -> transform_geometry_007.Geometry
                basic_gamepad.links.new(group_013.outputs[0], transform_geometry_007.inputs[0])
                # subdivision_surface.Mesh -> set_material_001.Geometry
                basic_gamepad.links.new(subdivision_surface.outputs[0], set_material_001.inputs[0])
                # set_material_001.Geometry -> join_geometry_005.Geometry
                basic_gamepad.links.new(set_material_001.outputs[0], join_geometry_005.inputs[0])
                # group_020.Geometry -> transform_geometry_009.Geometry
                basic_gamepad.links.new(group_020.outputs[0], transform_geometry_009.inputs[0])
                # group_015.Geometry -> transform_geometry_008.Geometry
                basic_gamepad.links.new(group_015.outputs[0], transform_geometry_008.inputs[0])
                # transform_geometry_009.Geometry -> join_geometry_002.Geometry
                basic_gamepad.links.new(transform_geometry_009.outputs[0], join_geometry_002.inputs[0])
                # transform_geometry_4.Geometry -> join_geometry_006.Geometry
                basic_gamepad.links.new(transform_geometry_4.outputs[0], join_geometry_006.inputs[0])
                # group_021.Geometry -> group_019.Geometry
                basic_gamepad.links.new(group_021.outputs[0], group_019.inputs[0])
                # subdivide_mesh_001.Mesh -> subdivision_surface.Mesh
                basic_gamepad.links.new(subdivide_mesh_001.outputs[0], subdivision_surface.inputs[0])
                # group_016.Geometry -> group_004.Geometry
                basic_gamepad.links.new(group_016.outputs[0], group_004.inputs[0])
                # group_021.Geometry -> group_020.Geometry
                basic_gamepad.links.new(group_021.outputs[0], group_020.inputs[0])
                # transform_geometry_016.Geometry -> join_geometry_1.Geometry
                basic_gamepad.links.new(transform_geometry_016.outputs[0], join_geometry_1.inputs[0])
                # group_017.Geometry -> group_005.Geometry
                basic_gamepad.links.new(group_017.outputs[0], group_005.inputs[0])
                # join_geometry_002.Geometry -> transform_geometry_010.Geometry
                basic_gamepad.links.new(join_geometry_002.outputs[0], transform_geometry_010.inputs[0])
                # join_geometry_005.Geometry -> set_shade_smooth.Geometry
                basic_gamepad.links.new(join_geometry_005.outputs[0], set_shade_smooth.inputs[0])
                # vector.Vector -> group_007.Push Vector
                basic_gamepad.links.new(vector.outputs[0], group_007.inputs[2])
                # group_018.Geometry -> transform_geometry_016.Geometry
                basic_gamepad.links.new(group_018.outputs[0], transform_geometry_016.inputs[0])
                # group_023.Geometry -> transform_geometry_012.Geometry
                basic_gamepad.links.new(group_023.outputs[0], transform_geometry_012.inputs[0])
                # join_geometry_006.Geometry -> transform_geometry_015.Geometry
                basic_gamepad.links.new(join_geometry_006.outputs[0], transform_geometry_015.inputs[0])
                # vector.Vector -> group_006.Push Vector
                basic_gamepad.links.new(vector.outputs[0], group_006.inputs[2])
                # group_input_9.R3 Y_Axis -> group_017.Y_axis_input
                basic_gamepad.links.new(group_input_9.outputs[15], group_017.inputs[2])
                # group_input_9.R3 X_Axis -> group_017.X_axis_input
                basic_gamepad.links.new(group_input_9.outputs[14], group_017.inputs[1])
                # group_input_9.L3 Button -> group_004.Button Input
                basic_gamepad.links.new(group_input_9.outputs[8], group_004.inputs[1])
                # group_input_9.Start Button -> group_020.Button Input
                basic_gamepad.links.new(group_input_9.outputs[7], group_020.inputs[1])
                # group_input_9.D_Pad Y -> group_018.Y_Input_D_Pad
                basic_gamepad.links.new(group_input_9.outputs[17], group_018.inputs[2])
                # group_input_9.D_Pad X -> group_018.X_Input_D_Pad
                basic_gamepad.links.new(group_input_9.outputs[16], group_018.inputs[1])
                # group_input_9.L1 Button -> group_022.Button Input
                basic_gamepad.links.new(group_input_9.outputs[4], group_022.inputs[1])
                # group_input_9.R2 Bumper -> group_015.Axis Input
                basic_gamepad.links.new(group_input_9.outputs[11], group_015.inputs[1])
                # group_input_9.L3 X_Axis -> group_016.X_axis_input
                basic_gamepad.links.new(group_input_9.outputs[12], group_016.inputs[1])
                # group_input_9.R3 Button -> group_005.Button Input
                basic_gamepad.links.new(group_input_9.outputs[9], group_005.inputs[1])
                # group_input_9.L3 Y_Axis -> group_016.Y_axis_input
                basic_gamepad.links.new(group_input_9.outputs[13], group_016.inputs[2])
                # group_input_9. R1 Button -> group_023.Button Input
                basic_gamepad.links.new(group_input_9.outputs[5], group_023.inputs[1])
                # group_input_9.L2 Bumper -> group_013.Axis Input
                basic_gamepad.links.new(group_input_9.outputs[10], group_013.inputs[1])
                # group_input_9.Select Button -> group_019.Button Input
                basic_gamepad.links.new(group_input_9.outputs[6], group_019.inputs[1])
                # subdivide_mesh_1.Mesh -> group_output_9.Mesh
                basic_gamepad.links.new(subdivide_mesh_1.outputs[0], group_output_9.inputs[0])
                # cone_1.Mesh -> group_006.Geometry
                basic_gamepad.links.new(cone_1.outputs[0], group_006.inputs[0])
                # group_input_9.Square Button -> group_009.Button Input
                basic_gamepad.links.new(group_input_9.outputs[0], group_009.inputs[1])
                # group_input_9.Circle Button -> group_008.Button Input
                basic_gamepad.links.new(group_input_9.outputs[2], group_008.inputs[1])
                # group_input_9.Cross Button -> group_006.Button Input
                basic_gamepad.links.new(group_input_9.outputs[1], group_006.inputs[1])
                # group_input_9.Triangle Button -> group_007.Button Input
                basic_gamepad.links.new(group_input_9.outputs[3], group_007.inputs[1])
                # transform_geometry_011.Geometry -> join_geometry_003.Geometry
                basic_gamepad.links.new(transform_geometry_011.outputs[0], join_geometry_003.inputs[0])
                # set_material.Geometry -> join_geometry_005.Geometry
                basic_gamepad.links.new(set_material.outputs[0], join_geometry_005.inputs[0])
                # transform_geometry_013.Geometry -> join_geometry_1.Geometry
                basic_gamepad.links.new(transform_geometry_013.outputs[0], join_geometry_1.inputs[0])
                # transform_geometry_002_2.Geometry -> join_geometry_001_1.Geometry
                basic_gamepad.links.new(transform_geometry_002_2.outputs[0], join_geometry_001_1.inputs[0])
                # transform_geometry_007.Geometry -> join_geometry_004.Geometry
                basic_gamepad.links.new(transform_geometry_007.outputs[0], join_geometry_004.inputs[0])
                # transform_geometry_006_1.Geometry -> join_geometry_002.Geometry
                basic_gamepad.links.new(transform_geometry_006_1.outputs[0], join_geometry_002.inputs[0])
                # group_004.Geometry -> join_geometry_006.Geometry
                basic_gamepad.links.new(group_004.outputs[0], join_geometry_006.inputs[0])
                # transform_geometry_003_1.Geometry -> join_geometry_001_1.Geometry
                basic_gamepad.links.new(transform_geometry_003_1.outputs[0], join_geometry_001_1.inputs[0])
                # transform_geometry_015.Geometry -> join_geometry_1.Geometry
                basic_gamepad.links.new(transform_geometry_015.outputs[0], join_geometry_1.inputs[0])
                # transform_geometry_004.Geometry -> join_geometry_001_1.Geometry
                basic_gamepad.links.new(transform_geometry_004.outputs[0], join_geometry_001_1.inputs[0])
                # transform_geometry_005.Geometry -> join_geometry_1.Geometry
                basic_gamepad.links.new(transform_geometry_005.outputs[0], join_geometry_1.inputs[0])
                # transform_geometry_010.Geometry -> join_geometry_1.Geometry
                basic_gamepad.links.new(transform_geometry_010.outputs[0], join_geometry_1.inputs[0])
                # transform_geometry_014.Geometry -> join_geometry_1.Geometry
                basic_gamepad.links.new(transform_geometry_014.outputs[0], join_geometry_1.inputs[0])
                return basic_gamepad

        basic_gamepad = basic_gamepad_node_group()

        # initialize ob_gamepad_0_axis node group
        def ob_gamepad_0_axis_node_group():
                ob_gamepad_0_axis = bpy.data.node_groups.new(type='GeometryNodeTree', name=obj_name + "_axis")

                ob_gamepad_0_axis.color_tag = 'NONE'
                ob_gamepad_0_axis.description = ""
                ob_gamepad_0_axis.default_group_node_width = 140

                # ob_gamepad_0_axis interface
                # Socket axis_0
                axis_0_socket = ob_gamepad_0_axis.interface.new_socket(name="axis_0", in_out='OUTPUT',
                                                                       socket_type='NodeSocketFloat')
                axis_0_socket.default_value = 0.0
                axis_0_socket.min_value = -3.4028234663852886e+38
                axis_0_socket.max_value = 3.4028234663852886e+38
                axis_0_socket.subtype = 'NONE'
                axis_0_socket.attribute_domain = 'POINT'

                # Socket axis_1
                axis_1_socket = ob_gamepad_0_axis.interface.new_socket(name="axis_1", in_out='OUTPUT',
                                                                       socket_type='NodeSocketFloat')
                axis_1_socket.default_value = 0.0
                axis_1_socket.min_value = -3.4028234663852886e+38
                axis_1_socket.max_value = 3.4028234663852886e+38
                axis_1_socket.subtype = 'NONE'
                axis_1_socket.attribute_domain = 'POINT'

                # Socket axis_2
                axis_2_socket = ob_gamepad_0_axis.interface.new_socket(name="axis_2", in_out='OUTPUT',
                                                                       socket_type='NodeSocketFloat')
                axis_2_socket.default_value = 0.0
                axis_2_socket.min_value = -3.4028234663852886e+38
                axis_2_socket.max_value = 3.4028234663852886e+38
                axis_2_socket.subtype = 'NONE'
                axis_2_socket.attribute_domain = 'POINT'

                # Socket axis_3
                axis_3_socket = ob_gamepad_0_axis.interface.new_socket(name="axis_3", in_out='OUTPUT',
                                                                       socket_type='NodeSocketFloat')
                axis_3_socket.default_value = 0.0
                axis_3_socket.min_value = -3.4028234663852886e+38
                axis_3_socket.max_value = 3.4028234663852886e+38
                axis_3_socket.subtype = 'NONE'
                axis_3_socket.attribute_domain = 'POINT'

                # Socket axis_4
                axis_4_socket = ob_gamepad_0_axis.interface.new_socket(name="axis_4", in_out='OUTPUT',
                                                                       socket_type='NodeSocketFloat')
                axis_4_socket.default_value = 0.0
                axis_4_socket.min_value = -3.4028234663852886e+38
                axis_4_socket.max_value = 3.4028234663852886e+38
                axis_4_socket.subtype = 'NONE'
                axis_4_socket.attribute_domain = 'POINT'

                # Socket axis_5
                axis_5_socket = ob_gamepad_0_axis.interface.new_socket(name="axis_5", in_out='OUTPUT',
                                                                       socket_type='NodeSocketFloat')
                axis_5_socket.default_value = 0.0
                axis_5_socket.min_value = -3.4028234663852886e+38
                axis_5_socket.max_value = 3.4028234663852886e+38
                axis_5_socket.subtype = 'NONE'
                axis_5_socket.attribute_domain = 'POINT'

                # initialize ob_gamepad_0_axis nodes
                # node Group Output
                group_output_10 = ob_gamepad_0_axis.nodes.new("NodeGroupOutput")
                group_output_10.name = "Group Output"
                group_output_10.is_active_output = True
                # Socket_0
                group_output_10.inputs[0].default_value = 0.003906369209289551
                # Socket_1
                group_output_10.inputs[1].default_value = 0.003906369209289551
                # Socket_2
                group_output_10.inputs[2].default_value = 0.003906369209289551
                # Socket_3
                group_output_10.inputs[3].default_value = -1.000030517578125
                # Socket_4
                group_output_10.inputs[4].default_value = -1.000030517578125
                # Socket_5
                group_output_10.inputs[5].default_value = 0.003906369209289551

                # Set locations
                group_output_10.location = (0.0, 0.0)

                # Set dimensions
                group_output_10.width, group_output_10.height = 140.0, 100.0

                return ob_gamepad_0_axis

        ob_gamepad_0_axis = ob_gamepad_0_axis_node_group()

        # initialize ob_gamepad_0_button node group
        def ob_gamepad_0_button_node_group():
                ob_gamepad_0_button = bpy.data.node_groups.new(type='GeometryNodeTree', name=obj_name +"_button")

                ob_gamepad_0_button.color_tag = 'NONE'
                ob_gamepad_0_button.description = ""
                ob_gamepad_0_button.default_group_node_width = 140

                # ob_gamepad_0_button interface
                # Socket button_0
                button_0_socket = ob_gamepad_0_button.interface.new_socket(name="button_0", in_out='OUTPUT',
                                                                           socket_type='NodeSocketFloat')
                button_0_socket.default_value = 0.0
                button_0_socket.min_value = -3.4028234663852886e+38
                button_0_socket.max_value = 3.4028234663852886e+38
                button_0_socket.subtype = 'NONE'
                button_0_socket.attribute_domain = 'POINT'

                # Socket button_1
                button_1_socket = ob_gamepad_0_button.interface.new_socket(name="button_1", in_out='OUTPUT',
                                                                           socket_type='NodeSocketFloat')
                button_1_socket.default_value = 0.0
                button_1_socket.min_value = -3.4028234663852886e+38
                button_1_socket.max_value = 3.4028234663852886e+38
                button_1_socket.subtype = 'NONE'
                button_1_socket.attribute_domain = 'POINT'

                # Socket button_2
                button_2_socket = ob_gamepad_0_button.interface.new_socket(name="button_2", in_out='OUTPUT',
                                                                           socket_type='NodeSocketFloat')
                button_2_socket.default_value = 0.0
                button_2_socket.min_value = -3.4028234663852886e+38
                button_2_socket.max_value = 3.4028234663852886e+38
                button_2_socket.subtype = 'NONE'
                button_2_socket.attribute_domain = 'POINT'

                # Socket button_3
                button_3_socket = ob_gamepad_0_button.interface.new_socket(name="button_3", in_out='OUTPUT',
                                                                           socket_type='NodeSocketFloat')
                button_3_socket.default_value = 0.0
                button_3_socket.min_value = -3.4028234663852886e+38
                button_3_socket.max_value = 3.4028234663852886e+38
                button_3_socket.subtype = 'NONE'
                button_3_socket.attribute_domain = 'POINT'

                # Socket button_4
                button_4_socket = ob_gamepad_0_button.interface.new_socket(name="button_4", in_out='OUTPUT',
                                                                           socket_type='NodeSocketFloat')
                button_4_socket.default_value = 0.0
                button_4_socket.min_value = -3.4028234663852886e+38
                button_4_socket.max_value = 3.4028234663852886e+38
                button_4_socket.subtype = 'NONE'
                button_4_socket.attribute_domain = 'POINT'

                # Socket button_5
                button_5_socket = ob_gamepad_0_button.interface.new_socket(name="button_5", in_out='OUTPUT',
                                                                           socket_type='NodeSocketFloat')
                button_5_socket.default_value = 0.0
                button_5_socket.min_value = -3.4028234663852886e+38
                button_5_socket.max_value = 3.4028234663852886e+38
                button_5_socket.subtype = 'NONE'
                button_5_socket.attribute_domain = 'POINT'

                # Socket button_6
                button_6_socket = ob_gamepad_0_button.interface.new_socket(name="button_6", in_out='OUTPUT',
                                                                           socket_type='NodeSocketFloat')
                button_6_socket.default_value = 0.0
                button_6_socket.min_value = -3.4028234663852886e+38
                button_6_socket.max_value = 3.4028234663852886e+38
                button_6_socket.subtype = 'NONE'
                button_6_socket.attribute_domain = 'POINT'

                # Socket button_7
                button_7_socket = ob_gamepad_0_button.interface.new_socket(name="button_7", in_out='OUTPUT',
                                                                           socket_type='NodeSocketFloat')
                button_7_socket.default_value = 0.0
                button_7_socket.min_value = -3.4028234663852886e+38
                button_7_socket.max_value = 3.4028234663852886e+38
                button_7_socket.subtype = 'NONE'
                button_7_socket.attribute_domain = 'POINT'

                # Socket button_8
                button_8_socket = ob_gamepad_0_button.interface.new_socket(name="button_8", in_out='OUTPUT',
                                                                           socket_type='NodeSocketFloat')
                button_8_socket.default_value = 0.0
                button_8_socket.min_value = -3.4028234663852886e+38
                button_8_socket.max_value = 3.4028234663852886e+38
                button_8_socket.subtype = 'NONE'
                button_8_socket.attribute_domain = 'POINT'

                # Socket button_9
                button_9_socket = ob_gamepad_0_button.interface.new_socket(name="button_9", in_out='OUTPUT',
                                                                           socket_type='NodeSocketFloat')
                button_9_socket.default_value = 0.0
                button_9_socket.min_value = -3.4028234663852886e+38
                button_9_socket.max_value = 3.4028234663852886e+38
                button_9_socket.subtype = 'NONE'
                button_9_socket.attribute_domain = 'POINT'

                # Socket button_10
                button_10_socket = ob_gamepad_0_button.interface.new_socket(name="button_10", in_out='OUTPUT',
                                                                            socket_type='NodeSocketFloat')
                button_10_socket.default_value = 0.0
                button_10_socket.min_value = -3.4028234663852886e+38
                button_10_socket.max_value = 3.4028234663852886e+38
                button_10_socket.subtype = 'NONE'
                button_10_socket.attribute_domain = 'POINT'

                # Socket button_11
                button_11_socket = ob_gamepad_0_button.interface.new_socket(name="button_11", in_out='OUTPUT',
                                                                            socket_type='NodeSocketFloat')
                button_11_socket.default_value = 0.0
                button_11_socket.min_value = -3.4028234663852886e+38
                button_11_socket.max_value = 3.4028234663852886e+38
                button_11_socket.subtype = 'NONE'
                button_11_socket.attribute_domain = 'POINT'

                # Socket button_12
                button_12_socket = ob_gamepad_0_button.interface.new_socket(name="button_12", in_out='OUTPUT',
                                                                            socket_type='NodeSocketFloat')
                button_12_socket.default_value = 0.0
                button_12_socket.min_value = -3.4028234663852886e+38
                button_12_socket.max_value = 3.4028234663852886e+38
                button_12_socket.subtype = 'NONE'
                button_12_socket.attribute_domain = 'POINT'

                # Socket button_13
                button_13_socket = ob_gamepad_0_button.interface.new_socket(name="button_13", in_out='OUTPUT',
                                                                            socket_type='NodeSocketFloat')
                button_13_socket.default_value = 0.0
                button_13_socket.min_value = -3.4028234663852886e+38
                button_13_socket.max_value = 3.4028234663852886e+38
                button_13_socket.subtype = 'NONE'
                button_13_socket.attribute_domain = 'POINT'

                # initialize ob_gamepad_0_button nodes
                # node Group Output
                group_output_11 = ob_gamepad_0_button.nodes.new("NodeGroupOutput")
                group_output_11.name = "Group Output"
                group_output_11.is_active_output = True
                # Socket_0
                group_output_11.inputs[0].default_value = 0.0
                # Socket_1
                group_output_11.inputs[1].default_value = 0.0
                # Socket_2
                group_output_11.inputs[2].default_value = 0.0
                # Socket_3
                group_output_11.inputs[3].default_value = 0.0
                # Socket_4
                group_output_11.inputs[4].default_value = 0.0
                # Socket_5
                group_output_11.inputs[5].default_value = 0.0
                # Socket_6
                group_output_11.inputs[6].default_value = 0.0
                # Socket_7
                group_output_11.inputs[7].default_value = 0.0
                # Socket_8
                group_output_11.inputs[8].default_value = 0.0
                # Socket_9
                group_output_11.inputs[9].default_value = 0.0
                # Socket_10
                group_output_11.inputs[10].default_value = 0.0
                # Socket_11
                group_output_11.inputs[11].default_value = 0.0
                # Socket_12
                group_output_11.inputs[12].default_value = 0.0
                # Socket_13
                group_output_11.inputs[13].default_value = 0.0

                # Set locations
                group_output_11.location = (0.0, 0.0)

                # Set dimensions
                group_output_11.width, group_output_11.height = 140.0, 100.0

                return ob_gamepad_0_button

        ob_gamepad_0_button = ob_gamepad_0_button_node_group()

        # initialize ob_gamepad_0_hat node group
        def ob_gamepad_0_hat_node_group():
                ob_gamepad_0_hat = bpy.data.node_groups.new(type='GeometryNodeTree', name=obj_name + "_dpad")

                ob_gamepad_0_hat.color_tag = 'NONE'
                ob_gamepad_0_hat.description = ""
                ob_gamepad_0_hat.default_group_node_width = 140

                # ob_gamepad_0_hat interface
                # Socket hat0_0
                hat0_0_socket = ob_gamepad_0_hat.interface.new_socket(name="dpad_x_0", in_out='OUTPUT',
                                                                      socket_type='NodeSocketFloat')
                hat0_0_socket.default_value = 0.0
                hat0_0_socket.min_value = -3.4028234663852886e+38
                hat0_0_socket.max_value = 3.4028234663852886e+38
                hat0_0_socket.subtype = 'NONE'
                hat0_0_socket.attribute_domain = 'POINT'

                # Socket hat1_0
                hat1_0_socket = ob_gamepad_0_hat.interface.new_socket(name="dpad_y_0", in_out='OUTPUT',
                                                                      socket_type='NodeSocketFloat')
                hat1_0_socket.default_value = 0.0
                hat1_0_socket.min_value = -3.4028234663852886e+38
                hat1_0_socket.max_value = 3.4028234663852886e+38
                hat1_0_socket.subtype = 'NONE'
                hat1_0_socket.attribute_domain = 'POINT'

                # initialize ob_gamepad_0_hat nodes
                # node Group Output
                group_output_12 = ob_gamepad_0_hat.nodes.new("NodeGroupOutput")
                group_output_12.name = "Group Output"
                group_output_12.is_active_output = True
                # Socket_0
                group_output_12.inputs[0].default_value = 0.0
                # Socket_1
                group_output_12.inputs[1].default_value = 0.0

                # Set locations
                group_output_12.location = (0.0, 0.0)

                # Set dimensions
                group_output_12.width, group_output_12.height = 140.0, 100.0

                return ob_gamepad_0_hat

        ob_gamepad_0_hat = ob_gamepad_0_hat_node_group()

        # initialize gamepad_gn node group
        def gamepad_gn_node_group():
                gamepad_gn = bpy.data.node_groups.new(type='GeometryNodeTree', name=obj_name + '_GN')

                gamepad_gn.color_tag = 'NONE'
                gamepad_gn.description = ""
                gamepad_gn.default_group_node_width = 140

                gamepad_gn.is_modifier = True

                # gamepad_gn interface
                # Socket Geometry
                geometry_socket_18 = gamepad_gn.interface.new_socket(name="Geometry", in_out='OUTPUT',
                                                                     socket_type='NodeSocketGeometry')
                geometry_socket_18.attribute_domain = 'POINT'

                # Socket Geometry
                geometry_socket_19 = gamepad_gn.interface.new_socket(name="Geometry", in_out='INPUT',
                                                                     socket_type='NodeSocketGeometry')
                geometry_socket_19.attribute_domain = 'POINT'

                # initialize gamepad_gn nodes
                # node Group Output
                group_output_13 = gamepad_gn.nodes.new("NodeGroupOutput")
                group_output_13.name = "Group Output"
                group_output_13.is_active_output = True

                # node Group.025
                group_025 = gamepad_gn.nodes.new("GeometryNodeGroup")
                group_025.name = "Group.025"
                group_025.node_tree = basic_gamepad

                # node Join Geometry
                join_geometry_2 = gamepad_gn.nodes.new("GeometryNodeJoinGeometry")
                join_geometry_2.name = "Join Geometry"

                # node Group
                group = gamepad_gn.nodes.new("GeometryNodeGroup")
                group.name = "Group"
                group.node_tree = ob_gamepad_0_axis

                # node Group.001
                group_001_2 = gamepad_gn.nodes.new("GeometryNodeGroup")
                group_001_2.name = "Group.001"
                group_001_2.node_tree = ob_gamepad_0_button

                # node Group.002
                group_002_1 = gamepad_gn.nodes.new("GeometryNodeGroup")
                group_002_1.name = "Group.002"
                group_002_1.node_tree = ob_gamepad_0_hat

                # Set locations
                group_output_13.location = (-85.52473449707031, 571.5177001953125)
                group_025.location = (-621.7999267578125, 572.7494506835938)
                join_geometry_2.location = (-265.28302001953125, 563.1323852539062)
                group.location = (-909.81982421875, 380.09429931640625)
                group_001_2.location = (-1043.80419921875, 753.9282836914062)
                group_002_1.location = (-913.6046142578125, 174.21652221679688)

                # Set dimensions
                group_output_13.width, group_output_13.height = 80.0, 100.0
                group_025.width, group_025.height = 140.0, 100.0
                join_geometry_2.width, join_geometry_2.height = 140.0, 100.0
                group.width, group.height = 140.0, 100.0
                group_001_2.width, group_001_2.height = 140.0, 100.0
                group_002_1.width, group_002_1.height = 140.0, 100.0

                # initialize gamepad_gn links
                # join_geometry_2.Geometry -> group_output_13.Geometry
                gamepad_gn.links.new(join_geometry_2.outputs[0], group_output_13.inputs[0])
                # group_025.Mesh -> join_geometry_2.Geometry
                gamepad_gn.links.new(group_025.outputs[0], join_geometry_2.inputs[0])
                # group_002_1.hat0_0 -> group_025.D_Pad X
                gamepad_gn.links.new(group_002_1.outputs[0], group_025.inputs[16])
                # group_002_1.hat1_0 -> group_025.D_Pad Y
                gamepad_gn.links.new(group_002_1.outputs[1], group_025.inputs[17])
                # group.axis_4 -> group_025.R2 Bumper
                gamepad_gn.links.new(group.outputs[4], group_025.inputs[11])
                # group.axis_5 -> group_025.R3 Y_Axis
                gamepad_gn.links.new(group.outputs[5], group_025.inputs[15])
                # group.axis_2 -> group_025.R3 X_Axis
                gamepad_gn.links.new(group.outputs[2], group_025.inputs[14])
                # group.axis_0 -> group_025.L3 X_Axis
                gamepad_gn.links.new(group.outputs[0], group_025.inputs[12])
                # group.axis_1 -> group_025.L3 Y_Axis
                gamepad_gn.links.new(group.outputs[1], group_025.inputs[13])
                # group.axis_3 -> group_025.L2 Bumper
                gamepad_gn.links.new(group.outputs[3], group_025.inputs[10])
                # group_001_2.button_0 -> group_025.Square Button
                gamepad_gn.links.new(group_001_2.outputs[0], group_025.inputs[0])
                # group_001_2.button_1 -> group_025.Cross Button
                gamepad_gn.links.new(group_001_2.outputs[1], group_025.inputs[1])
                # group_001_2.button_2 -> group_025.Circle Button
                gamepad_gn.links.new(group_001_2.outputs[2], group_025.inputs[2])
                # group_001_2.button_3 -> group_025.Triangle Button
                gamepad_gn.links.new(group_001_2.outputs[3], group_025.inputs[3])
                # group_001_2.button_10 -> group_025.L3 Button
                gamepad_gn.links.new(group_001_2.outputs[10], group_025.inputs[8])
                # group_001_2.button_11 -> group_025.R3 Button
                gamepad_gn.links.new(group_001_2.outputs[11], group_025.inputs[9])
                # group_001_2.button_8 -> group_025.Select Button
                gamepad_gn.links.new(group_001_2.outputs[8], group_025.inputs[6])
                # group_001_2.button_9 -> group_025.Start Button
                gamepad_gn.links.new(group_001_2.outputs[9], group_025.inputs[7])
                # group_001_2.button_4 -> group_025.L1 Button
                gamepad_gn.links.new(group_001_2.outputs[4], group_025.inputs[4])
                # group_001_2.button_5 -> group_025. R1 Button
                gamepad_gn.links.new(group_001_2.outputs[5], group_025.inputs[5])
                return gamepad_gn

        gamepad_gn = gamepad_gn_node_group()

        bpy.ops.mesh.primitive_cube_add()
        bpy.context.active_object.name = "Gamepad_Model"
        bpy.context.object.modifiers.new('geometry', 'NODES')
        bpy.context.object.modifiers['geometry'].node_group = bpy.data.node_groups[obj_name + '_GN']