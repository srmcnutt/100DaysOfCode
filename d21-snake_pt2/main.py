# 100 days of code day 20 - Snake pt 2.  Steven McNut 2021
from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.bgcolor("black")
screen.title("My Snake Game")
screen.setup(width=600, height=600)
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

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

    # detect collision with food
    if snake.head.distance(food) < 15:
        print("nom nom nom")
        food.refresh()
        score.refresh()
        snake.extend()

    # detect collision with wall
    if (
        snake.head.xcor() > 280
        or snake.head.ycor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() < -280
    ):
        game_is_on = False
        score.game_over()

    # detect collision with tail
    for segment in snake.segments[1:]:
        # if snake.head == segment:
        #     pass
        # elif snake.head.distance(segment) < 10:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()

