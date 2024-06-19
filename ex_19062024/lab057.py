# function with in the function

def outer_f1():
    v1 = 10
    v2 = 20

    def inner_f2():
        print(v1)

    inner_f2()

    def inner_f2():
        print(v2)

    inner_f2()


outer_f1()
