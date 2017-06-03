from action_mouse_release import ActionMouseRelease


class MacroActionMouseRelease(ActionMouseRelease):
    def __init__(self, mouse_key):
        ActionMouseRelease.__init__(self, [], mouse_key)
        pass
    pass
