from configuration_tokenizer import ConfigurationTokenizer
import configuration_tokenizer as ct
import keymapper
import pattern
from profile import Profile

from macro import Macro

from action_execute import ActionExecute
from action_print import ActionPrint
from action_play import ActionPlay
from action_execute_script import ActionExecuteScript

from action_key_click import ActionKeyClick
from action_key_press import ActionKeyPress
from action_key_release import ActionKeyRelease

from action_mouse_click import ActionMouseClick
from action_mouse_press import ActionMousePress
from action_mouse_release import ActionMouseRelease

from action_profile_change import ActionProfileChange
from action_profile_select import ActionProfileSelect
from action_profile_deselect import ActionProfileDeselect

from macro_action_sleep import MacroActionSleep
from macro_action_execute import MacroActionExecute
from macro_action_print import MacroActionPrint
from macro_action_play import MacroActionPlay
from macro_action_execute_script import MacroActionExecuteScript
from action_mouse_move_absolute import ActionMouseMoveAbsolute
from action_mouse_move_relative import ActionMouseMoveRelative

from macro_action_key_click import MacroActionKeyClick
from macro_action_key_press import MacroActionKeyPress
from macro_action_key_release import MacroActionKeyRelease

from macro_action_mouse_click import MacroActionMouseClick
from macro_action_mouse_press import MacroActionMousePress
from macro_action_mouse_release import MacroActionMouseRelease

from macro_action_mouse_move_absolute import MacroActionMouseMoveAbsolute
from macro_action_mouse_move_relative import MacroActionMouseMoveRelative


class Configuration:
    def __init__(self, text):
        self.__key_aliases = {}
        self.__device_aliases = {}
        self.__devices = {}
        self.__profiles = {}
        self.__macrosses = {}
        self.__default_profiles = []

        self._parse_from_text(text)
        pass

    @staticmethod
    def _parse_string(s):
        assert isinstance(s, str)

        first_index = 0
        last_index = len(s) - 1

        if s[first_index] == '\"':
            first_index = 1
            pass

        if s[last_index] == '\"':
            last_index = -1
            pass

        return s[first_index:last_index]

    def _parse_from_text(self, text):
        tokenizer = ConfigurationTokenizer()
        gen = tokenizer.tokenize(text)
        for token in gen:
            type = token[0]

            if type == ct.KEYWORD_ALIAS:
                alias_key, device_index, key_code = self._parse_alias(gen)

                if device_index is not None and key_code is not None:
                    alias_value = pattern.get_pattern(device_index, key_code)

                    self._add_key_alias(alias_key, alias_value)
                    pass
                pass
            elif type == ct.KEYWORD_KEYBOARD:
                token_path = gen.next()
                assert token_path[0] == ct.TOKEN_ID

                token_as = gen.next()
                assert token_as[0] == ct.KEYWORD_AS

                token_device_alias = gen.next()
                assert token_device_alias[0] == ct.TOKEN_ID

                self._add_device_alias(token_device_alias[1], token_path[1])
                self._add_device(token_path[1])
                pass
            elif type == ct.KEYWORD_MACRO:
                token_macro_name = gen.next()
                assert token_macro_name[0] == ct.TOKEN_ID

                token_lfb = gen.next()
                assert token_lfb[0] == ct.TOKEN_LEFTFIGUREBRACE

                macro_name = token_macro_name[1]
                macro = Macro(macro_name)

                macro_token = gen.next()
                while macro_token[0] != ct.TOKEN_RIGHTFIGUREBRACE:
                    action, macro_token = self._parse_macro_action(
                        macro_token,
                        gen
                    )
                    if action is not None:
                        macro.add_action(action)
                        pass

                    macro_token = gen.next()
                    pass

                self._add_macro(macro)
                pass
            elif type == ct.KEYWORD_PROFILE:
                token_profile_name = gen.next()
                assert token_profile_name[0] == ct.TOKEN_ID

                profile_name = token_profile_name[1]

                self._add_profile(profile_name)
                profile = self.get_profile(profile_name)

                profile_token = gen.next()
                assert profile_token[0] == ct.TOKEN_LEFTFIGUREBRACE

                while profile_token[0] != ct.TOKEN_RIGHTFIGUREBRACE:
                    profile_token = gen.next()

                    if profile_token[0] == ct.KEYWORD_BIND:
                        profile_token = gen.next()
                        patterns, profile_token = self._parse_patterns(
                            profile_token,
                            gen
                        )
                        if patterns is None:
                            raise Exception()

                        action, profile_token = self._parse_action(
                                                    profile_token,
                                                    patterns,
                                                    gen
                        )

                        print profile_token

                        if action is None:
                            raise Exception()

                        profile.add_action(action)

                        pass
                    pass
                pass
            elif type == ct.KEYWORD_SELECT:
                profile_name_token = gen.next()
                assert profile_name_token[0] == ct.TOKEN_ID

                profile_name = profile_name_token[1]

                self.__default_profiles.append(profile_name)
                pass

            pass
        pass

    def _parse_macro_action(self, macro_token, gen):
        action = None
        if macro_token[0] == ct.KEYWORD_PRINT:
            token_text = gen.next()
            assert token_text[0] == ct.TOKEN_STRING

            text = Configuration._parse_string(token_text[1])

            action = MacroActionPrint(text)
            pass
        elif macro_token[0] == ct.KEYWORD_EXECUTE:
            token_cmd = gen.next()
            assert token_cmd[0] == ct.TOKEN_STRING

            cmd = Configuration._parse_string(token_cmd[1])

            action = MacroActionExecute(cmd)
            pass
        elif macro_token[0] == ct.KEYWORD_KEY:
            token_action_type = gen.next()

            token_key_name = gen.next()
            assert token_key_name[0] == ct.TOKEN_ID

            key_name = token_key_name[1]
            key_code = keymapper.key_name_to_key_code(key_name)

            if token_action_type[0] == ct.KEYWORD_PRESS:
                action = MacroActionKeyPress(key_code)
                pass
            elif token_action_type[0] == ct.KEYWORD_RELEASE:
                action = MacroActionKeyRelease(key_code)
                pass
            elif token_action_type[0] == ct.KEYWORD_CLICK:
                action = MacroActionKeyClick(key_code)
                pass
            else:
                raise Exception()
            pass
        elif macro_token[0] == ct.KEYWORD_MOUSE:
            token_action_type = gen.next()

            if token_action_type[0] == ct.KEYWORD_PRESS:
                token_mouse_key_name = gen.next()
                assert token_mouse_key_name[0] == ct.TOKEN_ID

                mouse_key_name = token_mouse_key_name[1]
                mouse_key_code = keymapper.mouse_key_name_to_key_code(
                    mouse_key_name
                )
                action = MacroActionMousePress(mouse_key_code)
                pass
            elif token_action_type[0] == ct.KEYWORD_RELEASE:
                token_mouse_key_name = gen.next()
                assert token_mouse_key_name[0] == ct.TOKEN_ID

                mouse_key_name = token_mouse_key_name[1]
                mouse_key_code = keymapper.mouse_key_name_to_key_code(
                    mouse_key_name
                )
                action = MacroActionMouseRelease(mouse_key_code)
                pass
            elif token_action_type[0] == ct.KEYWORD_CLICK:
                token_mouse_key_name = gen.next()
                assert token_mouse_key_name[0] == ct.TOKEN_ID

                mouse_key_name = token_mouse_key_name[1]
                mouse_key_code = keymapper.mouse_key_name_to_key_code(
                    mouse_key_name
                )
                action = MacroActionMouseClick(mouse_key_code)
                pass
            elif token_action_type[0] == ct.KEYWORD_MOVE:
                token_move_type = gen.next()

                token_x_coord = gen.next()
                assert token_x_coord[0] == ct.TOKEN_ID

                token_y_coord = gen.next()
                assert token_y_coord[0] == ct.TOKEN_ID

                x = int(token_x_coord[1])
                y = int(token_y_coord[1])

                if token_move_type[0] == ct.KEYWORD_POLAR:
                    pass
                elif token_move_type[0] == ct.KEYWORD_ABSOLUTE:
                    action = MacroActionMouseMoveAbsolute(x, y)
                    pass
                elif token_move_type[0] == ct.KEYWORD_RELATIVE:
                    action = MacroActionMouseMoveRelative(x, y)
                    pass
                else:
                    raise Exception()
                pass
            else:
                raise Exception()
            pass
        elif macro_token[0] == ct.KEYWORD_PLAY:
            token_macro_name = gen.next()
            assert token_macro_name[0] == ct.TOKEN_ID

            macro_name = token_macro_name[1]
            macro = self.get_macro(macro_name)

            action = MacroActionPlay(macro)
            pass
        elif macro_token[0] == ct.KEYWORD_SLEEP:
            token_sleep_time = gen.next()
            assert token_sleep_time[0] == ct.TOKEN_ID

            sleep_time = int(token_sleep_time[1])

            action = MacroActionSleep(sleep_time)
            pass
        elif macro_token[0] == ct.KEYWORD_SCRIPT:
            token_shell_cmd = gen.next()
            assert token_shell_cmd[0] == ct.TOKEN_STRING

            token_script_path = gen.next()
            assert token_script_path[0] == ct.TOKEN_STRING

            shell_cmd = Configuration._parse_string(token_shell_cmd[1])
            script_path = Configuration._parse_string(token_script_path[1])

            action = MacroActionExecuteScript(shell_cmd, script_path)
            pass
        else:
            raise Exception()

        return action, macro_token

    def _parse_alias(self, gen):
        token_lsb = gen.next()
        assert token_lsb[0] == ct.TOKEN_LEFTSQUAREBRACE

        token_device_name = gen.next()
        assert token_device_name[0] == ct.TOKEN_ID

        token_key_name = gen.next()
        assert token_key_name[0] == ct.TOKEN_ID

        token_rsb = gen.next()
        assert token_rsb[0] == ct.TOKEN_RIGHTSQUAREBRACE

        token_as = gen.next()
        assert token_as[0] == ct.KEYWORD_AS

        token_alias = gen.next()
        assert token_alias[0] == ct.TOKEN_ID

        device_name = token_device_name[1]
        device_path = self.get_device_alias(device_name)
        device_index = self.get_device_index(device_path)

        key_name = token_key_name[1]
        key_code = keymapper.key_name_to_key_code(key_name)

        alias_key = token_alias[1]

        return alias_key, device_index, key_code

    def _parse_patterns(self, profile_token, gen):
        patterns = []

        while profile_token[0] != ct.KEYWORD_DO:
            if profile_token[0] == ct.TOKEN_LEFTSQUAREBRACE:
                token_device_name = gen.next()
                assert token_device_name[0] == ct.TOKEN_ID

                token_key_name = gen.next()
                assert token_key_name[0] == ct.TOKEN_ID

                rsb = gen.next()
                assert rsb[0] == ct.TOKEN_RIGHTSQUAREBRACE

                device_name = token_device_name[1]
                device_path =\
                    self.get_device_alias(device_name)
                device_index =\
                    self.get_device_index(device_path)

                key_name = token_key_name[1]
                key_code =\
                    keymapper.key_name_to_key_code(key_name)

                if (key_code is not None
                        and key_name is not None):
                    pat = pattern.get_pattern(device_index,
                                              key_code)
                    patterns.append(pat)
                    pass
                else:
                    raise Exception()

                profile_token = gen.next()
                pass
            elif profile_token[0] == ct.TOKEN_LEFTARROW:
                token_alias = gen.next()
                assert token_alias[0] == ct.TOKEN_ID

                token_right_arrow = gen.next()
                assert token_right_arrow[0] ==\
                    ct.TOKEN_RIGHTARROW

                alias = token_alias[1]
                pat = self.get_key_alias(alias)
                if pat is not None:
                    patterns.append(pat)
                    pass
                else:
                    raise Exception()

                profile_token = gen.next()
                pass
            elif profile_token[0] == ct.TOKEN_ID:
                aliases = profile_token[1]
                for alias in aliases:
                    pat = self.get_key_alias(alias)
                    if pat is not None:
                        patterns.append(pat)
                        pass
                    else:
                        raise Exception()
                    pass

                profile_token = gen.next()
                pass
            else:
                raise Exception()
            pass

# skip do
        profile_token = gen.next()

        return patterns, profile_token

    def _parse_action(self, profile_token, patterns, gen):
        action = None
        if profile_token[0] == ct.KEYWORD_PRINT:
            token_text = gen.next()
            assert token_text[0] == ct.TOKEN_STRING

            text = Configuration._parse_string(token_text[1])

            action = ActionPrint(patterns, text)
            pass
        elif profile_token[0] == ct.KEYWORD_EXECUTE:
            token_cmd = gen.next()
            assert token_cmd[0] == ct.TOKEN_STRING

            cmd = Configuration._parse_string(token_cmd[1])

            action = ActionExecute(patterns, cmd)
            pass
        elif profile_token[0] == ct.KEYWORD_KEY:
            token_action_type = gen.next()

            token_key_name = gen.next()
            assert token_key_name[0] == ct.TOKEN_ID

            key_name = token_key_name[1]
            key_code = keymapper.key_name_to_key_code(key_name)

            if token_action_type[0] == ct.KEYWORD_PRESS:
                action = ActionKeyPress(patterns, key_code)
                pass
            elif token_action_type[0] == ct.KEYWORD_RELEASE:
                action = ActionKeyRelease(patterns, key_code)
                pass
            elif token_action_type[0] == ct.KEYWORD_CLICK:
                action = ActionKeyClick(patterns, key_code)
                pass
            else:
                raise Exception()

            pass
        elif profile_token[0] == ct.KEYWORD_MOUSE:
            token_action_type = gen.next()

            if token_action_type[0] == ct.KEYWORD_PRESS:
                token_mouse_key_name = gen.next()
                assert token_mouse_key_name[0] == ct.TOKEN_ID

                mouse_key_name = token_mouse_key_name[1]
                mouse_key_code = keymapper.mouse_key_name_to_key_code(
                    mouse_key_name
                )
                action = ActionMousePress(patterns, mouse_key_code)
                pass
            elif token_action_type[0] == ct.KEYWORD_RELEASE:
                token_mouse_key_name = gen.next()
                assert token_mouse_key_name[0] == ct.TOKEN_ID

                mouse_key_name = token_mouse_key_name[1]
                mouse_key_code = keymapper.mouse_key_name_to_key_code(
                    mouse_key_name
                )
                action = ActionMouseRelease(patterns, mouse_key_code)
                pass
            elif token_action_type[0] == ct.KEYWORD_CLICK:
                token_mouse_key_name = gen.next()
                assert token_mouse_key_name[0] == ct.TOKEN_ID

                mouse_key_name = token_mouse_key_name[1]
                mouse_key_code = keymapper.mouse_key_name_to_key_code(
                    mouse_key_name
                )
                action = ActionMouseClick(patterns, mouse_key_code)
                pass
            elif token_action_type[0] == ct.KEYWORD_MOVE:
                token_move_type = gen.next()

                token_x_coord = gen.next()
                assert token_x_coord[0] == ct.TOKEN_ID

                token_y_coord = gen.next()
                assert token_y_coord[0] == ct.TOKEN_ID

                x = int(token_x_coord[1])
                y = int(token_y_coord[1])

                if token_move_type[0] == ct.KEYWORD_POLAR:
                    pass
                elif token_move_type[0] == ct.KEYWORD_ABSOLUTE:
                    action = ActionMouseMoveAbsolute(patterns, x, y)
                    pass
                elif token_move_type[0] == ct.KEYWORD_RELATIVE:
                    action = ActionMouseMoveRelative(patterns, x, y)
                    pass
                else:
                    raise Exception()
                pass
            else:
                raise Exception()
            pass
        elif profile_token[0] == ct.KEYWORD_PROFILE:
            token_profile_change_type = gen.next()

            if token_profile_change_type[0] == ct.KEYWORD_SELECT:
                token_profile = gen.next()
                assert token_profile[0] == ct.TOKEN_ID

                profile_name = token_profile[1]

                action = ActionProfileSelect(patterns, self, profile_name)

                pass
            elif token_profile_change_type[0] == ct.KEYWORD_DESELECT:
                token_profile = gen.next()
                assert token_profile[0] == ct.TOKEN_ID

                profile_name = token_profile[1]

                action = ActionProfileDeselect(patterns, self, profile_name)
                pass
            elif token_profile_change_type[0] == ct.KEYWORD_CHANGE:
                token_profile_from = gen.next()
                assert token_profile_from[0] == ct.TOKEN_ID

                token_profile_to = gen.next()
                assert token_profile_to[0] == ct.TOKEN_ID

                profile_from_name = token_profile_from[1]
                profile_to_name = token_profile_to[1]

                action = ActionProfileChange(
                    patterns,
                    self,
                    profile_from_name,
                    profile_to_name
                )
                pass
            else:
                raise Exception()
            pass
        elif profile_token[0] == ct.KEYWORD_PLAY:
            token_macro_name = gen.next()
            assert token_macro_name[0] == ct.TOKEN_ID

            macro_name = token_macro_name[1]
            macro = self.get_macro(macro_name)
            if macro is not None:
                action = ActionPlay(patterns, macro)
                pass
            else:
                raise Exception()
            pass
        elif profile_token[0] == ct.KEYWORD_SCRIPT:
            token_shell_cmd = gen.next()
            assert token_shell_cmd[0] == ct.TOKEN_STRING

            token_script_path = gen.next()
            assert token_script_path[0] == ct.TOKEN_STRING

            shell_cmd = Configuration._parse_string(token_shell_cmd[1])
            script_path = Configuration._parse_string(token_script_path[1])
            action = ActionExecuteScript(patterns, shell_cmd, script_path)
            pass

        return action, profile_token

    def _add_macro(self, macro):
        self.__macrosses[macro.get_macro_name()] = macro
        pass

    def get_macro(self, macro_name):
        if macro_name in self.__macrosses:
            return self.__macrosses[macro_name]

        return None

    def get_macro_names(self):
        return self.__macrosses.keys()

    def _add_profile(self, profile_name):
        self.__profiles[profile_name] = Profile(profile_name)
        pass

    def get_profile_names(self):
        return self.__profiles.keys()

    def get_profile(self, profile_name):
        if profile_name in self.__profiles.keys():
            return self.__profiles[profile_name]

        return None

    def _add_device_alias(self, device_name, device_path):
        print "added device alias {} = {}".format(device_name,
                                                  device_path)
        self.__device_aliases[device_name] = device_path
        pass

    def get_device_alias(self, device_name):
        if device_name in self.__device_aliases:
            return self.__device_aliases[device_name]

        return None

    def _add_device(self, device_path):
        print "added device {}".format(device_path)
        self.__devices[device_path] = len(self.__devices)
        pass

    def get_device_index(self, device_path):
        if device_path in self.__devices:
            return self.__devices[device_path]

        return None

    def get_device_paths(self):
        return self.__devices.keys()

    def _add_key_alias(self, alias_key, alias_value):
        print "added key alias {} = {}".format(alias_key, alias_value)

        self.__key_aliases[alias_key] = alias_value
        pass

    def get_key_alias(self, alias_key):
        if alias_key in self.__key_aliases:
            return self.__key_aliases[alias_key]

        return None

    def get_default_profiles(self):
        return self.__default_profiles

    pass
