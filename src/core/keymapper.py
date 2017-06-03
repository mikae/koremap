import evdev.ecodes as ecodes

# - Documentatsii net
# - Pochemu?
# - Potomu-chto idi nahui, vot pochemu

MODIFIER_NONE = 0x0

MODIFIER_LEFTSHIFT = 0x1
MODIFIER_LEFTCTRL = 0x2
MODIFIER_LEFTALT = 0x4
MODIFIER_LEFTMETA = 0x8

MODIFIER_RIGHTSHIFT = 0x16
MODIFIER_RIGHTCTRL = 0x32
MODIFIER_RIGHTALT = 0x64
MODIFIER_RIGHTMETA = 0x128

char_to_key_code_table = {
    "A": ecodes.KEY_A,
    "B": ecodes.KEY_B,
    "C": ecodes.KEY_C,
    "D": ecodes.KEY_D,
    "E": ecodes.KEY_E,
    "F": ecodes.KEY_F,
    "G": ecodes.KEY_G,
    "H": ecodes.KEY_H,
    "I": ecodes.KEY_I,
    "J": ecodes.KEY_J,
    "K": ecodes.KEY_K,
    "L": ecodes.KEY_L,
    "M": ecodes.KEY_M,
    "N": ecodes.KEY_N,
    "O": ecodes.KEY_O,
    "P": ecodes.KEY_P,
    "Q": ecodes.KEY_Q,
    "R": ecodes.KEY_R,
    "S": ecodes.KEY_S,
    "T": ecodes.KEY_T,
    "U": ecodes.KEY_U,
    "V": ecodes.KEY_V,
    "W": ecodes.KEY_W,
    "X": ecodes.KEY_X,
    "Y": ecodes.KEY_Y,
    "Z": ecodes.KEY_Z,

    "a": ecodes.KEY_A,
    "b": ecodes.KEY_B,
    "c": ecodes.KEY_C,
    "d": ecodes.KEY_D,
    "e": ecodes.KEY_E,
    "f": ecodes.KEY_F,
    "g": ecodes.KEY_G,
    "h": ecodes.KEY_H,
    "i": ecodes.KEY_I,
    "j": ecodes.KEY_J,
    "k": ecodes.KEY_K,
    "l": ecodes.KEY_L,
    "m": ecodes.KEY_M,
    "n": ecodes.KEY_N,
    "o": ecodes.KEY_O,
    "p": ecodes.KEY_P,
    "q": ecodes.KEY_Q,
    "r": ecodes.KEY_R,
    "s": ecodes.KEY_S,
    "t": ecodes.KEY_T,
    "u": ecodes.KEY_U,
    "v": ecodes.KEY_V,
    "w": ecodes.KEY_W,
    "x": ecodes.KEY_X,
    "y": ecodes.KEY_Y,
    "z": ecodes.KEY_Z,

    "1": ecodes.KEY_1,
    "2": ecodes.KEY_2,
    "3": ecodes.KEY_3,
    "4": ecodes.KEY_4,
    "5": ecodes.KEY_5,
    "6": ecodes.KEY_6,
    "7": ecodes.KEY_7,
    "8": ecodes.KEY_8,
    "9": ecodes.KEY_9,
    "0": ecodes.KEY_0,

    "!": ecodes.KEY_1,
    "@": ecodes.KEY_2,
    "#": ecodes.KEY_3,
    "$": ecodes.KEY_4,
    "%": ecodes.KEY_5,
    "^": ecodes.KEY_6,
    "&": ecodes.KEY_7,
    "*": ecodes.KEY_8,
    "(": ecodes.KEY_9,
    ")": ecodes.KEY_0,

    "{": ecodes.KEY_LEFTBRACE,
    "}": ecodes.KEY_RIGHTBRACE,
    "[": ecodes.KEY_LEFTBRACE,
    "]": ecodes.KEY_RIGHTBRACE,

    " ": ecodes.KEY_SPACE,
    ".": ecodes.KEY_DOT,
    ",": ecodes.KEY_COMMA,
    "/": ecodes.KEY_SLASH,
    "\\": ecodes.KEY_BACKSLASH,
    "'": ecodes.KEY_APOSTROPHE,
    ";": ecodes.KEY_SEMICOLON,
    "-": ecodes.KEY_MINUS,
    "=": ecodes.KEY_EQUAL,

    "_": ecodes.KEY_MINUS,
    "+": ecodes.KEY_EQUAL,
    ":": ecodes.KEY_SEMICOLON,
    ">": ecodes.KEY_DOT,
    "<": ecodes.KEY_COMMA,
    "?": ecodes.KEY_SLASH,
    "|": ecodes.KEY_BACKSLASH,
    "\"": ecodes.KEY_APOSTROPHE,
    '`': ecodes.KEY_GRAVE,
}

char_to_key_code_modifier_table = {
    ">": MODIFIER_LEFTSHIFT,
    "<": MODIFIER_LEFTSHIFT,
    "?": MODIFIER_LEFTSHIFT,
    "|": MODIFIER_LEFTSHIFT,
    "\"": MODIFIER_LEFTSHIFT,
    ":": MODIFIER_LEFTSHIFT,

    "!": MODIFIER_LEFTSHIFT,
    "@": MODIFIER_LEFTSHIFT,
    "#": MODIFIER_LEFTSHIFT,
    "$": MODIFIER_LEFTSHIFT,
    "%": MODIFIER_LEFTSHIFT,
    "^": MODIFIER_LEFTSHIFT,
    "&": MODIFIER_LEFTSHIFT,
    "*": MODIFIER_LEFTSHIFT,
    "(": MODIFIER_LEFTSHIFT,
    ")": MODIFIER_LEFTSHIFT,
    "_": MODIFIER_LEFTSHIFT,
    "+": MODIFIER_LEFTSHIFT,
    "{": MODIFIER_LEFTSHIFT,
    "}": MODIFIER_LEFTSHIFT,

    "A": MODIFIER_LEFTSHIFT,
    "B": MODIFIER_LEFTSHIFT,
    "C": MODIFIER_LEFTSHIFT,
    "D": MODIFIER_LEFTSHIFT,
    "E": MODIFIER_LEFTSHIFT,
    "F": MODIFIER_LEFTSHIFT,
    "G": MODIFIER_LEFTSHIFT,
    "H": MODIFIER_LEFTSHIFT,
    "I": MODIFIER_LEFTSHIFT,
    "J": MODIFIER_LEFTSHIFT,
    "K": MODIFIER_LEFTSHIFT,
    "L": MODIFIER_LEFTSHIFT,
    "M": MODIFIER_LEFTSHIFT,
    "N": MODIFIER_LEFTSHIFT,
    "O": MODIFIER_LEFTSHIFT,
    "P": MODIFIER_LEFTSHIFT,
    "Q": MODIFIER_LEFTSHIFT,
    "R": MODIFIER_LEFTSHIFT,
    "S": MODIFIER_LEFTSHIFT,
    "T": MODIFIER_LEFTSHIFT,
    "U": MODIFIER_LEFTSHIFT,
    "V": MODIFIER_LEFTSHIFT,
    "W": MODIFIER_LEFTSHIFT,
    "X": MODIFIER_LEFTSHIFT,
    "Y": MODIFIER_LEFTSHIFT,
    "Z": MODIFIER_LEFTSHIFT,
}

key_code_to_key_name_table = {
    ecodes.KEY_1: '1',
    ecodes.KEY_2: '2',
    ecodes.KEY_3: '3',
    ecodes.KEY_4: '4',
    ecodes.KEY_5: '5',
    ecodes.KEY_6: '6',
    ecodes.KEY_7: '7',
    ecodes.KEY_8: '8',
    ecodes.KEY_9: '9',
    ecodes.KEY_0: '0',

    ecodes.KEY_Q: 'Q',
    ecodes.KEY_W: 'W',
    ecodes.KEY_E: 'E',
    ecodes.KEY_R: 'R',
    ecodes.KEY_Y: 'Y',
    ecodes.KEY_U: 'U',
    ecodes.KEY_I: 'I',
    ecodes.KEY_O: 'O',
    ecodes.KEY_P: 'P',
    ecodes.KEY_A: 'A',
    ecodes.KEY_S: 'S',
    ecodes.KEY_D: 'D',
    ecodes.KEY_F: 'F',
    ecodes.KEY_G: 'G',
    ecodes.KEY_H: 'H',
    ecodes.KEY_J: 'J',
    ecodes.KEY_K: 'K',
    ecodes.KEY_L: 'L',
    ecodes.KEY_Z: 'Z',
    ecodes.KEY_X: 'X',
    ecodes.KEY_C: 'C',
    ecodes.KEY_V: 'V',
    ecodes.KEY_B: 'B',
    ecodes.KEY_N: 'N',
    ecodes.KEY_M: 'M',

    ecodes.KEY_GRAVE: '`',
    ecodes.KEY_TAB: 'TAB',
    ecodes.KEY_CAPSLOCK: 'CAPS',
    ecodes.KEY_LEFTSHIFT: 'LEFTSHIFT',
    ecodes.KEY_LEFTCTRL: 'LEFTCTRL',
    ecodes.KEY_LEFTMETA: 'LEFTMETA',
    ecodes.KEY_LEFTALT: 'LEFTALT',
    ecodes.KEY_SPACE: 'SPACE',
    ecodes.KEY_RIGHTALT: 'RIGHTALT',
    ecodes.KEY_RIGHTMETA: 'RIGHTMETA',
    ecodes.KEY_RIGHTCTRL: 'RIGHTCTRL',
    ecodes.KEY_RIGHTSHIFT: 'RIGHTSHIFT',
    ecodes.KEY_ENTER: 'ENTER',
    ecodes.KEY_LEFTBRACE: '[',
    ecodes.KEY_RIGHTBRACE: ']',
    ecodes.KEY_SEMICOLON: ';',
    ecodes.KEY_APOSTROPHE: '\'',
    ecodes.KEY_BACKSLASH: '\\',
    ecodes.KEY_COMMA: ',',
    ecodes.KEY_DOT: '.',
    ecodes.KEY_SLASH: '/',

    ecodes.KEY_F1: 'F1',
    ecodes.KEY_F2: 'F2',
    ecodes.KEY_F3: 'F3',
    ecodes.KEY_F4: 'F4',
    ecodes.KEY_F5: 'F5',
    ecodes.KEY_F6: 'F6',
    ecodes.KEY_F7: 'F7',
    ecodes.KEY_F8: 'F8',
    ecodes.KEY_F9: 'F9',
    ecodes.KEY_F10: 'F10',
    ecodes.KEY_F11: 'F11',
    ecodes.KEY_F12: 'F12',

    ecodes.KEY_INSERT: 'INSERT',
    ecodes.KEY_DELETE: 'DELETE',
    ecodes.KEY_HOME: 'HOME',
    ecodes.KEY_END: 'END',
    ecodes.KEY_PAGEUP: 'PAGEUP',
    ecodes.KEY_PAGEDOWN: 'PAGEDOWN',

    ecodes.KEY_LEFT: 'LEFTARROW',
    ecodes.KEY_RIGHT: 'RIGHTARROW',
    ecodes.KEY_UP: 'UPARROW',
    ecodes.KEY_DOWN: 'DOWNARROW',

    ecodes.KEY_PRINT: 'PRINT',
    ecodes.KEY_SCROLLLOCK: 'SCROLLLOCK',
    ecodes.KEY_PAUSE: 'PAUSE',

    ecodes.KEY_NUMLOCK: 'NUMLOCK',
    ecodes.KEY_KP1: 'NUM1',
    ecodes.KEY_KP2: 'NUM2',
    ecodes.KEY_KP3: 'NUM3',
    ecodes.KEY_KP4: 'NUM4',
    ecodes.KEY_KP5: 'NUM5',
    ecodes.KEY_KP6: 'NUM6',
    ecodes.KEY_KP7: 'NUM7',
    ecodes.KEY_KP8: 'NUM8',
    ecodes.KEY_KP9: 'NUM9',
    ecodes.KEY_KP0: 'NUM0',

    ecodes.KEY_KPDOT: 'NUMDOT',
    ecodes.KEY_KPSLASH: 'NUM/',
    ecodes.KEY_KPMINUS: 'NUM-',
    ecodes.KEY_KPPLUS: 'NUM+',
    ecodes.KEY_KPENTER: 'NUMENTER',
    ecodes.KEY_KPASTERISK: 'NUM*',

    ecodes.KEY_MINUS: '-',
    ecodes.KEY_EQUAL: '=',

    ecodes.KEY_BACKSPACE: 'BACKSPACE',

    ecodes.KEY_VOLUMEUP: 'VOLUMEUP',
    ecodes.KEY_VOLUMEDOWN: 'VOLUMEDOWN',
}


key_name_to_key_code_table = {
    '1': ecodes.KEY_1,
    '2': ecodes.KEY_2,
    '3': ecodes.KEY_3,
    '4': ecodes.KEY_4,
    '5': ecodes.KEY_5,
    '6': ecodes.KEY_6,
    '7': ecodes.KEY_7,
    '8': ecodes.KEY_8,
    '9': ecodes.KEY_9,
    '0': ecodes.KEY_0,

    'q': ecodes.KEY_Q,
    'w': ecodes.KEY_W,
    'e': ecodes.KEY_E,
    'r': ecodes.KEY_R,
    't': ecodes.KEY_T,
    'y': ecodes.KEY_Y,
    'u': ecodes.KEY_U,
    'i': ecodes.KEY_I,
    'o': ecodes.KEY_O,
    'p': ecodes.KEY_P,
    'a': ecodes.KEY_A,
    's': ecodes.KEY_S,
    'd': ecodes.KEY_D,
    'f': ecodes.KEY_F,
    'g': ecodes.KEY_G,
    'h': ecodes.KEY_H,
    'j': ecodes.KEY_J,
    'k': ecodes.KEY_K,
    'l': ecodes.KEY_L,
    'z': ecodes.KEY_Z,
    'x': ecodes.KEY_X,
    'c': ecodes.KEY_C,
    'v': ecodes.KEY_V,
    'b': ecodes.KEY_B,
    'n': ecodes.KEY_N,
    'm': ecodes.KEY_M,
    'q': ecodes.KEY_Q,
    'w': ecodes.KEY_W,
    'e': ecodes.KEY_E,
    'r': ecodes.KEY_R,
    'y': ecodes.KEY_Y,
    'u': ecodes.KEY_U,
    'i': ecodes.KEY_I,
    'o': ecodes.KEY_O,
    'p': ecodes.KEY_P,
    'a': ecodes.KEY_A,
    's': ecodes.KEY_S,
    'd': ecodes.KEY_D,
    'f': ecodes.KEY_F,
    'g': ecodes.KEY_G,
    'h': ecodes.KEY_H,
    'j': ecodes.KEY_J,
    'k': ecodes.KEY_K,
    'l': ecodes.KEY_L,
    'z': ecodes.KEY_Z,
    'x': ecodes.KEY_X,
    'c': ecodes.KEY_C,
    'v': ecodes.KEY_V,
    'b': ecodes.KEY_B,
    'n': ecodes.KEY_N,
    'm': ecodes.KEY_M,

    '`': ecodes.KEY_GRAVE,
    'TAB': ecodes.KEY_TAB,
    'CAPS': ecodes.KEY_CAPSLOCK,

    'LEFTSHIFT': ecodes.KEY_LEFTSHIFT,
    'LEFTCTRL': ecodes.KEY_LEFTCTRL,
    'LEFTMETA': ecodes.KEY_LEFTMETA,
    'LEFTALT': ecodes.KEY_LEFTALT,

    'SPACE': ecodes.KEY_SPACE,
    'ENTER': ecodes.KEY_ENTER,

    'RIGHTALT': ecodes.KEY_RIGHTALT,
    'RIGHTMETA': ecodes.KEY_RIGHTMETA,
    'RIGHTCTRL': ecodes.KEY_RIGHTCTRL,
    'RIGHTSHIFT': ecodes.KEY_RIGHTSHIFT,

    '[': ecodes.KEY_LEFTBRACE,
    ']': ecodes.KEY_RIGHTBRACE,
    ';': ecodes.KEY_SEMICOLON,
    '\'': ecodes.KEY_APOSTROPHE,
    '\\': ecodes.KEY_BACKSLASH,
    ',': ecodes.KEY_COMMA,
    '.': ecodes.KEY_DOT,
    '/': ecodes.KEY_SLASH,

    'LEFTBRACE': ecodes.KEY_LEFTBRACE,
    'RIGHTBRACE': ecodes.KEY_RIGHTBRACE,
    'SEMICOLON': ecodes.KEY_SEMICOLON,
    'APOSTROPHE': ecodes.KEY_APOSTROPHE,
    'BACKSLASH': ecodes.KEY_BACKSLASH,
    'COMMA': ecodes.KEY_COMMA,
    'DOT': ecodes.KEY_DOT,
    'SLASH': ecodes.KEY_SLASH,

    'F1': ecodes.KEY_F1,
    'F2': ecodes.KEY_F2,
    'F3': ecodes.KEY_F3,
    'F4': ecodes.KEY_F4,
    'F5': ecodes.KEY_F5,
    'F6': ecodes.KEY_F6,
    'F7': ecodes.KEY_F7,
    'F8': ecodes.KEY_F8,
    'F9': ecodes.KEY_F9,
    'F10': ecodes.KEY_F10,
    'F11': ecodes.KEY_F11,
    'F12': ecodes.KEY_F12,

    'INSERT': ecodes.KEY_INSERT,
    'DELETE': ecodes.KEY_DELETE,
    'HOME': ecodes.KEY_HOME,
    'END': ecodes.KEY_END,
    'PAGEUP': ecodes.KEY_PAGEUP,
    'PAGEDOWN': ecodes.KEY_PAGEDOWN,

    'LEFTARROW': ecodes.KEY_LEFT,
    'RIGHTARROW': ecodes.KEY_RIGHT,
    'UPARROW': ecodes.KEY_UP,
    'DOWNARROW': ecodes.KEY_DOWN,

    'PRINT': ecodes.KEY_PRINT,
    'SCROLLLOCK': ecodes.KEY_SCROLLLOCK,
    'PAUSE': ecodes.KEY_PAUSE,
    'NUMLOCK': ecodes.KEY_NUMLOCK,

    'NUM1': ecodes.KEY_KP1,
    'NUM2': ecodes.KEY_KP2,
    'NUM3': ecodes.KEY_KP3,
    'NUM4': ecodes.KEY_KP4,
    'NUM5': ecodes.KEY_KP5,
    'NUM6': ecodes.KEY_KP6,
    'NUM7': ecodes.KEY_KP7,
    'NUM8': ecodes.KEY_KP8,
    'NUM9': ecodes.KEY_KP9,
    'NUM0': ecodes.KEY_KP0,
    'NUMDOT': ecodes.KEY_KPDOT,
    'NUM/': ecodes.KEY_KPSLASH,
    'NUM-': ecodes.KEY_KPMINUS,
    'NUM+': ecodes.KEY_KPPLUS,
    'NUMENTER': ecodes.KEY_KPENTER,
    'NUM*': ecodes.KEY_KPASTERISK,

    '-': ecodes.KEY_MINUS,
    '=': ecodes.KEY_EQUAL,
    'BACKSPACE': ecodes.KEY_BACKSPACE,

    'VOLUMEUP': ecodes.KEY_VOLUMEUP,
    'VOLUMEDOWN': ecodes.KEY_VOLUMEDOWN,
}

mouse_key_name_to_key_code_table = {
    'LEFT': ecodes.BTN_LEFT,
    'RIGHT': ecodes.BTN_RIGHT,
    'MIDDLE': ecodes.BTN_MIDDLE,
    '1': ecodes.BTN_LEFT,
    '2': ecodes.BTN_RIGHT,
    '3': ecodes.BTN_MIDDLE,
}


def mouse_key_name_to_key_code(mouse_key_name):
    return mouse_key_name_to_key_code_table[mouse_key_name]


def key_code_to_key_name(key_code):
    return key_code_to_key_name_table[key_code]


def key_name_to_key_code(name):
    return key_name_to_key_code_table[name]


def char_to_key_code(name):
    if name in char_to_key_code_table.keys():
        return char_to_key_code_table[name]
    else:
        return None

    pass


def char_to_key_code_modifier(name):
    if name in char_to_key_code_modifier_table.keys():
        return char_to_key_code_modifier_table[name]
    else:
        return MODIFIER_NONE

    pass


def parse_modifiers(modifier):
    modifiers = []

    if modifier is None:
        return modifiers

    if modifier & MODIFIER_LEFTSHIFT:
        modifiers.append(ecodes.KEY_LEFTSHIFT)
        pass

    if modifier & MODIFIER_LEFTALT:
        modifiers.append(ecodes.KEY_LEFTALT)
        pass

    if modifier & MODIFIER_LEFTCTRL:
        modifiers.append(ecodes.KEY_LEFTCTRL)
        pass

    if modifier & MODIFIER_LEFTMETA:
        modifiers.append(ecodes.KEY_LEFTMETA)
        pass

    if modifier & MODIFIER_RIGHTSHIFT:
        modifiers.append(ecodes.KEY_RIGHTSHIFT)
        pass

    if modifier & MODIFIER_RIGHTALT:
        modifiers.append(ecodes.KEY_RIGHTALT)
        pass

    if modifier & MODIFIER_RIGHTCTRL:
        modifiers.append(ecodes.KEY_RIGHTCTRL)
        pass

    if modifier & MODIFIER_RIGHTMETA:
        modifiers.append(ecodes.KEY_RIGHTMETA)
        pass

    return modifiers


def parse_modifier(modifier):
    if modifier is None:
        return None

    if modifier & MODIFIER_LEFTSHIFT:
        return ecodes.KEY_LEFTSHIFT

    if modifier & MODIFIER_LEFTALT:
        return ecodes.KEY_LEFTALT

    if modifier & MODIFIER_LEFTCTRL:
        return ecodes.KEY_LEFTCTRL

    if modifier & MODIFIER_LEFTMETA:
        return ecodes.KEY_LEFTMETA

    if modifier & MODIFIER_RIGHTSHIFT:
        return ecodes.KEY_RIGHTSHIFT

    if modifier & MODIFIER_RIGHTALT:
        return ecodes.KEY_RIGHTALT

    if modifier & MODIFIER_RIGHTCTRL:
        return ecodes.KEY_RIGHTCTRL

    if modifier & MODIFIER_RIGHTMETA:
        return ecodes.KEY_RIGHTMETA

    return None
