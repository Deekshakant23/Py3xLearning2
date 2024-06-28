class person:
    # Class Variables / instance variables
    name = "deeksha"
    age = "34"

    def walk(self):
        a = 20 # Local Varaible
        print("i am a method")
        print("hi", self.age)


priya = person()
priya.walk()
