import turtle as t
from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()

def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.back(10)

def turn_right():
    # new_heading = timmy.heading() - 10
    # timmy.setheading(new_heading)
    timmy.right(10)

def turn_left():
    # new_heading = timmy.heading() + 10
    # timmy.setheading(new_heading)
    timmy.left(10)

def counter_clock():
    timmy.circle(50,10)

def clock():
    timmy.circle(50,-10)

def clean():
    timmy.reset()

screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=turn_left)
screen.onkey(key="d",fun=turn_right)
screen.onkey(key="e",fun=counter_clock)
screen.onkey(key="q",fun=clock)

screen.onkey(key="c",fun=clean)
screen.exitonclick()