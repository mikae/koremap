from action_key_click import ActionKeyClick


class MacroActionKeyClick(ActionKeyClick):
    def __init__(self, key):
        ActionKeyClick.__init__(self, [], key)
        pass
