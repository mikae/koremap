from action_key_press import ActionKeyPress


class MacroActionKeyPress(ActionKeyPress):
    def __init__(self, key):
        ActionKeyPress.__init__(self, [], key)
        pass
