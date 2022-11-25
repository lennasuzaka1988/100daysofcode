from turtle import Turtle
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(open("D:/Python Projects/100daysofcode/day_24_write_and_open_files/high_score.txt", "r").read())
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

    def high_score_write(self):
        high_score_file_write = open("D:/Python Projects/100daysofcode/day_24_write_and_open_files/high_score.txt", "w")
        with high_score_file_write as f:
            f.write(f"{self.high_score}")
