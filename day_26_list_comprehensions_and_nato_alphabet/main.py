# Convert guess to title case
# Check if guess is in 50 states
# Write correct guesses on map
# Use loop to allow user to keep guessing
# Record guesses in list
# Track score

import turtle
import pandas as pd
import time

font = ("Arial", 10, "bold")

with open("50_states.csv") as states:
    states_and_coordinates = pd.read_csv(states)
    df = pd.DataFrame(states_and_coordinates)

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "../day_26_list_comprehensions_and_nato_alphabet/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

states_list = df.state.to_list()
coordinates_x = df.x.to_list()
coordinates_y = df.y.to_list()

state_coordinates = list(zip(coordinates_x, coordinates_y))

recorded_correct_states = []
states_to_learn = []
score = 0

game = True
while game:
    answer = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()
    if answer in recorded_correct_states:
        score += 0

    elif answer in states_list:
        states_id = states_list.index(answer)
        state_coord = state_coordinates[states_id]

        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        state.pencolor("dark blue")
        state.goto(state_coord)
        state.write(answer, font=font, align="center")

        recorded_correct_states.append(answer)
        score += 1

    if score == 50:
        gg = turtle.Turtle()
        gg.hideturtle()
        gg.penup()
        print("You know all 50 states! Congrats!")
        game = False

states_to_learn = [a_state for a_state in states_list if a_state not in recorded_correct_states]

csv_data = pd.DataFrame({"states": states_to_learn})
export_states_to_learn = csv_data.to_csv("states_to_learn.csv", index=False)


screen.exitonclick()