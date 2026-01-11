nested_programming_dictionary = { 
    "Key1": ["item1","item2","item3"], 
    "Key2": ["item1","item2",["item3","item4"]],

    "Key3": {"NKey1": "NVal1","NKey2": ["NVal2","Stuttgart"],}, 

    "Key4": "Value4",
}


# List as value
print(nested_programming_dictionary["Key1"][0])

# Nested List as value
print(nested_programming_dictionary["Key2"][2])
print(nested_programming_dictionary["Key2"][2][1])

# Nested Dictionary and List as value
print(nested_programming_dictionary["Key3"]["NKey2"][1])

# Regular key:value pair
print(nested_programming_dictionary["Key4"])


