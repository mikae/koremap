from action import Action


class Profile:
    def __init__(self, profile_name):
        self.__profile_name = profile_name
        self.__actions = []
        pass

    def add_action(self, action):
        assert isinstance(action, Action)
        self.__actions.append(action)
        pass

    def get_actions(self):
        return self.__actions
    pass
