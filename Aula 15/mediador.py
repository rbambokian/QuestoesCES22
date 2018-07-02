class Mediator:
    def __init__(self):
        self._colleague_1 = Colleague1(self)
        self._colleague_2 = Colleague2(self)


class Colleague1:
    def __init__(self, mediator):
        self._mediator = mediator


class Colleague2:
    def __init__(self, mediator):
        self._mediator = mediator


def main():
    mediator = Mediator()


if __name__ == "__main__":
    main()
