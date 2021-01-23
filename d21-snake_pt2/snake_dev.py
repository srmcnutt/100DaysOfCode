from turtle import Turtle, Screen, fd
import time

screen = Screen()
screen.bgcolor("black")
screen.title("My Snake Game")
screen.setup(width=600, height=600)
screen.tracer(0)

# initialize snake parameters
segments = []
snake_length = 3
x = 0
y = 0
pensize = 20

# spawn our starter snake
for _ in range(snake_length):
    new_segment = Turtle("square")
    new_segment.pensize(pensize)
    new_segment.pencolor("white")
    new_segment.fillcolor("white")
    new_segment.penup()
    new_segment.goto(x, y)
    x -= 20
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for segment in range(len(segments) - 1, 0, -1):
        new_x = segments[segment - 1].xcor()
        new_y = segments[segment - 1].ycor()
        segments[segment].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)


#

screen.exitonclick()

