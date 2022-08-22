import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

data = pandas.read_csv("50_states.csv")
list_of_states = data["state"].to_list()

# Read once during first run.
# x_coordinates = data["x"].to_list()
# y_coordinate = data["y"].to_list()

game_on = True
guessed_states = []

while len(guessed_states) <= 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's the state name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in list_of_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in list_of_states:
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
        state_row = data[data.state == answer_state]
        x_coordinates = int(state_row.x)
        y_coordinate = int(state_row.y)
        state_name = turtle.Turtle()
        state_name.hideturtle()
        state_name.penup()
        state_name.goto(x=x_coordinates, y=y_coordinate)
        state_name.write(answer_state)

    screen.update()

turtle.mainloop()


