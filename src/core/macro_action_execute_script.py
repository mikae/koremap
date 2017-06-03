from action_execute_script import ActionExecuteScript


class MacroActionExecuteScript(ActionExecuteScript):
    def __init__(self, shell_command, script_path):
        ActionExecuteScript.__init__(self, [], shell_command, script_path)
        pass
    pass
