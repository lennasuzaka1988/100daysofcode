# from turtle import Turtle
#
# Y_SEG = [320, 310]
#
# class MidLine(Turtle):
#
#     def __init__(self):
#         super().__init__()
#         self.segments = [320, 310]
#         self.coordinates = []
#         self.line_segments()
#         self.mid_pen()
#
#     def mid_pen(self):
#         for little_turtle in self.coordinates:
#             line_segment = Turtle()
#             line_segment.hideturtle()
#             line_segment.penup()
#             line_segment.speed("fastest")
#             line_segment.shape("square")
#             line_segment.color("white")
#             line_segment.shapesize(0.5)
#             line_segment.setposition(little_turtle)
#             line_segment.showturtle()
#             line_segment.setheading(270)
#
#     def line_segments(self):
#         y = 30
#         for _ in range(22):
#             for i in Y_SEG:
#                 new_y = i - y
#                 self.segments.append(new_y)
#             y += 30
#         for segs in self.segments:
#             self.coordinates.append((0, segs))
