# import evdev
import evdev.ecodes as ecodes

from state import State
from state_machine import StateMachine
from configuration import Configuration
import keymapper
import key_sender
import pattern


class ActionMaker:
    def __init__(self, conf):
        assert isinstance(conf, Configuration)
        profile_to_end_state_to_action = {}
        profile_to_state_machine = {}
        selected_actions = {}

        for profile_name in conf.get_profile_names():
            profile = conf.get_profile(profile_name)
            profile_to_end_state_to_action[profile] = {}

            stm, end_state_to_action = self._ini_state_machine_from_profile(
                conf, profile
            )

            stm.add_achieved_end_state_achieved_listener(self._listener)

            profile_to_state_machine[profile] = stm
            profile_to_end_state_to_action[profile] = end_state_to_action

            selected_actions[profile] = {}
            pass

        selected_profiles = []

        for profile_name in conf.get_default_profiles():
            profile = conf.get_profile(profile_name)
            selected_profiles.append(profile)
            pass

        self.__selected_profiles = selected_profiles
        self.__selected_actions = selected_actions
        self.__modifiers = keymapper.MODIFIER_NONE
        self.__conf = conf
        self.__profile_to_end_state_to_action =\
            profile_to_end_state_to_action
        self.__profile_to_state_machine = profile_to_state_machine
        self.__modifiers = keymapper.MODIFIER_NONE
        self.__excited_action = None

        self._ini_modifier_patterns(conf)
        pass

    def _ini_modifier_patterns(self, conf):
        modifier_left_shift_pattern = conf.get_key_alias("LEFTSHIFT")
        modifier_left_ctrl_pattern = conf.get_key_alias("LEFTCTRL")
        modifier_left_alt_pattern = conf.get_key_alias("LEFTALT")
        modifier_left_meta_pattern = conf.get_key_alias("LEFTMETA")

        modifier_right_shift_pattern = conf.get_key_alias("RIGHTSHIFT")
        modifier_right_ctrl_pattern = conf.get_key_alias("RIGHTCTRL")
        modifier_right_alt_pattern = conf.get_key_alias("RIGHTALT")
        modifier_right_meta_pattern = conf.get_key_alias("RIGHTMETA")

        modifier_patterns = {}

        ActionMaker._add_to_dict_if_key_not_none(
            modifier_patterns,
            modifier_left_shift_pattern,
            ecodes.KEY_LEFTSHIFT
        )

        ActionMaker._add_to_dict_if_key_not_none(
            modifier_patterns,
            modifier_right_shift_pattern,
            ecodes.KEY_RIGHTSHIFT
        )

        ActionMaker._add_to_dict_if_key_not_none(
            modifier_patterns,
            modifier_left_meta_pattern,
            ecodes.KEY_LEFTMETA
        )

        ActionMaker._add_to_dict_if_key_not_none(
            modifier_patterns,
            modifier_right_meta_pattern,
            ecodes.KEY_RIGHTMETA
        )

        ActionMaker._add_to_dict_if_key_not_none(
            modifier_patterns,
            modifier_left_alt_pattern,
            ecodes.KEY_LEFTALT
        )

        ActionMaker._add_to_dict_if_key_not_none(
            modifier_patterns,
            modifier_right_alt_pattern,
            ecodes.KEY_RIGHTALT
        )

        ActionMaker._add_to_dict_if_key_not_none(
            modifier_patterns,
            modifier_left_ctrl_pattern,
            ecodes.KEY_LEFTCTRL
        )

        ActionMaker._add_to_dict_if_key_not_none(
            modifier_patterns,
            modifier_right_ctrl_pattern,
            ecodes.KEY_RIGHTCTRL
        )

        self.__modifier_patterns = modifier_patterns

        pass

    @staticmethod
    def _add_to_dict_if_key_not_none(dict, key, value):
        if key is not None:
            dict[key] = value
            pass
        pass

    @staticmethod
    def _ini_state_machine_from_profile(conf, profile):
        stm = StateMachine()
        end_state_to_action = {}

        for action in profile.get_actions():
            patterns = action.get_pattern()
            end_state = stm.make_states(patterns)

            end_state_to_action[end_state] = action
            pass

        return stm, end_state_to_action

    def _listener(self, end_state):
        assert isinstance(end_state, State)
        end_state_to_action = self.__profile_to_end_state_to_action[
            self.__selected_profile]
        action = end_state_to_action[end_state]

        self.__excited_action = action
        pass

    def excite(self, device_index, event_code, event_value):
        pat = pattern.get_pattern(device_index, event_code)

        if pat in self.__modifier_patterns:
            modifier_key_code = self.__modifier_patterns[pat]

            if event_value == 0:
                key_sender.instance().send_release(modifier_key_code)
                key_sender.instance().syn()
                pass
            elif event_value == 1:
                key_sender.instance().send_press(modifier_key_code)
                key_sender.instance().syn()
                pass

            pass
        else:
            if event_value == 1:
                for selected_profile in self.__selected_profiles:
                    self.__selected_profile = selected_profile
                    stm = self.__profile_to_state_machine[selected_profile]
                    stm.excite(pat)

                    if self.__excited_action is not None:
                        self.__selected_actions[selected_profile][
                            pat] = self.__excited_action

                        self.__excited_action.on_action_start(self.__modifiers)
                        self.__excited_action.update(self)

                        self.__excited_action = None
                        break
                        pass
                    pass
                pass
            elif event_value == 0:
                for selected_profile in self.__selected_profiles:
                    if pat in self.__selected_actions[selected_profile]:
                        self.__selected_actions[selected_profile][
                            pat].on_action_end()
                        self.__selected_actions[selected_profile][pat] = None
                        pass
                    pass
                pass

        pass

    def deselect_profile(self, profile):
        if profile not in self.__selected_profiles:
            self.__selected_profiles.remove(profile)
            pass
        pass

    def select_profile(self, profile):
        if profile not in self.__selected_profiles:
            self.__selected_profiles.append(profile)
            pass
        pass

    def change_profile(self, profile_from, profile_to):
        print profile_from
        if profile_from in self.__selected_profiles:
            self.__selected_profiles.remove(profile_from)
            self.__selected_profiles.append(profile_to)
            pass
        pass

    pass
