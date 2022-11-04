from turtle import Turtle, Screen
import turtle

tiny = Turtle()
screen = Screen()


def move_forward():
    tiny.fd(10)


def move_backward():
    tiny.back(10)


def move_left():
    tiny.left(10)


def move_right():
    tiny.right(10)


def clear():
    tiny.clear()
    tiny.penup()
    tiny.home()
    tiny.pendown()


screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='a', fun=move_left)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='d', fun=move_right)
screen.onkey(key='F1', fun=clear)
screen.exitonclick()
