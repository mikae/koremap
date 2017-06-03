import state


class StateMachine:
    def __init__(self):
        self._end_state_achieved_listeners = []

        self._begin_state = state.State(False)
        self._target_state = self._begin_state
        pass

    @staticmethod
    def _add_state(prev_state, trigger, is_end_state):
        """
        Adds new state for the trigger if it doesn't exist in prev_state
        :param prev_state: to which state we should add new state
        :param trigger: target trigger
        :param is_end_state: true if should be End state
        :return:
        """
        returned_state = prev_state.get_state(trigger)

        if returned_state is not None:
            temp_state = returned_state
            pass
        else:
            new_state = state.State(is_end_state)
            prev_state.add_state(trigger, new_state)
            temp_state = new_state
            pass

        return temp_state

    def _fire_end_state_event(self, end_state):
        for end_state_listener in self._end_state_achieved_listeners:
            end_state_listener(end_state)
            pass
        pass

    def make_states(self, triggers):
        assert triggers is not None

        count = len(triggers)
        temp_state = self._begin_state

        for i in range(count - 1):
            trigger = triggers[i]
            temp_state = StateMachine._add_state(temp_state, trigger, False)
            pass

        end_state = StateMachine._add_state(
            temp_state, triggers[count - 1], True
        )
        return end_state

    def add_achieved_end_state_achieved_listener(self, end_state_listener):
        assert end_state_listener is not None

        self._end_state_achieved_listeners.append(end_state_listener)
        pass

    def remove_end_state_listener(self, end_state_listener):
        self._end_state_achieved_listeners.remove(end_state_listener)
        pass

    def get_listener_count(self):
        return len(self._end_state_achieved_listeners)

    def excite(self, trigger):
        new_state = self._target_state.get_state(trigger)

        if new_state is None:
            new_state = self._begin_state
            pass
        else:
            if new_state.is_end_state():
                self._fire_end_state_event(new_state)
                new_state = self._begin_state
                pass
            pass

        self._target_state = new_state
        pass

    def drop_state(self):
        self._target_state = self._begin_state
        pass

    def clear_state_machine(self):
        self._target_state = self._begin_state
        self._target_state.clear_states()
        pass
