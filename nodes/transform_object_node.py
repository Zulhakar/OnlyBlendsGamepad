import bpy
from ..cnt.nodes.basic_nodes import ConstantNodeCnt
from ..config import CntSocketTypes
import math
from mathutils import Vector

class TransformObjectNodeCnt(ConstantNodeCnt):
    bl_label = "Transform Object"

    def init(self, context):
        self.inputs.new(CntSocketTypes.Object, "Object")
        self.inputs.new(CntSocketTypes.Float, "X")
        self.inputs.new(CntSocketTypes.Float, "Y")
        self.inputs.new(CntSocketTypes.Float, "Z")
        self.inputs.new(CntSocketTypes.Float, "rot X")
        self.inputs.new(CntSocketTypes.Float, "rot Y")
        self.inputs.new(CntSocketTypes.Float, "rot Z")
        self.inputs.new(CntSocketTypes.Float, "scale X")
        self.inputs.new(CntSocketTypes.Float, "scale Y")
        self.inputs.new(CntSocketTypes.Float, "scale Z")

    def camera_update(self):
        if self.inputs[0].input_value:
            obj = self.inputs[0].input_value
            obj.location = (self.inputs[1].input_value, self.inputs[2].input_value, self.inputs[3].input_value)
            obj.rotation_euler = (math.radians(self.inputs[4].input_value), math.radians(self.inputs[5].input_value), math.radians(self.inputs[6].input_value))
            obj.scale = (self.inputs[7].input_value, self.inputs[8].input_value, self.inputs[9].input_value)

    def socket_update(self, socket):
        if not self.mute:
            if not socket.is_output:
                self.camera_update()
            else:
                for link in socket.links:
                    link.to_socket.input_value = socket.input_value


