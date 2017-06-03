# 2017.01.31 12:43:37 MSK
#Embedded file name: /home/data/Documents/Python/Jessy/src/core/_tokenizer.py
TOKEN_ID = 'ID'
TOKEN_NUMBER = 'NUMBER'
TOKEN_NEWLINE = 'NEWLINE'
TOKEN_SKIP = 'SKIP'
TOKEN_LEFTBRACE = 'LEFTBRACE'
TOKEN_RIGHTBRACE = 'RIGHTBRACE'
TOKEN_COMMA = 'COMMA'
configuration_keywords = 'alias'
configuration_token_specification = [(TOKEN_ID, '[A-Za-z_][a-zA-Z0-9_]*'),
 (TOKEN_NUMBER, '[0-9]+'),
 (TOKEN_NEWLINE, '\\n'),
 (TOKEN_SKIP, '[ \\t]'),
 (TOKEN_LEFTBRACE, '\\['),
 (TOKEN_RIGHTBRACE, '\\]'),
 (TOKEN_COMMA, ',')
]
# +++ okay decompyling _tokenizer.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.01.31 12:43:37 MSK
