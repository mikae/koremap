from action_mouse_click import ActionMouseClick


class MacroActionMouseClick(ActionMouseClick):
    def __init__(self, mouse_key):
        ActionMouseClick.__init__(self, [], mouse_key)
        pass
    pass
