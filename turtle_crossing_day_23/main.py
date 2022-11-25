import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)

timmy = Player()
screen.listen()
screen.onkeypress(timmy.up, "Up")
game_is_on = True
car = CarManager()
scoreboard = Scoreboard()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()

    for current_car in car.cars:
        if current_car.distance(timmy) < 20:
            game_is_on = False
            scoreboard.game_over()
    if timmy.ycor() >= 280:
        timmy.if_goal_line()
        scoreboard.update_scoreboard()
        car.reset_cars()
        car.level_speed()
        time.sleep(1)
screen.exitonclick()
