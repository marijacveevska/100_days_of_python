from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("classic")
timmy.color("red")
timmy.speed(1.5)

# Using the GUI - Graphical User Interface

# Challenge 1 - Draw a square
for x in range(0,4):
    timmy.right(90)
    timmy.forward(100)

screen = Screen()
screen.exitonclick()