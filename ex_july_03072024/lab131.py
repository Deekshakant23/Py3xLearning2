#exceptional handiling  : # An exception is an event that occurs during the execution of a program that disrupts the normal flow of instructions.

#while True print("Hello World")  # you will get ZeroDivisionError: division by zero this error when u run this line of code

# Syntax Error
# Identation - most common kind of complaint you get

print("Start")
10/0
print("End of the program")


a = int(input("Ent the num1"))    # ValueError: invalid literal
b = int(input("Ent the num2"))
c = a/b                           # ZeroDivisionError
print("Result Div is ", c)

# What are the different problem we can face?

# Why we want to handle this?

# ATM -> SBI
# ATM -> SBI -> INSERTED card -> 10k
# Entered the amount, PIN, money got deducted but you din't get it
# via ATM, There is not message( not handled properly)



# Bad User Exp.
# User will curse you :)
# We need to handle it and give user a better exp.