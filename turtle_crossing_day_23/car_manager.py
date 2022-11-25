from turtle import Turtle
import random
COLORS = ["red", "orange", "green", "yellow", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance = random.randint(0, 6)
        if chance == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            y_coord = random.randint(-250, 250)
            new_car.goto(400, y_coord)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def level_speed(self):
        self.car_speed += MOVE_INCREMENT

    def reset_cars(self):
        for car in self.cars:
            car.reset()
            car.hideturtle()
            car.penup()



