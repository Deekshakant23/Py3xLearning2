# Inheritance
# Acquire the Attributes and Behaviour
# Data members and Methods

# 3BHK Hourse -F -> Inheritance - Son -
# concept in object-oriented programming (OOP)
# that allows a class (child class) to inherit attributes and methods
# from another class (parent class)

# Types of Inheritance

# Single - 80%  - # API, Web Automation - 80% -> Single
# Multiple
# Multi level
# Hybrid
# Hierarchical



#single Inheritance
class grandparent:         # Parent Class, Base Class
    key = "abh @ gmail.com"

    def grandparent_method(self):
        return "grandparent's method"


class father(grandparent):     # Child Class, Sub Class
    def parent_method(self):
        return "parent method"

lal = grandparent()
lal.grandparent_method()
# grandfather.parent_method()


pradeep = father()
print(pradeep.grandparent_method())
print(pradeep.parent_method())  # how parent is able to call the graparent? inheritance
print(father.key)
