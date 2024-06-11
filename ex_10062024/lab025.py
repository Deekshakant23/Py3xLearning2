# Logical Operator always produce output in bool
x = 20
y = 40

print(x>y)
print(x<y)

a = 10
b = 20
print(a >= b) # 10 > 20 or 10 = 20
print(a == b) # 10 = 20 or 10 = 20
print(not a)

f = False
t = True
print(f and t)
print(f or t) # Truth Table of or

x = 10
y = 20

result = (x != y) # 10 not equal 20 -> True
print(result)