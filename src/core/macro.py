from action import Action

import os
import sys


class Macro:
    def __init__(self, macro_name):
        self.__actions = []
        self.__macro_name = macro_name
        pass

    def _execute_in_this_thread(self):
        for action in self.__actions:
            action.on_action_start()
            action.on_action_end()
            pass
        pass

    def _execute_in_other_thread(self):
        pid = os.fork()

        if pid < 0:
            raise Exception()

        if pid == 0:
            # child
            # do work in child thread

            self._execute_in_this_thread()

            sys.exit(0)
            pass
        else:
            # parent
            # continue to the main work
            return
            pass
        pass

    def get_macro_name(self):
        return self.__macro_name

    def add_action(self, action):
        assert isinstance(action, Action)

        self.__actions.append(action)
        pass

    def get_actions(self):
        return self.__actions

    def execute(self, other_thread=False):
        if other_thread:
            self._execute_in_other_thread()
            pass
        else:
            self._execute_in_this_thread()
            pass
        pass
    pass
