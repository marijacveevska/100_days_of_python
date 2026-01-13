# Import Modules

import turtle
tim = turtle.Turtle()
tom = turtle.Turtle()

from turtle import Turtle, Screen
tam = Turtle()
screen = Screen()

from turtle import * # Means import everything, but don't use it often

# Aliasing Modules
import turtle as t
tim = t.Turtle()


# Modules that are not from the limited python standard library you need to pip install the packages in order to use them
# https://pypi.org/project/heroes/

import heroes
print(heroes.gen())