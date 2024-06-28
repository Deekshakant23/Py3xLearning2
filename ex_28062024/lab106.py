class car:
    name = None
    make = None
    model = None

    def __init__(self, o_name, o_make, o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model

    def car_brand(self):
        print("Starting a car with the name " + self.name)
        print("Starting a car with the make " + self.make)
        print("Starting a car with the model " + self.model)


kia = car("kia1", "nline", "2023")
kia.car_brand()

huyndai = car("h1", "Rline", "2024")
huyndai.car_brand()
