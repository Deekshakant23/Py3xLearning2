class Calculator:

    def __init__(self):
        print("hello calciiiii")

    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def dev(self, a, b):
        return a * b


object_ref = Calculator()
output = object_ref .sum(5, 3)
print(output)
