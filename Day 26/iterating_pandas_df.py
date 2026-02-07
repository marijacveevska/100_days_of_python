import random
import pandas

# How to iterate over Pandas DataFrame

# Dictionary
student_dict = { 
    "student": ["Marija","Angela","Tor"],
    "score": [29,17,20]
}

for (key,value) in student_dict.items():
    print(key)
    print(value)

# Data Frame
student_df = pandas.DataFrame(student_dict)
print(student_df)    

# Loop through rows of a data frame

for (index, row) in student_df.iterrows():
    if row.student == "Angela":
        print(row.score)

    if index == 0:
        print(row)