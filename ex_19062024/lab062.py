def find_even_odd(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")


find_even_odd(6)

# lambda expression
check_even_odd = lambda num: "Even" if num % 2 == 0 else "Odd"
print(check_even_odd(11))
