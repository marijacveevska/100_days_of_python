import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters between 10 and 20 would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols between 2 and 6 would you like?\n"))
nr_numbers = int(input(f"How many numbers between 6 and 10 would you like?\n"))

# Solution 1
lists = [letters,numbers,symbols]
password=[]
for x in lists:
    
    if x == letters:

        for letter in range(0,nr_letters):
            password.append(random.choice(letters))

    if x == numbers:

        for number in range(0,nr_numbers):
            password.append(random.choice(numbers))
    
    if x == symbols:

        for symbol in range(0,nr_symbols):
            password.append(random.choice(symbols))

random.shuffle(password)
your_pass = "".join(password)

print(f"Your password is: {your_pass}")

# Solution 2

lists = [letters,numbers,symbols]
password=[]
for x in lists:
    
    if x == letters:

        for letter in range(0,nr_letters):
            password.append(random.choice(letters))

    if x == numbers:

        for number in range(0,nr_numbers):
            password.append(random.choice(numbers))
    
    if x == symbols:

        for symbol in range(0,nr_symbols):
            password.append(random.choice(symbols))

print(password)
random.shuffle(password)

str_pass = ""
for elem in password:
    str_pass += elem

print(f"Your password is: {str_pass}")