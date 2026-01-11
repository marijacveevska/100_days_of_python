# ONE INPUT
def greet(x):
    print("Hello " + x) 

name = input("What is your name? ")
greet(name)

# x is called a PARAMETER, and is the name of the data that is passed in the function
# name or "Petar" is called an ARGUMENT, and is the actual value of the data

greet("Petar")

# LIFE IN WEEKS CALCULATION

def life_in_weeks(x):
    y = 90 - x
    weeks = y * 52
    print(f"You have {weeks} weeks left.")

age = int(input("what is your age? "))

life_in_weeks(age)

# TWO INPUTS

def greet_with_info(x,y):
    print("Hello " + x) 
    print(f"Do you like living in {y}? ")

name = input("What is your name? ")
location = input("Where do you live? ")

greet_with_info(name,location)

greet_with_info(x="Tanja",y="Skopje")