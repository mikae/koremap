from action import Action


class ActionProfileChange(Action):
    def __init__(self, pattern, conf, profile_from_name, profile_to_name):
        Action.__init__(self, pattern)

        self.__profile_from_name = profile_from_name
        self.__profile_to_name = profile_to_name
        self.__conf = conf
        pass

    def update(self, action_maker):
        profile_from = self.__conf.get_profile(self.__profile_from_name)
        profile_to = self.__conf.get_profile(self.__profile_to_name)

        action_maker.change_profile(profile_from, profile_to)
        pass

    pass
