# file = open("Day 24/my_file.txt")
# contents = file.read()
# print(contents)
# file.close()


with open("Day 24/my_file.txt") as file:
    """This is read only file mode. By default is : ("Day 24/my_file.txt",mode='r')"""
    contents = file.read()
    print(contents) 

with open("Day 24/my_file.txt",mode="w") as file:
    file.write("This mode will delete everything and overwrite the file with this line. \n")

with open("Day 24/my_file.txt",mode="a") as file:
    file.write("This mode will append new text to the already existing text.") 

with open("Day 24/my_new_file.txt",mode="w") as file_new:
    file_new.write("If this file doesn't exist and you want to create it, you do this in mode='w'. \n")