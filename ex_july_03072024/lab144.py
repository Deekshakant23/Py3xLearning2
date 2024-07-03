# this how u can append something in file
with open("TestData.txt", "a") as file:
    file.write("hello i am doing first time file exception")

# this how u can read something in file
with open("TestData.txt", "r") as file:
    content = file.readlines()
    print(content)

# for line in content:
#     print(line, end="")