#1.Develop a Python script that calculates the square and cube of a given number. num = 2 sq - 4, c = 8

s1 = 2
s2 = 2
area_square = s1*s2
print("area of square" '\t' +str(area_square))

#alternet way
num = 2
square = num*2
cube = num**3

print("value of square is:", square)
print("value of cubeis :", cube)

#2.Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.


num1 = float(input("enter the first number"))
num2 = float(input("enter the second number"))
if (num1>num2):
    print("first number is greater")
elif (num1<num2):
   print("first number is less than second number")
else:
  print("first number is equal to second number")
