# Hybrid Inheritance

# multiple types of inheritance,
# such as single,
# multiple, and
# multilevel inheritance.

class A:
    def method1(self):
        print("i am A")


class B(A):
    def method2(self):
        print("i am B")


class C(A):
    def method3(self):
        print("i am C")


class D(C, B):  # Multiple, Multilevel - MRO(Method Resolution Order - First
    def method4(self):
        print("i am D")


d_obj_ref = D()
d_obj_ref.method3()
d_obj_ref.method1()
