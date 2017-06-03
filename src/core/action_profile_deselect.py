from action import Action


class ActionProfileDeselect(Action):
    def __init__(self, pattern, conf, profile_name):
        Action.__init__(self, pattern)

        self.__profile_name = profile_name
        self.__conf = conf
        pass

    def update(self, action_maker):
        profile = self.__conf.get_profile(self.__profile_name)

        action_maker.deselect(profile)
        pass

    pass
