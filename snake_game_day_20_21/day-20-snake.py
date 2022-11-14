import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


# Create the snake body
# Create the snake food
# Detect collision with food
# Create a scoreboard
# Detect collision with wall
# Detect collision with tail


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = Scoreboard()
segments = snake.segments
game = True
screen.listen()
screen.onkey(key='Left', fun=snake.move_left)
screen.onkey(key='Right', fun=snake.move_right)
screen.onkey(key='Up', fun=snake.move_up)
screen.onkey(key='Down', fun=snake.move_down)

while game:
    snake.move()
    screen.update()
    time.sleep(0.1)

    while snake.head.distance(food) < 15:
        food.hideturtle()
        food = Food()
        snake.extend()
        score.clear()
        score.score_increase()

    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        score.game_over()
        game = False

    for seg in segments[1:]:
        if snake.head.distance(seg) < 10:
            score.game_over()
            game = False


screen.exitonclick()

