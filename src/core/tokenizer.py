# 2017.01.31 12:52:27 MSK
#Embedded file name: /home/data/Documents/Python/Jessy/src/core/tokenizer.py
import re
import collections
import _tokenizer
token_yield_format = collections.namedtuple('Token', ['type',
 'value',
 'line',
 'column'])

class Tokenizer:

    def __init__(self, keywords, token_specification):
        self.__keywords = keywords
        self.__token_specification = token_specification
        self.__token_reg = '|'.join(('(?P<%s>%s)' % pair for pair in token_specification))
        self.__token_match = re.compile(self.__token_reg).match

    def tokenize(self, s):
        line = 1
        pos = line_start = 0
        mo = self.__token_match(s)
        while mo is not None:
            typ = mo.lastgroup
            if typ == 'NEWLINE':
                line_start = pos
                line += 1
            elif typ != 'SKIP':
                val = mo.group(typ)
                if typ == 'ID' and val in self.__keywords:
                    typ = val
                yield token_yield_format(typ, val, line, mo.start() - line_start)
            pos = mo.end()
            mo = self.__token_match(s, pos)

        if pos != len(s):
            raise RuntimeError('Unexpected character %r on line %d' % (s[pos], line))


class ConfigurationTokenizer(Tokenizer):

    def __init__(self):
        Tokenizer.__init__(self, keywords=_tokenizer.configuration_keywords, token_specification=_tokenizer.configuration_token_specification)
# +++ okay decompyling tokenizer.pyc
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.01.31 12:52:27 MSK
