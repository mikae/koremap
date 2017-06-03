from action_mouse_press import ActionMousePress


class MacroActionMousePress(ActionMousePress):
    def __init__(self, mouse_key):
        ActionMousePress.__init__(self, [], mouse_key)
        pass
    pass
