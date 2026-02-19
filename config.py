IS_DEBUG = False
APP_NAME = "OnlyBlends.Gamepad"
APP_NAME_SHORT = "obc"
OB_TREE_TYPE = 'OnlyBlendsGamepadNodeTree'
NEW_NODE_GROUP_NAME = "Gamepad Nodes"
NODE_EDITOR_NAME = "OnlyBlends.Gamepad Node Editor"
TREE_ICON = 'PLUGIN'

########################################################################################################################
# don't change this
from .cnt.base.constants import *

CONSTANTS_MENU_IDNAME = f'NODE_MT_{APP_NAME_SHORT}_Constants'
INPUT_MENU_IDNAME = f'NODE_MT_{APP_NAME_SHORT}_Input'
GROUP_MENU_IDNAME = f'NOD_MT_{APP_NAME_SHORT}_Group'
MAKE_GROUP_OT_IDNAME = f'node.{APP_NAME_SHORT}_make_group'
