import turtle
import pandas
from writer import writer

states = pandas.read_csv("50_states.csv")
all_states = states.state.to_list()
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.penup()
correct_answers = []
correct_count = 0
play_game = True
writer = writer()

while play_game:
    answer_state = screen.textinput(
        title=f"{correct_count}/50 States Correct",
        prompt="What's another State's name?",
    )

    answer_state = answer_state.title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in correct_answers:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        play_game = False

    print(answer_state)
    if answer_state in states.values and answer_state not in correct_answers:
        position = []
        correct_count += 1
        correct_answers.append(answer_state)
        state = states[states.state == answer_state]
        print(state.x, state.y)
        position.append(state.iloc[0][1])
        position.append(state.iloc[0][2])
        writer.writer(state=answer_state, position=position)
        print(correct_count, position)

    if correct_count == 50:
        writer.writer(state="you won!!!!", position=(0, 0))
        play_game = False

# get screen coordinates from a click
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()

screen.exitonclick()