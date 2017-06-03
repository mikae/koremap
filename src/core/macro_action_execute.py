from action_execute import ActionExecute


class MacroActionExecute(ActionExecute):
    def __init__(self, cmd):
        ActionExecute.__init__(self, [], cmd)
        pass
    pass
