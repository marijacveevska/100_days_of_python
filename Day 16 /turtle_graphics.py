import _tkinter
from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("brown")
timmy.forward(100) # steps
timmy.left(120) # angle
timmy.forward(50)

# attribute of the Screen
my_screen = Screen()
print(my_screen.canvheight)

# method
my_screen.exitonclick()


