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