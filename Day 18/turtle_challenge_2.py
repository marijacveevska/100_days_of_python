from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("classic")
timmy.color("red")
timmy.speed(1.5)


# Challenge 2 - Draw a dashed line
for x in range(0,10):
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()
    timmy.forward(10)


screen = Screen()
screen.exitonclick()