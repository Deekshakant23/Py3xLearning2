
class A:
    def method(self):
        print("i am A")


class B:
    def method(self):
        print("i am B")


class C(A, B):
    print( "I am C")


c_obj_ref = C()
c_obj_ref.method()


