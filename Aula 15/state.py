import abc


class Context:
    def __init__(self, state):
        self._state = state

    def request(self):
        self._state.handle()


class State(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def handle(self):
        pass


class ConcreteStateA(State):
    def handle(self):
        pass


class ConcreteStateB(State):
    def handle(self):
        pass


def main():
    concrete_state_a = ConcreteStateA()
    context = Context(concrete_state_a)
    context.request()


if __name__ == "__main__":
    main()
