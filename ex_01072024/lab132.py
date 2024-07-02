from abc import ABC, abstractmethod


class PTM(ABC):

    def enrolled(self):
        print("user enrolled")

    @abstractmethod
    def perform_task1(self):
        pass

    @abstractmethod
    def perform_task2(self):
        pass


class deeksha(PTM):

    def perform_task1(self):
        print("done task 1")

    def perform_task2(self):
        print("done task 2")


deeksha = deeksha()
print(deeksha.perform_task2())
print(deeksha.perform_task1())
