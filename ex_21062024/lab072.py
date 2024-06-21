#union ,intersection and difference how it works in python by using set

set1 = {1, 2, 3}
set2 = {4, 5, 6}
new_set = set1.union(set2)
print(new_set)

set3 = {6, 2, 5, 4}
set4 = {10, 9, 6}
new_set2 = set3.intersection(set4)
print(new_set2)

# my_set = set1.difference(set2)
new_set = set2.difference(set1)
print(new_set)