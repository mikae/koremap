from action_print import ActionPrint


class MacroActionPrint(ActionPrint):
    def __init__(self, text):
        ActionPrint.__init__(self, [], text)
    pass


