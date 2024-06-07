# List - Shopping List
# milk, bread, butter, poha
# 1. Add item
# 2. Remove item
# 3. Update item
# 4. View item
# 5. Exit


shopping_list = ["table", "nife", "table cover", "iphone"]
print(shopping_list)
print(type(shopping_list))
print(len(shopping_list))
print(shopping_list[2])
print(shopping_list[-1])

shopping_list.insert(2, "comb")  # Add item in the middle
print(shopping_list)
shopping_list.append("shampoo") # Add item in the end
print(shopping_list)
shopping_list.extend(["oil", "brush"]) # Add multiple items in the end
print(shopping_list)


#marging 2 list
rohit_list = ["trimmer", "bedsheet", "pen"]
shopping_list.extend(rohit_list)
print(shopping_list)

#marging numeric value
num = [1,3,4,5,3]
shopping_list.extend(num)
print(shopping_list)



#insert the value by using len function without indexing
shopping_list.insert(len(shopping_list)-1, "car")
print(shopping_list)


