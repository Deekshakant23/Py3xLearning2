from abc import ABC, abstractmethod


class father(ABC):
    def __init__(self, name):
        self.name = name


@abstractmethod


def loan(self):
    pass


class deeksha(father):
    def loan(self):
        print("loan given")


p1 = deeksha("rohit")
p1.loan()
