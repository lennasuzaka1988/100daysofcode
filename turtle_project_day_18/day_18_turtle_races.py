import turtle
from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Place Your Bets!", prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_roster = []

y_coord = [-70, -40, -10, 20, 50, 80]

# Coordinate center is 0, 0 and divide the height and width of window by half
for each_turtle in range(0, 6):
    turtle_entrant = Turtle(shape="turtle")
    turtle_entrant.color(colors[each_turtle])
    turtle_entrant.penup()
    turtle_entrant.goto(x=-230, y=y_coord[each_turtle])
    turtle_roster.append(turtle_entrant)


if bet:
    race_commence = True

    while race_commence:
        for turtle_racer in turtle_roster:
            if turtle_racer.xcor() > 230:
                race_commence = False
                winner = turtle_racer.pencolor()
                if winner == bet:
                    print(f"You've won! The winner is {winner}.")
                else:
                    race_commence = False
                    print(f"Your turtle did not win. The winning turtle is {winner}.")

            speed = random.randint(0, 10)
            distance = random.randint(0, 10)
            turtle_racer.speed(speed)
            turtle_racer.forward(distance)


