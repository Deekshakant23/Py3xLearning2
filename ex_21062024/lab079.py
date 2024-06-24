# Decorators
# What is a Decorator?
# A decorator is essentially a function that takes another function as an argument
# returns a new function that usually extends the behavior

def decorator_function(func):
    def wrapper():
        print("its starting")
        print("***********")
        func()
        print("*******")
        print("ending")

    return wrapper()

@decorator_function
def say_hello():
    print("Say Hello")


