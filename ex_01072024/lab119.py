# Hierarchical Inheritance

# Father - Multiple Children

class Father:
    def BHK3(self):
        print("3bhk")

class pinky(Father):
    def BHK2(self):
        print("2bhk")
class megha(Father):
    def BHK1(self):
        print("1bhk")

class neha(Father):
    def no_flat(self):
        print("no_flat")



pinky_ref_obj = pinky()
pinky_ref_obj.BHK2()
pinky_ref_obj.BHK3()

megha_ref_obj = megha()
#megha_ref_obj.BHK2    #NOT POSSIBLE  # BHK2()? This belong to PINKY WHICH MEGHA CAN NOT ACCESS
megha_ref_obj.BHK1()
megha_ref_obj.BHK3()