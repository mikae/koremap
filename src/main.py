import sys
import os.path

from core.configuration import Configuration
from core.daemon import Daemon


def tracefunc(frame, event, arg, indent=[0]):
    if event == "call":
        indent[0] += 2
        print "-" * indent[0] + "> call function", frame.f_code.co_name
    elif event == "return":
        print "<" + "-" * indent[0], "exit function", frame.f_code.co_name
        indent[0] -= 2
    return tracefunc


def make_gen(args):
    for arg in args:
        yield arg


if __name__ == "__main__":
    # sys.settrace(tracefunc)

    gen = make_gen(sys.argv)

    configuration_path = None

    for arg in gen:
        if arg == '-c':
            conf_file = gen.next()

            if conf_file is not None:
                configuration_path = conf_file
                pass
            pass
        pass

    if configuration_path is None:
        xdg_config_home = os.getenv("XDG_CONFIG_HOME")
        if xdg_config_home is None or xdg_config_home == "":
            xdg_config_home = os.path.expandvars('$HOME/.config')
            pass

        if xdg_config_home is None:
            print 'Can\'t find configuration file'
            sys.exit(-1)
            pass

        configuration_path = os.path.join(
            xdg_config_home,
            "koremap/.koremaprc"
        )
        pass

    if not os.path.isfile(configuration_path):
        print "There is no configuration file with name: {}".format(
            configuration_path
        )
        sys.exit(0)
        pass

    f = open(configuration_path, 'r')
    text = f.read()

    conf = Configuration(text)
    daemon = Daemon(conf)
    daemon.start()

    pass
