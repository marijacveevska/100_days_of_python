import random

rock_paper_scissors = ["Rock","Paper","Scissors"]

my_choice = input("What do you choose? Type Rock, Paper or Scissors ")

if my_choice not in rock_paper_scissors:
    print("Invalid input")
else:
    comp_choice = random.choice(rock_paper_scissors)

    print(f"Your choice is: {my_choice}")
    print(f"Computer's choice is: {comp_choice}")


    if my_choice == comp_choice:
        print("You are equal")
    elif my_choice == "Rock" and comp_choice == "Scissors":
        print("You win, Computer loses")
    elif my_choice == "Paper" and comp_choice == "Rock":
        print("You win, Computer loses")

    elif my_choice == "Scissors" and comp_choice == "Paper":
        print("You win, Computer loses")

    else:
        print("Computer wins, you lose")


