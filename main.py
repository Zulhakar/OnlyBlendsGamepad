import bpy
from .constants import *

def create_gamepad_empty(name):
    gamepad_reader_empty = bpy.data.objects.get(name)
    if gamepad_reader_empty is None:
        gamepad_reader_empty = bpy.data.objects.new(name, None)
        gamepad_reader_empty.use_fake_user = True
    return gamepad_reader_empty

