#operators
# Assignment Operator
# = - assign the value from right to left

name = "deeksha"

# == -> Compare operator ( bool)
#he “==” operator is known as the equality operator. The operator will return “true” if both the operands are equal
v1  = (1 == True)
v2  = (0 == False)
print(v1)
print(v2)

age = +98 # Unary Operator + ( Pycharm +_ -> Remove, Self exp.
num = -1
print(age)
print(num)
p = age+num  # BODMAS - Math (98+(-1))
print(p)

is_married = True
print(not is_married)

# Is Operator - Identity Operator - Return bool
# List

a = 4
b = 9
c = False


print(a is b)

my_list = [1,2,3]
my_list2 = [1,2,3]
print(my_list is my_list2)