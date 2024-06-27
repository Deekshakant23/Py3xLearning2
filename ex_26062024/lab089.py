# Create a class

class Person:
    # Attributes
    name = None
    id = None
    age = None
    phone_number = None

    # attribute

    def talk(self):  # No Arg -> No Return
        print("I can talk")

    def sleep(self, name):  # Arg with No Return
        print("sleep", name)
        print("i am method")

    def sleep2(self, name):  # Arg with Return
        print("i am also method")
        return None

    def walk(self):
        print("i can walk")

    def walk_return(self):  # No Arg with Return
        return "i am walking"

    # Create Object of the Person Class
    # objectRef = Object ->  ClassName()


deeksha1 = Person()
deeksha1.name = "pinky"
print(deeksha1.name)
deeksha1.talk()
deeksha1.walk()
