from abc import ABC, abstractmethod


class LOVE(ABC):

    @abstractmethod
    def attension(self):
        pass

    def time(self):
        print("spent time")


class rohit(LOVE):
    def attension(self):
        print("go for a date")


ro = rohit()
ro.attension()
