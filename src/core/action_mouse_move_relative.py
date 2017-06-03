from action import Action
import keymapper
import event_sender


class ActionMouseMoveRelative(Action):
    def __init__(self, pattern, dx, dy):
        Action.__init__(self, pattern)

        assert isinstance(dx, int)
        assert isinstance(dy, int)

        self.__dx = dx
        self.__dy = dy
        pass

    def on_action_start(self, modifiers=keymapper.MODIFIER_NONE):
        event_sender.instance().send_mouse_move_by(self.__dx, self.__dy)
        pass

    pass
