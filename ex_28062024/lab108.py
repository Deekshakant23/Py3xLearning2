# Encapsulation -
# bind the data variables with the methods
# Data Member - / Class Variables
# Methods - Def function within the class
# Wrapping or binding the data variables with the methods - Encapsulation.

# Hide the data members(class variables, instance variables) by using only the methods.

class login:

    def __init__(self):
        self.passord = None
        print("i aam method")

    def change_password(self):
        self.passord = "3455"
        print("hfhhf", self.passord)


deeksha = login()
# deeksha.passord = "33456"
deeksha.change_password()