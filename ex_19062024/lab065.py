# map function
# Map()
# Takes each item from list
# execute function on it
# return same no of elements (list)
# return modified list

my_list = [3, 5, 6, 7]


def double_item(num):
    return num * 2


result = list(map(double_item, my_list))
print(result)
