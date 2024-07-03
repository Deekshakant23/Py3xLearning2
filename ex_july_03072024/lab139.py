class MyCustomException(Exception):
    def __init__(self, message):
        self.mesage = message
        super().__init__(message)


balance = 3000
withdrow = int(input("enter the amount"))
if withdrow > balance:
    raise Exception("BAL IS LOW")
else:
    print("remain bal", (balance - withdrow))