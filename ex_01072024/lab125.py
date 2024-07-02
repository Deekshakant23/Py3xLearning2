class GF:
    def car(self):
        print("kia car")


class F(GF):
    def car(self):
        print("kia SALTOS")


class S(F):
    def car(self):
        print("kia SONET")


s_obj_ref = S()
s_obj_ref.car()

# if we have the same method name in call the class and u wan to acess the each of one the u have to create indiviual
# class object instance to access the method
gf = GF()
gf.car()

# multilevel example
