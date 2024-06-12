# ✅ Conditions
# age > 18 -> You are allowed to go the club
# age < 18 -> You are not allowed

# pramod -> goa -> father permission
# pramod -> no goa -> no permission

# If, ELSE
# Syntax
# if condition:
#     code to be executed
# else:
#     code to be executed when condition is false

# Write a program to take a user age and let him know if he can go the club.

# Take a user pinput

age = int(input("enter the age"))
if age > 18:
    print("go to the club")
else:
    print("not allowed")


#single if code
age = 90
if age > 100:
    print("You are old")
