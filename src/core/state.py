class State:
    def __init__(self, is_end_state):
        self._is_end_state = is_end_state
        self._triggers = {}
        pass

    def is_end_state(self):
        return self._is_end_state

    def add_state(self, trigger, new_state):
        assert isinstance(new_state, State)

        self._triggers[trigger] = new_state
        pass

    def get_state(self, trigger):
        if trigger in self._triggers:
            return self._triggers[trigger]
        else:
            return None

    def remove_state(self, trigger):
        if trigger in self._triggers:
            self._triggers[trigger] = None
            del self._triggers[trigger]
            pass
        pass

    def clear_states(self):
        self._triggers.clear()
        pass
