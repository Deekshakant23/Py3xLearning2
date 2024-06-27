my_dict = \
    {
        'a': 1,
        'b': 2,
        'c': 3
    }

for k, v in my_dict.items():
    if k == 'a':
        print("key with the name a is found")

output = 'a' in my_dict
print(output)  # output is always comes in True or False
output = 'b' in my_dict
print(output)

output = 't' in my_dict
print(output)
