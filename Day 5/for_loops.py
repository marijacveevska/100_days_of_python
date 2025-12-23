# For Loops
# example 1
# for item in list_of_items:
    # Do something to each item
# example 2
# for number in range (a,b)
    # Do something for the amount of numbers


fruits = ["apple","pear","peach"]

for fruit in fruits:
    print(fruit)
    print(fruit + " pie")


student_scores = [30,30,29,15,3,5,7,10,11,18,18,18,5,21,20,22,5,28,30,29,28,6,27]

# MAX
print(max(student_scores))

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)

# MIN
print(min(student_scores))

min_score = student_scores[0]
for score in student_scores:
    if score < min_score:
        min_score = score
print(min_score)

# SUM
print(sum(student_scores))

sum = 0
for score in student_scores:
    sum += score
print(sum)

# Range

sum_100 = 0
for i in range(1,101):
    sum_100 += i
print(sum_100)


