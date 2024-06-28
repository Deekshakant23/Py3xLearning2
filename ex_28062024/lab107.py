class Girikon_Page:
    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    def login(self):
        if self.email == "pramod@gmail.com" and self.password == "Pass123":
            print("Allowed to enter")
        else:
            print("Not allowed")

email = input("enter the email \n")
password = input("enter the password \n")
deeksha = Girikon_Page(email, password)
deeksha.login()

#another way to call the class

pramod = Girikon_Page("pramod@gmail.com", "Pass123")
pramod.login()