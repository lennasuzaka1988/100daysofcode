from turtle import Turtle
FONT = ("Courier", "80", "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 175)
        self.write(self.left_score, font=FONT, align="center")
        self.goto(100, 175)
        self.write(self.right_score, font=FONT, align="center")

    def left_point(self):
        self.left_score += 1
        self.clear()
        self.update_scoreboard()

    def right_point(self):
        self.right_score += 1
        self.clear()
        self.update_scoreboard()




