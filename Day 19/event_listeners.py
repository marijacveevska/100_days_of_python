# Event Listeners are a programming concept used to wait for something to happen (an event) and then react to it by running code.
    # “When X happens, do Y.” Executes a callback function when that event occurs
    # An event can be : A mouse click, A key press, A message arriving, A timer finishing


import turtle as t
from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()

def move_forward():
    timmy.forward(10)


screen.listen()
screen.onkey(key="space",fun=move_forward)
screen.exitonclick()