# Creating new list from an existing list 
# FOR loop
numbers = [1,2,3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

print(new_list)

# List Comprehension
# new_list = [new_item for item in list]
numbers = [1,2,3]
new_list = [n+1 for n in numbers]
print(new_list)


# Strings
name = "Marija"

new_letter_list = [ letter for letter in name]
print(new_letter_list)

# Python Sequences : list, string, tupple, range

double_list = [n*2 for n in range(1,5)]
print(double_list)

# CONDITIONAL List Comprehension
# new_list = [new_item for item in list if test]

names = ["Alex","Peter","Beth","Marija","Angela","Tor"]
short_names = [n for n in names if len(n) < 5]
upper_names = [n.upper() for n in names if len(n) >= 5]
print(short_names)
print(upper_names)