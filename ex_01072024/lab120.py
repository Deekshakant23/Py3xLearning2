#multilevel Inheritance

# Father - Multiple Children

class Grandfather:   #LEVEL1
    def BHK3(self):
        print("3bhk")

class father(Grandfather): #LEVEL12
    def BHK2(self):
        print("2bhk")
class child(father):   #LEVEL3
    def BHK1(self):
        print("1bhk")


child_obj_ref =child()
child_obj_ref.BHK1()
child_obj_ref.BHK2()
child_obj_ref.BHK1()


father_obj_ref =father()
father_obj_ref.BHK3()
father_obj_ref.BHK2()

grandfather_obj_ref = Grandfather()
grandfather_obj_ref.BHK3()