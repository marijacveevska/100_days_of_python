from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("classic")
timmy.color("red")
timmy.speed(5)
timmy.pensize(6)

# Challenge 3 - Draw triangle, square,pentagon,hexagon,heptagon,octagon,nonagon and decagon

color = ["RoyalBlue","moccasin","OrangeRed","aquamarine4","DarkOrchid","LightSeaGreen"]
side = [timmy.right,timmy.left]
angle = [0,90,180,270]

for x in range(150):
    timmy.color(random.choice(color))
    timmy.forward(30)
    a = random.choice(angle)
    turn = random.choice(side)
    turn(a)

screen = Screen()
screen.exitonclick()

