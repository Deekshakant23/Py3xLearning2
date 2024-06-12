
# Problem  Find the Max between 3 numbers

# num1, num2 , num3

# num1 > num2 and num1 > num3 ->  num1
#
# num2 > num1 and num2 > num3 -> num2
#
# num3


num1 = int(input("enter the num1\n"))
num2 = int(input("enter the num2\n"))
num3 = int(input("enter the num3\n"))

if num1 >= num2 and num1 >= num3:
    print(num1)
elif num2 >= num1 and num2 >= num3:
    print(num2)
else:
    print(num3)