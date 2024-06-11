# Program - Calculate the area of circle.
# input -> radius
# output -> area
import math

# data types
# input -> int or float -> float
# output -> float

# Core Logic -> pi*r*r = 3.14

radius = float(input("enter the radius:"))
print(math.pi)

area1 = math.pi*(radius**2)
print(area1)

#alternet way to thnis area calculation
area2 = math.pi*(math.pow(radius,2))
print(area2)

#alternet way to thnis area calculation(single line code)
print(3.1415*(float(input("enter the radius"))**2))