# Dictionary Comprehension
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

import random

names = ["Alex","Peter","Beth","Marija","Angela","Tor"]

student_scores = {student:random.randint(1,100) for student in names}
print(student_scores)

#{'Alex': 53, 'Peter': 17, 'Beth': 44, 'Marija': 72, 'Angela': 47, 'Tor': 28}

passed_students = {student:score for (student,score) in student_scores.items() if score >= 60}

print(passed_students)

# You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the 
# given sentence and calculates the number of letters in each word.  

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}
print(result)