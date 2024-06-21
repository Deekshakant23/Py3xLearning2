# how we can append the value in tuple


# value  and , this is one way u can add the value)
t1 = (23, 56, 78)
print(t1)
new_t1 = t1 + (7,)  # create new tuple and and the (value  and , this way u can add the value)
print(new_t1)

# another way by coverting the tuple into a list

my_list = list(t1)
print(my_list)
my_list.append(3)
my_list1 = tuple(my_list)
print(my_list1)
