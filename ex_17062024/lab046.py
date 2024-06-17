# Functions
# Block of Code - Which can executed or reused.
# Define
# Call

# Built Functions - bultins.py - file (Python 3 setup)
# Which are created by the Python Contributers
#result = max(2, 3)


# User Defined
# They can return something
# The can't return -> non return
# They have parameters
# They don't parameters / arguments

# def say_hello():  # No Return Type and No Parameter / Argument
#     print("Hello")
#
#
# say_hello()
#
#
# def say_hello_arg(name):  # No Return Type and with Argument
#     print("Hello", name)
#
#
# say_hello_arg("pramod")
# say_hello_arg("amit")
def say_hello_agr_default(name="deeksha"):  # No Return Type and with Default Argument
    # Write the Code
    print("hello", name)


say_hello_agr_default()
say_hello_agr_default("pinky")
say_hello_agr_default(name="rohit")


def sum_number_argument_ret(a, b): # Argument + return Type
    #print(a, b)
    return a+b

#result = sum_number_argument_ret(2,4
result = sum_number_argument_ret(a=29,b=24)
#result = sum_number_argument_ret(b=3, a=24)
print(result)


