from tokenizer import Tokenizer

TOKEN_STRING = 'STRING'
TOKEN_ID = 'ID'
TOKEN_PATH = 'PATH'
TOKEN_NEWLINE = 'NEWLINE'
TOKEN_SKIP = 'SKIP'
TOKEN_LEFTSQUAREBRACE = 'LEFTSQUAREBRACE'
TOKEN_RIGHTSQUAREBRACE = 'RIGHTSQUAREBRACE'
TOKEN_LEFTFIGUREBRACE = "LEFTFIGUREBRACE"
TOKEN_RIGHTFIGUREBRACE = "RIGHTFTFIGUREBRACE"
TOKEN_LEFTARROW = "LEFTARROW"
TOKEN_RIGHTARROW = "RIGHTARROW"
TOKEN_AP = "AP"

KEYWORD_ALIAS = 'alias'
KEYWORD_KEYBOARD = 'keyboard'
KEYWORD_AS = 'as'
KEYWORD_PROFILE = 'profile'
KEYWORD_BIND = 'bind'
KEYWORD_PRINT = 'print'
KEYWORD_EXECUTE = 'execute'
KEYWORD_PRESS = 'press'
KEYWORD_PLAY = 'play'
KEYWORD_DO = 'do'
KEYWORD_MACRO = 'macro'
KEYWORD_SLEEP = 'sleep'
KEYWORD_SELECT = 'select'
KEYWORD_SCRIPT = 'script'
KEYWORD_KEY = 'key'
KEYWORD_CLICK = 'click'
KEYWORD_PRESS = 'press'
KEYWORD_RELEASE = 'release'
KEYWORD_MOUSE = 'mouse'
KEYWORD_MOVE = 'move'
KEYWORD_ABSOLUTE = 'absolute'
KEYWORD_RELATIVE = 'relative'
KEYWORD_POLAR = 'polar'
KEYWORD_CHANGE = 'change'
KEYWORD_DESELECT = 'deselect'

configuration_keywords = (
    KEYWORD_ALIAS,
    KEYWORD_KEYBOARD,
    KEYWORD_AS,
    KEYWORD_PROFILE,
    KEYWORD_BIND,
    KEYWORD_PRINT,
    KEYWORD_PRESS,
    KEYWORD_EXECUTE,
    KEYWORD_PLAY,
    KEYWORD_DO,
    KEYWORD_MACRO,
    KEYWORD_SLEEP,
    KEYWORD_SELECT,
    KEYWORD_DESELECT,
    KEYWORD_SCRIPT,
    KEYWORD_KEY,
    KEYWORD_CLICK,
    KEYWORD_PRESS,
    KEYWORD_RELEASE,
    KEYWORD_MOUSE,
    KEYWORD_ABSOLUTE,
    KEYWORD_RELATIVE,
    KEYWORD_POLAR,
    KEYWORD_MOVE,
    KEYWORD_CHANGE,
)

configuration_token_specification = [
    (TOKEN_ID,               r'[a-zA-Z0-9_\/\-]+|[\[\]\\\/\,\.\'\-\=\;]'),
    (TOKEN_STRING,           r'"[^"]*"'),
    (TOKEN_NEWLINE,          r'\n'),
    (TOKEN_SKIP,             r'[ \t]'),
    (TOKEN_LEFTSQUAREBRACE,  r'\('),
    (TOKEN_RIGHTSQUAREBRACE, r'\)'),
    (TOKEN_LEFTFIGUREBRACE,  r'\{'),
    (TOKEN_RIGHTFIGUREBRACE, r'\}'),
    (TOKEN_LEFTARROW,        r'\<'),
    (TOKEN_RIGHTARROW,       r'\>'),
    (TOKEN_AP,               r'"'),
]


class ConfigurationTokenizer(Tokenizer):
    def __init__(self):
        Tokenizer.__init__(
            self,
            keywords=configuration_keywords,
            token_specification=configuration_token_specification
        )
        pass
    pass
