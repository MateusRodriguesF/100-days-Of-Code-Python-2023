import pandas as pd
import turtle

# Variables

image = r"Day_25\brazil_game\brasil_map.gif"
data = pd.read_csv(r"Day_25\brazil_game\27_states.csv")
all_states = data.state.tolist()
guessed_states = []
screen = turtle.Screen()

# Screen configurations
screen.title("Brazil States Games")
screen.addshape(image)
turtle.shape(image)

# Logical section
while len(guessed_states) < 27:
    answer_text = screen.textinput(title=f"{len(guessed_states)}/27 States Correct", prompt="Whats another state's name?").title()
    
    if answer_text == "Exit":
        # States to learn
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)

        states_to_learn = pd.DataFrame(missing_states)
        states_to_learn.to_csv(r"Day_25\brazil_game\states_to_learn.csv")

        break

    if answer_text in all_states:
        guessed_states.append(answer_text)
        t = turtle.Turtle()
        t.hideturtle()
        t.pu()
        state_data = data[data.state == answer_text]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_text)
        # t.write(state_data.state.item()) # write the actual value of the state

screen.exitonclick()

# code to get the coordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
