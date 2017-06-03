from action import Action
import event_sender
import keymapper


class ActionPrint(Action):
    def __init__(self, pattern, text):
        Action.__init__(self, pattern)
        self.__text = text
        pass

    def _type(self):
        event_sender.instance().send_string(self.__text)
        pass

    def on_action_start(self, modifiers=keymapper.MODIFIER_NONE):
        self._type()
        pass

    pass
