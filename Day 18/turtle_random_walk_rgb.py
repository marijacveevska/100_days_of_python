import turtle as t
from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()

t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color


timmy.shape("classic")
timmy.speed(5)
timmy.pensize(6)

# Challenge 4 - Random Walk

side = [timmy.right,timmy.left]
angle = [0,90,180,270]

for x in range(150):
    timmy.color(random_color())
    timmy.forward(30)
    a = random.choice(angle)
    turn = random.choice(side)
    turn(a)


screen.exitonclick()
