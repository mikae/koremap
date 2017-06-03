from action import Action
import keymapper

import os
import sys


class ActionExecute(Action):
    def __init__(self, pattern, cmd):
        Action.__init__(self, pattern)
        self.__cmd = cmd

        if self.__cmd is None:
            raise Exception()
        pass

    def _execute(self, cmd):
        pid = os.fork()

        if pid == 0:
            os.system(cmd)
            sys.exit()
        elif pid > 0:
            return
        else:
            raise Exception()
            pass
        pass

    def on_action_start(self, modifiers=keymapper.MODIFIER_NONE):
        self._execute(self.__cmd)
        pass

    pass
