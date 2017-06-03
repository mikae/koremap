from action import Action
import os
import os.path
import keymapper
import sys


class ActionExecuteScript(Action):
    def __init__(self, pattern, shell_command, script_path):
        Action.__init__(self, pattern)

        self.__shell_command = shell_command
        self.__script_path = script_path
        pass

    @staticmethod
    def _check_program_exists(program_cmd):
        cmd = "which " + program_cmd
        val = os.system(cmd)

        if val == 0:
            return True
        else:
            return False
        pass

    @staticmethod
    def _check_file_exists(filepath):
        return os.path.exists(filepath)

    @staticmethod
    def _execute_script(shell_cmd, script_path):
        if not ActionExecuteScript._check_program_exists(shell_cmd):
            return

        if not ActionExecuteScript._check_file_exists(script_path):
            return

        pid = os.fork()
        if pid == 0:

            cmd = shell_cmd + " " + script_path
            os.system(cmd)
            sys.exit(0)
            pass
        elif pid > 0:
            return
        elif pid < 0:
            raise Exception()
        pass

    def on_action_start(self, modifiers=keymapper.MODIFIER_NONE):
        self._execute_script(self.__shell_command, self.__script_path)
        pass

    pass
