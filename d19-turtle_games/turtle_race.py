from turtle import Turtle, Screen
from random import randint

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

tim = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="make your bet", prompt="Which turtle will wind the race?  Enter a color: "
)


turtle_list = []
turtle_names = []


def spawn_turtles():
    y_pos = 125
    for color in colors:
        # create one turtle for each color and place at the starting line
        turtle_name = color + "_turtle"
        turtle_names.append(turtle_name)
        turtle_name = Turtle(shape="turtle")
        turtle_list.append(turtle_name)
        turtle_name.color(color)
        turtle_name.penup()
        turtle_name.goto(x=-230, y=y_pos)
        y_pos -= 50


spawn_turtles()

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        turtle.forward(randint(1, 10))
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won!  the {winner} turtle is the winner")
            else:
                print(f"The {winner} turtle is the winner.  Try again.")


screen.exitonclick()
