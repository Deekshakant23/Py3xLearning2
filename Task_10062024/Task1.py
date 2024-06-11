#1.#Explain the difference between the = operator and the == operator in Python.

# = its is assignment operator , which we used to assign any value to a any variable

x = 3 # here 3 is assigned to x with the help of = operator
# or u can say 3 is assign to variable to x
print(x)


# == its a relational operator for checking the equality of two value
# also this == operator always given output in boolean form like(TRUE AND FALSE)

x = 10
y = 20

print(x >= y)    # 10>20 or 10=20 #returns False because 10 is not greater than 20 or nor equal to 20
print(y == x)    # 20 =10  #returns False because 20 is not equal to 10

#another way to use these operators

result =(x ==y)
print(result)

#2 What does the ** operator do in Python, and how is it used?

# ** operator is called Exponentiation
#this is the arithmatic operator
#it's a power operator that raises the number on its left to the power of the number on its right

a = 2
b = 4
print( a ** b)  # 2*2*2*2

#3.What does the ^ operator do in Python, and in what context is it commonly used?

# ^ Sets each bit to 1 if only one of two bits is 1

a = 2
b = 3

# Decimal numbers and their binary values:
#2 = 0000000000000010
#3 = 0000000000000011
print(2 ^ 3) #The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:
