from action import Action

import time


class MacroActionSleep(Action):
    def __init__(self, sleep_value):
        Action.__init__(self, [])
        self.__sleep_value = sleep_value
        pass

    def _sleep(self):
        time.sleep(self.__sleep_value * 0.001)
        pass

    def on_action_start(self):
        self._sleep()
        pass
    pass
