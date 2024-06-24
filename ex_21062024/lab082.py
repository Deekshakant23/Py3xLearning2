def decorator1(func):
    def wrapper():
        print("deco 1")
        func()
    return wrapper


def decorator2(func):
    def wrapper():
        print("deco 2")
        func()
    return wrapper


@decorator1
@decorator2
def say_hello():
    print("hii")


say_hello()
