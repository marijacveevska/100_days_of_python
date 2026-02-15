# #FileNotFoundError
# with open("a_file.txt") as file:
#     file.read()

# #KeyError
# a_dict = {"key":"value"}
# value = a_dict["non_existent_key"]
# print(value)

# #IndexError
# fruit_list = ["apple","banana","pear"]
# fruit = fruit_list[3]

# #TypeError
# text = "abc"
# print(text+5)

#CATCH EXCEPTION

# try: Something that might cause an exception
# except: Do this if there was an exception
# else: Do this if there were no exceptions
# finally: Do this no matter what happens

try:
    file = open("Day 30/a_file.txt")
    a_dict = {"key":"value"}
    print(a_dict["non_key"])
except FileNotFoundError:
    file = open("Day 30/a_file.txt","w")
    file.write("something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")

else:
    content = file.read()
    print(content)

finally:
    file.close()
    print("File was closed")