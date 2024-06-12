factorial = int(input("Enter the Number:\n"))
num = 1
for i in range(1, factorial+1):
    num = num*i
print(f"The Factorial of {factorial} is {num}")