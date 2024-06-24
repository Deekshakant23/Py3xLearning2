# dictionary is in a key-value pair format always.

pramod_details2 = \
    {"name": "pinky",     #name,90,isfemale and address are keys
     "90": 34.34,          #here pinky,34.34,true and delhi are value
     "isFemale": True,
     "Address": "Delhi"
     }

print(pramod_details2.get("Address"))    # this is how u can print the value in dictionary
print(pramod_details2["Address"])      # this is another way to u can print the value in dictionary
print(pramod_details2.values())
print(pramod_details2.keys())

my_dict = {'a': 1, 'b': 2, 'c': 3,'a': 95, 'd': 95}   # duplicate key is not allowed in dictionary
print(my_dict)
print(len(my_dict))   # that is why ouput is here 4
print(list(my_dict.keys()))
print(list(my_dict.values()))

for k, v in my_dict.items():   # k means key and v means value here ....that loop will give u all key and value alltogather
    print(k, v)