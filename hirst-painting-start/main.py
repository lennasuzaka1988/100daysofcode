###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import turtle as turtle_module
import random

turtle = turtle_module.Turtle()
turtle_module.colormode(255)
window = turtle_module.Screen()

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
turtle.penup()
turtle.seth(225)
turtle.forward(300)
turtle.setheading(0)

for color in colors:
    rgb_colors.append(tuple(color.rgb))


def pen_forward():
    turtle.penup()
    turtle.fd(50)


def line():
    for _ in range(10):
        turtle.pendown()
        turtle.dot(20, random.choice(rgb_colors))
        turtle.penup()
        turtle.fd(50)


def line_odd():
    line()
    turtle.left(90)
    pen_forward()
    turtle.left(90)
    turtle.fd(50)


def line_even():
    line()
    turtle.right(90)
    pen_forward()
    turtle.right(90)
    turtle.fd(50)


for _ in range(5):
    line_odd()
    line_even()

window.exitonclick()
