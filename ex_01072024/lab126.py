# Polymorphism
# Polymorphism allows objects of
# different classes to be treated as
# objects of a common superclass.

# Pramod -> Mentor, Husband, Brother.
# Object -Method -> Mother, Matenal She is, sister, parent -

# Method overriding

class shape:
    def area(self):
        print("area of the shape")


class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class circle(shape):
    def __init__(self, redius):
        self.redius = redius

    def area(self):
        return 3.14 * self.redius * self.redius

shape1 = rectangle(3,5)
print(shape1.area())

shape2 = circle(56)
print(shape2.area())

shape3 = shape()
print(shape3.area())