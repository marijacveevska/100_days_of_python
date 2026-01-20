from turtle import Screen, Turtle
from paddle import Paddle
import time
import random

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle = Paddle()

screen.listen()
screen.onkey(key="Up",fun=paddle.up)
screen.onkey(key="Down",fun=paddle.down)

game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.1)
    paddle.move()



screen.exitonclick()