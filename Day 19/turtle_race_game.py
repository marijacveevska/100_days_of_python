import turtle as t
from turtle import Turtle, Screen
import random

red_t = Turtle()
orange_t = Turtle()
yellow_t = Turtle()
green_t = Turtle()
blue_t = Turtle()
purple_t = Turtle()


screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")

turtles = [red_t,orange_t,yellow_t,green_t,blue_t,purple_t]
colors = ["red","orange","yellow","green","blue","purple"]

def turtle_style(turtles,colors):
    for turt,col in zip(turtles,colors):
        turt.shape("turtle")
        turt.speed("normal")
        turt.color(col)

def starting_position(turtles):
    start_x = -200
    start_y = -100
    spacing = 40
    for i, turt in enumerate(turtles):
        turt.penup()
        turt.goto(start_x, start_y + spacing * i)


# enumerate(turtles) is [(0, turtles[0]), (1, turtles[1]),(2, turtles[2]),(3, turtles[3]),(4, turtles[4]),(5, turtles[5])]
# zip(turtles,colors) is 
    # (red_t, "red")
    # (orange_t, "orange")
    # (yellow_t, "yellow")
    # (green_t, "green")
    # (blue_t, "blue")
    # (purple_t, "purple")

turtle_style(turtles,colors)
starting_position(turtles)

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turt in turtles:
        distance = random.randint(0,10)
        turt.forward(distance)

        if turt.xcor() >=200:
            is_race_on = False
            winning_color = turt.pencolor()
            print(f"The winner is the {winning_color} turtle")

            if winning_color == user_bet:
                print("You won!")
            else:
                print(f"You lost!")


screen.exitonclick()