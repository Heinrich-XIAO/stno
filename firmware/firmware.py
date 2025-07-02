import board
import math
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.hid import HIDModes
from kmk.hid import HIDKeycode
from kmk.modules.analog import Analog
from kmk.modules.steno import Steno
from kmk.modules.mouse_keys import MouseKeys

keyboard = KMKKeyboard()
keyboard.modules.append(MouseKeys())
keyboard.modules.append(Layers())
keyboard.modules.append(Steno())
keyboard.modules.append(HIDModes())
# Analog joystick module
analog = Analog()
keyboard.modules.append(analog)



def transform_grid(input_grid, extra_key):
    transformed = [[None for _ in range(5)] for _ in range(5)]

    for col in range(5):
        for row in range(4):
            transformed[col][row] = input_grid[row][col]

    for row in range(4):
        transformed[4][row] = input_grid[row][5]

    transformed[4][4] = extra_key

    flat_output = [transformed[r][c] for r in range(5) for c in range(5)]
    return flat_output



keyboard.col_pins = (board.D0, board.D1, board.D4, board.D5, board.D6)  # 5 cols
keyboard.row_pins = (board.D7, board.D8, board.D9, board.D10, board.D11)  # 5 rows

keyboard.diode_orientation = keyboard.DIODE_COL2ROW

layer0 = [
    KC.F,    KC.P,   KC.L,   KC.T,   KC.D,
    KC.R,     KC.B,    KC.G,    KC.S,    KC.Z,
    KC.S,     KC.T,    KC.P,    KC.H,    KC.J,
    KC.ASTR,  KC.K,    KC.W,    KC.R,    KC.N,
    KC.TRNS,KC.MB_LMB,KC.MB_RMB,KC.MB_MMB,KC.TRNS,
]

keyboard.keymap = [
    transform_grid(layer0, KC.TRNS),
]


# Constants
V_PIN = board.A0
H_PIN = board.A1
DEADZONE = 0.2  # to ignore small wobbles

# This maps 16 compass directions to AOEU chords
SECTOR_CHORDS = [
    ('O',),               # 0   → East
    ('A','O'),            # 1   → ENE
    ('A','O','E'),        # 2   → NE
    ('O','E'),            # 3   → NNE
    ('E',),               # 4   → South
    ('A','E'),            # 5   → SSE
    ('A','E','U'),        # 6   → SE
    ('E','U'),            # 7   → ESE
    ('U',),               # 8   → West
    ('A','U'),            # 9   → WNW
    ('A','O','U'),        # 10  → NW
    ('O','U'),            # 11  → NNW
    ('A',),               # 12  → North
    ('A','O','E','U'),    # 13  → NNE wraparound
    ('O','E','U'),        # 14  → ESE wraparound
    ('A','U','E'),        # 15  → SSE wraparound
]


# Mapping from steno letter to HIDKeycode used by Plover
STENO_KEYCODES = {
    'A': HIDKeycode.S,
    'O': HIDKeycode.D,
    'E': HIDKeycode.F,
    'U': HIDKeycode.J,
}

def get_steno_chord_from_joystick():
    v = analog.analog_read(V_PIN)  # vertical axis
    h = analog.analog_read(H_PIN)  # horizontal axis

    # Normalize to -1.0 ... 1.0
    v = (v - 32768) / 32768
    h = (h - 32768) / 32768

    magnitude = math.sqrt(h*h + v*v)
    if magnitude < DEADZONE:
        return []  # don't send anything

    angle = math.atan2(-v, h)  # invert v to treat upward as +Y
    angle_deg = math.degrees(angle)
    angle_deg = (angle_deg + 360) % 360

    sector = int((angle_deg + 11.25) // 22.5) % 16
    chord = SECTOR_CHORDS[sector]
    return [STENO_KEYCODES[c] for c in chord if c in STENO_KEYCODES]

def before_matrix_scan():
    chord = get_steno_chord_from_joystick()
    if chord:
        keyboard.send_hid(chord)

keyboard.before_matrix_scan = before_matrix_scan


if __name__ == '__main__':
    keyboard.go()

