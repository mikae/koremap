from action import Action
from macro import Macro
import keymapper


class ActionPlay(Action):
    def __init__(self, pattern, macro):
        Action.__init__(self, pattern)

        assert isinstance(macro, Macro)
        self.__macro = macro
        pass

    def on_action_start(self, modifiers=keymapper.MODIFIER_NONE):
        self.__macro.execute(True)
        pass

    def get_macro(self):
        return self.__macro

    pass
