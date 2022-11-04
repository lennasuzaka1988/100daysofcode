import turtle as t
import random

tiny = t.Turtle()
screen = t.Screen()
screen.setup(720, 480)

t.colormode(255)
tiny.shape("turtle")
tiny.color("teal")
tiny.turtlesize(2)
tiny.speed("fastest")
tiny.pen(pensize=1)


directions = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tiny.pen(pencolor=(r, g, b))


def spirograph(gap):
    for circ in range(int(360 / gap)):
        random_color()
        tiny.circle(100)
        tiny.seth(tiny.heading() + gap)


spirograph(1)
screen.exitonclick()
