# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# {key:value} = {"Bug":"An error in a program that prevents the program from running as expected."}

programming_dictionary = { 
    "Key1": "Value1", 
    "Key2": "Value2", 
    "Key3": "Value3",
}


# Call on a key to get the value
print(programming_dictionary["Key1"])


# Add new key and value in the Dict
programming_dictionary["Key4"] = "Value4"


# Edit an existing item in the Dict
programming_dictionary["Key1"] = "Value0"

print(programming_dictionary)

# Loop through a Dict
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Wipe a Dictionary clean
# programming_dictionary = {}