
# In built Functions -
# Function -> Repeat a task - You can use a function.
# print(),input, type(), format(), max, min, id(), sum(), avg()
# Strings
name = "deeksha" #0-6
# 0,1,2,3,4,5,6
# d,e,e,k,s,h,a
print(name)
print(type(name))
print(len(name))
print(id(name))   #id -> memory address where it is stored 2245213754192

a = name.count('k')
print(a)

#print(name[4]) # string index out of range

# Python - Immutable - that can't be changed
name[0] = "P" # 'str' object does not support item assignment