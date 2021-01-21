from turtle import Turtle, Screen

tim = Turtle()
tim.speed("fastest")
screen = Screen()


def left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def forward():
    tim.forward(10)


def backward():
    tim.backward(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(fun=forward, key="w")
screen.onkey(fun=backward, key="s")
screen.onkey(fun=left, key="a")
screen.onkey(fun=right, key="d")
screen.onkey(fun=clear, key="c")


screen.exitonclick()
