from action_play import ActionPlay


class MacroActionPlay(ActionPlay):
    def __init__(self, macro):
        ActionPlay.__init__(self, [], macro)
        pass

    def on_action_start(self):
        self.get_macro().execute(False)
        pass
    pass
