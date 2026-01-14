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
timmy.speed("fastest")
timmy.pensize(2)


# Challenge 5 - Spirograph

# for x in range(72):
#         timmy.color(random_color())
#         timmy.circle(100)
#         timmy.setheading(timmy.heading() + 5)


def draw_spirograph(size_of_gap):
    for x in range(int(360/size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)
    
draw_spirograph(5)

screen.exitonclick()
