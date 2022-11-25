from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-380, 250)
        self.level = 0
        self.initial_start()

    def initial_start(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def update_scoreboard(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", font=("Arial", 24, "normal"), align="center")

