# File Handling
# How to Read a Text, and Write into it using python Code.

# Function -
# open("file_name","mode")

# Mode -
# 'r' for reading (default).
# 'w' for writing (creates a new file or truncates an existing one).
# 'a' for appending.
# 'b' for binary mode.  zoom.exe - binary
# '+' for updating (reading and writing).


# Read and Write content
# Read a File
# Reading Entire Content: content = file_object.read()
# line = file_object.readline() for a single line.
# lines = file_object.readlines() for all lines in a list.
# # Close the file

file = open("TestData.txt", 'r')   #id exist in same folder then u need to give only file name here, if file is another folder then u need to profile whole pathe of that file like:"/Users/promode/PycharmProjects/Py3xATBLearning/ex02_July/01072024/TestData2.txt"
content = file.read()
print(content)
file.close()