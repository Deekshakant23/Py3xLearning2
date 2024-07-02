# Multiple Inheritance


class father:
    def father_money(self):
        return "5"

    def home(self):
        return "this is my father home"


class mother:
    def mother_money(self):
        return "6"

    def home(self):
        return "this is my mother home"


class child(father, mother):   #who ever is define fisrt that will call first
    pass


# Probelm - Diamond Problem - Java
# Python - Multiple Inheritance
# F,M -> S

child_ref_obj = child()
child_ref_obj.father_money()
child_ref_obj.mother_money()
print(child_ref_obj.home())
