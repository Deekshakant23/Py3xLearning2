numbers = [1, 2, 3, 4, 5, 6, 7, 8]


def double(number):
    return number * 2


def even(number):
    return number % 2 == 0


doubled_numbers = map(double, numbers)
print(list(doubled_numbers))
even_numbers = filter(even, numbers)
print(list(even_numbers))

