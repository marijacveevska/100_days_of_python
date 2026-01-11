print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

direction = input("You are at a crossroad, where do you go? left or right? ")

if direction == "right":
    print("You fell into a hole. Game Over")
elif direction =="left":
    choice1 = input("Now you swim or wait? ")
    if choice1 == "swim":
        print("Shark ate you.Game Over")
    elif choice1 =="wait":
        choice2 = input("Boat took you to an island with a house on the beach. The house has 2 doors. Which door do you choose? red or yellow? ")
        if choice2 == "red":
            print("You got burned by fire. Game Over")
        elif choice2 =="yellow":
            print("You win the Treasure!")
else:
    print("invalid input")
