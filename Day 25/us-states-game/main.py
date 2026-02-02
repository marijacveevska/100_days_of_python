from turtle import Turtle, Screen
import pandas as pd

turtle = Turtle()
screen = Screen()
screen.title("U.S. States Game")

data_path = "Day 25/us-states-game/50_states.csv"
df = pd.read_csv(data_path)

image_path = "Day 25/us-states-game/blank_states_img.gif"
screen.addshape(image_path)
turtle.shape(image_path)
all_states = df["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title = f"{len(guessed_states)}/ 50 States", prompt = "What's another state's name? ")
    guess = answer_state.title()

    if answer_state == "exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)

        # export_data = pd.DataFrame(missing_states,columns=["states"])
        # export_data.to_csv("Day 25/us-states-game/states_to_learn.csv")
        break

    if guess in all_states:
        guessed_states.append(guess)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df["state"] == guess]
        x = state_data["x"].item()
        y = state_data["y"].item()
        t.goto(x,y)
        t.write(guess)

#screen.exitonclick()