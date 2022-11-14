import time
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (0, -20), (0, -40)]
RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270
FORWARD = 20


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for snake_object in STARTING_POSITIONS:
            self.append_snake_body(snake_object)

    def append_snake_body(self, snake_object):
        snake_segment = Turtle()
        snake_segment.color("white")
        snake_segment.shape("square")
        snake_segment.penup()
        snake_segment.goto(snake_object)
        self.segments.append(snake_segment)

    def extend(self):
        self.append_snake_body(self.segments[-1].position())

    def move(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_seg_x = self.segments[segment_num - 1].xcor()
            new_seg_y = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(new_seg_x, new_seg_y)
        self.head.forward(FORWARD)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
