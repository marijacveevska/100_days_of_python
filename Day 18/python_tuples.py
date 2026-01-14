# Tuples are a collection of ordered and immutable elements. Once created, you cannot change or modify the elements of a tuple. 
# Python programming often uses tuples when fixed data structures are needed

my_tuple = (1,3,5,7)
print(my_tuple[2])

list(my_tuple)
print(my_tuple)

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


for x in range(0,4):
    timmy.color(random_color())
    timmy.right(90)
    timmy.forward(100)

screen = Screen()
screen.exitonclick()
