from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.move_speed = STARTING_MOVE_DISTANCE
        self.hideturtle()

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(1,2)
            new_car.penup()

            car_color = random.choice(COLORS)
            new_car.color(car_color)
            
            x = random.randint(280,300)
            y = random.randint(-250,250)
            new_car.goto(x,y)
            self.all_cars.append(new_car)


    def move_car(self):
        for car in self.all_cars:
            car.backward(self.move_speed)

    def level_up(self):
        self.move_speed += MOVE_INCREMENT


