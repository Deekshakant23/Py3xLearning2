# tuple --collection of item and its immutable
#uple'does not support item assignment

my_list = [2, 4, 6, 7]
print(id(my_list))
my_list[0] = 34
print(my_list)

my_tuple = (2, 4, 6, 7)
#my_tuple[0] = 21 # Immutable
print(my_tuple)
