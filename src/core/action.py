import keymapper


class Action:
    def __init__(self, pattern):
        self.__pattern = pattern
        pass

    def get_pattern(self):
        return self.__pattern

    def on_action_start(self, modifiers=keymapper.MODIFIER_NONE):
        pass

    def update(self, action_maker):
        pass

    def on_action_end(self):
        pass

    pass
