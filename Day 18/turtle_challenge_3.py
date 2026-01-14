from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("classic")
timmy.color("red")
timmy.speed(1.5)

# Challenge 3 - Draw triangle, square,pentagon,hexagon,heptagon,octagon,nonagon and decagon
sides = [3,4,5,6,7,8,9,10]
color = ["RoyalBlue","moccasin","OrangeRed","aquamarine4"]

for side in sides:
    angle = 360 / side
    timmy.color(random.choice(color))
    for x in range(0,side):
        timmy.forward(100)
        timmy.right(angle)



screen = Screen()
screen.exitonclick()