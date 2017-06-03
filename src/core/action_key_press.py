from action import Action
import event_sender
import keymapper


# todo rename
class ActionKeyPress(Action):
    def __init__(self, pattern, key):
        Action.__init__(self, pattern)
        self.__key = key
        pass

    def on_action_start(self, modifiers=keymapper.MODIFIER_NONE):
        event_sender.instance().send_key_press(self.__key)
        event_sender.instance().syn()
        pass

    def on_action_end(self):
        pass
    pass
