import random
from guess_the_number_art import guess_the_number_ASCII

def guessing(g,c,l):
    diff = abs(g - c)
    if diff > 2 and g < c:
        print("Too Low")
        return l-1
    elif diff > 2 and g > c:
        print("Too High")
        return l-1
    elif g == c:
        print("CORRECT, YOU WIN !")
        return 0
    elif diff <= 2 and g < c:
        print("Too Low, but you are getting close")
        return l-1
    elif diff <= 2 and g > c:
        print("Too High, but you are getting close")
        return l-1
    


print(guess_the_number_ASCII)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
comp_number = random.randint(1,100)

if difficulty != "easy" and difficulty != "hard":
    print("Not valid input")

else:
    if difficulty == "easy":
        lives = 10

    elif difficulty == "hard":
        lives = 5

    while lives > 0:
        guess = int(input("Make a guess: "))
        lives = guessing(guess,comp_number,lives)
        if lives > 0:
            print(f"Lives left {lives}")
        

    if lives == 0 and guess != comp_number:
        print("Lost all your lives :(")
        print("*** YOU LOSE! ***")
        print(f"The correct number was {comp_number}")
    