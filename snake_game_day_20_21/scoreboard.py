from turtle import Turtle
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 220)
        self.color("white")
        self.write(f"Score: {self.score} High Score: {self.high_score}", font=FONT, align="center")

    def new_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", font=FONT, align="center")

    def game_over(self):
        self.clear()
        self.write("Game Over. \n", font=FONT, align="center")
        self.write(f"Final Score: {self.score}", font=FONT, align="center")

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.new_score()

    def score_increase(self):
        self.score += 1
        self.new_score()