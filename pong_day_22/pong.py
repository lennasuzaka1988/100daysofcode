from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_1 = Paddle((-350, 0))
paddle_2 = Paddle((350, 0))
ball = Ball()
screen.listen()
screen.onkeypress(paddle_1.up_key, "w")
screen.onkeypress(paddle_1.down_key, "s")
screen.onkeypress(paddle_2.up_key, "Up")
screen.onkeypress(paddle_2.down_key, "Down")

scoreboard = Scoreboard()
game = True

while game:

    if paddle_1.ycor() < -240 or paddle_1.ycor() > 260:
        paddle_1.undo()

    if paddle_2.ycor() > 260 or paddle_2.ycor() < -240:
        paddle_2.undo()

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_2) < 50 and ball.xcor() > 320 or ball.distance(paddle_1) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # For right paddle or paddle_2
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.left_point()

    # For left paddle or paddle_1
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.right_point()

screen.exitonclick()
