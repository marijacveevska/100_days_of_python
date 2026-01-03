# EXAMPLE WRONG CODE
"""
age = int(input("How old are you? "))

if age > 18:
    print("You are allowed to drive at age {age}")

"""

# SOLUTION

try:
    age = int(input("How old are you? "))
except ValueError:
    print(" You have typed invalid number. Please try again with a numerical responce example. 15")
    age = int(input("How old are you? "))


if age > 18:
    print(f"You are allowed to drive at age {age}")