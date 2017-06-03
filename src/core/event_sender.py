import evdev
import evdev.ecodes as ecodes
import time
from pymouse import PyMouse

import keymapper


class EventSender:
    def __init__(self):
        self.__output_device = evdev.UInput()
        self.__pymouse = PyMouse()
        pass

    def send_string(self, string, sleep_fraction=10, sleep_time=0.001):
        length = len(string)

        for i in range(length):
            key_code = keymapper.char_to_key_code(string[i])
            key_code_modifier_flags = keymapper.char_to_key_code_modifier(
                string[i]
            )
            key_code_modifier = keymapper.parse_modifiers(
                key_code_modifier_flags
            )

            if key_code is not None:
                for j in range(len(key_code_modifier)):
                    self.__output_device.write(
                        ecodes.EV_KEY, key_code_modifier[j], 1
                    )
                    pass

                self.__output_device.write(ecodes.EV_KEY, key_code, 1)
                self.__output_device.write(ecodes.EV_KEY, key_code, 0)

                for j in range(len(key_code_modifier)):
                    self.__output_device.write(
                        ecodes.EV_KEY, key_code_modifier[j], 0
                    )
                    pass

                self.__output_device.syn()
                pass

            if i % sleep_fraction == 0:
                time.sleep(sleep_time)
                pass
            pass
        pass

    def send_key_press_and_release(self, key_code, modifiers):
        self.send_key_press(key_code, modifiers)
        self.send_key_release(key_code, modifiers)
        self.syn(key_code, modifiers)
        pass

    def send_key_press(self, key_code):
        self.__output_device.write(ecodes.EV_KEY, key_code, 1)
        pass

    def send_key_release(self, key_code):
        self.__output_device.write(ecodes.EV_KEY, key_code, 0)
        pass

    def syn(self):
        self.__output_device.syn()
        pass

    def send_mouse_click(self, mouse_button):
        self.__output_device.write(ecodes.EV_KEY, mouse_button, 1)
        self.__output_device.write(ecodes.EV_KEY, mouse_button, 0)
        self.__output_device.syn()
        pass

    def send_mouse_move_to(self, x, y):
        self.__pymouse.move(x, y)
        pass

    def send_mouse_move_by(self, dx, dy):
        x, y = self.__pymouse.position()

        self.__pymouse.move(x + dx, y + dy)
        pass

    def send_mouse_release(self, mouse_button):
        self.__output_device.write(ecodes.EV_KEY, mouse_button, 0)
        self.__output_device.syn()
        pass

    def send_mouse_press(self, mouse_button):
        self.__output_device.write(ecodes.EV_KEY, mouse_button, 1)
        self.__output_device.syn()
        pass

    pass


event_sender = EventSender()


def instance():
    return event_sender
