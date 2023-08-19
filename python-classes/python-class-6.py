# Read File
# f = open("file.txt", "r")

# Method 1:
# fileContent = f.read() #read whole file at once return string, so thats why make sure file size should be smaller
# print("Read", fileContent)

# if you want to replace anything in content you can use replace method its works only when you read file at once
# fileContent.replace("**name**", "Hamza") #pass any place holder or any string who laready exist in your content file
# print("Read after replace string",fileContent)

# Method 2:
# fileContent = f.readlines() #read each line and return list of line strings
# print("Read Lines", fileContent)

# Method 3:
# row = f.readline() #read each line and return list of line strings
# print("Read Line",row)
# # print using while loop
# while f.readline():
#     row = f.readline()
#     print(row)
# f.close()

# Write File
""" 
Note: Make sure when you use write check any file is exist with the name of you provided 
other wise wirte function override your content and you loss content
 """
f = open("write_file.txt", "w")

# # Method 1
# f.write("A B C D\n")
# f.write("A B C D")

# # Method 2
# f.writelines(["A B C D\n", "E F G H\n", "I J K L"])

# # Append File
# f = open("file.txt", "a")
# f.write("Hamza Hamza")

""" 
Note: when you done your operation with file must close your file using f.close()
 """
# f.close()

# Write and also read content same time
# f = open("file2_txt", "w+")
# print("pointer postion", f.tell())
# f.write("Hamza")
# print("Read FIle", f.read())
# f.seek(0)
# print("Read File after reset pointer", f.read())

# Write and also read content same time
# f = open("file2_txt", "r+")
# print("pointer postion", f.tell())
# f.write("Hamza")
# print("Read FIle", f.read())
# f.seek(0)
# print("Read File after reset pointer", f.read())

# Write and also read content same time
# f = open("file2_txt", "a+")
# print("pointer postion", f.tell())
# f.write("Hamza")
# print("Read FIle", f.read())
# f.seek(0)
# print("Read File after reset pointer", f.read())

# flush method clear the buffer and imidiate write to a file 
# f.flush()
# # 
# import time
# # Time sleet method use for pause it just like set timeout
# time.sleep()

# Module OS
import os

get_current_directory = os.getcwd()
print(get_current_directory)

# print(__file__)

list_of_files = os.listdir()
# print(list_of_files)

path = os.path.join(get_current_directory, "..")
# print(path)

absPath = os.path.abspath(path)
print(os.listdir(absPath))
# # if you want to back 
# path = os.path.join("..", "..", "files", "main.py")
# print(path)
