from action import Action
import event_sender
import keymapper


# todo rename
class ActionMouseClick(Action):
    def __init__(self, pattern, mouse_key):
        Action.__init__(self, pattern)
        self.__mouse_key = mouse_key
        pass

    def on_action_start(self, modifiers=keymapper.MODIFIER_NONE):
        event_sender.instance().send_mouse_click(self.__mouse_key)
        pass

    def on_action_end(self):
        pass
    pass
