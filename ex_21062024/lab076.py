set1 = set(["TheTestingAcademy", "For", "TheTestingAcademy."])
print(len(set1))

for i in set1:
    print(i)

set1 = set([1, 3, 4, 5, 6, 7, 7, 8, 8])
print(len(set1))
set1.remove(7)
print(set1)
print(len(set1))
set1.add(23)
print(set1)
set1.pop()
print(set1)
