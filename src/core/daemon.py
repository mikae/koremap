import select
import traceback
import evdev
import evdev.ecodes as ecodes

from configuration import Configuration
from action_maker import ActionMaker


class Daemon:
    def __init__(self, conf):
        assert isinstance(conf, Configuration)

        self.__conf = conf
        pass

    @staticmethod
    def _create_devices(conf):
        devices = {}

        for device_path in conf.get_device_paths():
            device = evdev.InputDevice(device_path)
            devices[device_path] = device

            print "Created device: {}".format(device_path)
            pass

        return devices

    @staticmethod
    def _close_devices(devices):
        for device_path in devices.keys():
            devices[device_path].close()
            print "Closed device: {}".format(device_path)
            pass
        pass

    @staticmethod
    def _ungrab_devices(devices):
        for device_path in devices.keys():
            devices[device_path].ungrab()
            pass
        pass

    @staticmethod
    def _grab_devices(devices):
        for device_path in devices.keys():
            devices[device_path].grab()
            pass
        pass

    def start(self):
        conf = self.__conf
        am = ActionMaker(conf)

        devices = Daemon._create_devices(conf)
        fd_to_device_path = {devices[d].fd: d for d in devices.keys()}

        Daemon._grab_devices(devices)

        try:
            while True:
                r, w, x = select.select(fd_to_device_path, [], [])

                for fd in r:
                    device_path = fd_to_device_path[fd]
                    device = devices[device_path]
                    device_index = conf.get_device_index(device_path)

                    for event in device.read():
                        if event.type == ecodes.EV_KEY:
                            am.excite(device_index, event.code, event.value)
                            pass
                        pass
                    pass
                pass
        except KeyboardInterrupt:
            pass
        except Exception:
            traceback.print_exc()
            pass

        Daemon._ungrab_devices(devices)
        Daemon._close_devices(devices)
        pass
    pass
