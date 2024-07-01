class parent:
    gold = "3kg"

    def BHK2(self):
        print("i have 2 bhk flat")


class child(parent):
    def BHK4(self):
        print("i have 4 bhk flat")


child_obj_ref = child()
child_obj_ref.BHK4()
child_obj_ref.BHK2()
print(parent.gold)


father_obect_ref = parent()
#father_obect_ref.BHK3()
#father_obect_ref.gold