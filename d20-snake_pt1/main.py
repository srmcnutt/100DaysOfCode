# 100 days of code day 20 - Snake pt 1.  Steven McNut 2021

from turtle import Turtle, Screen, fd
import time
from snake import Snake

screen = Screen()
screen.bgcolor("black")
screen.title("My Snake Game")
screen.setup(width=600, height=600)
screen.tracer(0)

# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()

