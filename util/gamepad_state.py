from ..config import IS_DEBUG

EVENT_ABB = (
    ("Absolute-ABS_HAT0X", "HX"),
    ("Absolute-ABS_HAT0Y", "HY"),
    ("Key-BTN_NORTH", "N"),
    ("Key-BTN_EAST", "E"),
    ("Key-BTN_SOUTH", "S"),
    ("Key-BTN_WEST", "W"),
    ("Key-BTN_THUMBL", "THL"),
    ("Key-BTN_THUMBR", "THR"),
    ("Key-BTN_TL", "TL"),
    ("Key-BTN_TR", "TR"),
    ("Key-BTN_TL2", "TL2"),
    ("Key-BTN_TR2", "TR3"),
    ("Key-BTN_MODE", "M"),
    ("Key-BTN_START", "ST"),
    ("Key-BTN_TRIGGER", "N"),
    ("Key-BTN_THUMB", "E"),
    ("Key-BTN_THUMB2", "S"),
    ("Key-BTN_TOP", "W"),
    ("Key-BTN_BASE3", "SL"),
    ("Key-BTN_BASE4", "ST"),
    ("Key-BTN_TOP2", "TL"),
    ("Key-BTN_PINKIE", "TR"),
)

MIN_ABS_DIFFERENCE = 5

def init_state(abbrevs=EVENT_ABB):
    abbrevs_dict = dict(abbrevs)
    btn_state = {}
    old_btn_state = {}
    abs_state = {}
    old_abs_state = {}
    for key, value in abbrevs_dict.items():
        if key.startswith("Absolute"):
            abs_state[value] = 0
            old_abs_state[value] = 0
        if key.startswith("Key"):
            btn_state[value] = 0
            old_btn_state[value] = 0
    return {
        "abbrevs": abbrevs_dict,
        "btn_state": btn_state,
        "old_btn_state": old_btn_state,
        "abs_state": abs_state,
        "old_abs_state": old_abs_state,
        "_other": 0,
        "nodes": [],
    }

def format_state(state):
    out = ""
    for k, v in state["abs_state"].items():
        out += f"{k}:{v:>4} "
    for k, v in state["btn_state"].items():
        out += f"{k}:{v} "
    return out

def handle_unknown_event(state, ev_type, key):
    if ev_type == "Key":
        new_abbv = "B" + str(state["_other"])
        state["btn_state"][new_abbv] = 0
        state["old_btn_state"][new_abbv] = 0
    elif ev_type == "Absolute":
        new_abbv = "A" + str(state["_other"])
        state["abs_state"][new_abbv] = 0
        state["old_abs_state"][new_abbv] = 0
    else:
        return None
    state["abbrevs"][key] = new_abbv
    state["_other"] += 1
    return new_abbv

def output_state(state, ev_type, abbv, nodes):
    if ev_type == "Key":
        if state["btn_state"][abbv] != state["old_btn_state"][abbv]:
            if IS_DEBUG:
                print(format_state(state))
            for node in nodes:
                node.outputs[0].input_value = abbv
                node.outputs[1].input_value = state["btn_state"][abbv]
            return
    if abbv and abbv[0] == "H":
        if IS_DEBUG:
            print(format_state(state))
        for node in nodes:
            node.outputs[2].input_value = abbv
            node.outputs[3].input_value = state["abs_state"][abbv]
        return
    if abbv in state["abs_state"]:
        diff = state["abs_state"][abbv] - state["old_abs_state"][abbv]
        if abs(diff) > MIN_ABS_DIFFERENCE:
            for node in nodes:
                node.outputs[4].input_value = abbv
                node.outputs[5].input_value = state["abs_state"][abbv]
            if IS_DEBUG:
                print(format_state(state))

def process_event(state, ev, nodes):
    ev_type = ev["ev_type"]
    code = ev["code"]
    state_val = ev["state"]
    if ev_type in ("Sync", "Misc"):
        return
    key = f"{ev_type}-{code}"
    try:
        abbv = state["abbrevs"][key]
    except KeyError:
        abbv = handle_unknown_event(state, ev_type, key)
        if not abbv:
            return
    if ev_type == "Key":
        state["old_btn_state"][abbv] = state["btn_state"][abbv]
        state["btn_state"][abbv] = state_val
    if ev_type == "Absolute":
        state["old_abs_state"][abbv] = state["abs_state"][abbv]
        state["abs_state"][abbv] = state_val
    output_state(state, ev_type, abbv, nodes)