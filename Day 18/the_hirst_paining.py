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


screen.setup(500,500)
timmy.shape("classic")
timmy.speed("fastest")
timmy.pensize(6)

timmy.penup()
start_x = -250
start_y = -250
timmy.goto(start_x, start_y)

DOT_SIZE = 10
SPACING = 50

for col in range(10):            
    for row in range(11):        # 11 dots per line
        timmy.color(random_color())
        timmy.dot(DOT_SIZE)
        timmy.forward(SPACING)

    # move to next row
    timmy.goto(start_x, start_y + SPACING * (col + 1))


screen.exitonclick()