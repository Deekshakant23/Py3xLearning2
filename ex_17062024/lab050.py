# *args - any number of arguments
# print("Pramod", "Amit", "SB")
def sum_of_three(a=1, b=3, c=4):
    return a + b + c


result = sum_of_three()
result1 = sum_of_three(1, 3)
result2 = sum_of_three(a=20, b=2, c=3)
print(result, result1, result2)
