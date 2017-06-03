from action_key_release import ActionKeyRelease


class MacroActionKeyRelease(ActionKeyRelease):
    def __init__(self, key):
        ActionKeyRelease.__init__(self, [], key)
        pass
    pass
