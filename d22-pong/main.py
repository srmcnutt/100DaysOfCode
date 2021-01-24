import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.screensize(800, 600)
screen.bgcolor("black")
screen.title("Pong!")
screen.tracer(0)


r_paddle = Paddle(x=350)
l_paddle = Paddle(x=-350)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detect collision with wall
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()

    # detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() < 340) or (
        ball.distance(l_paddle) < 50 and ball.xcor() < -340
    ):
        ball.bounce_x()

    # detect left or right paddle miss
    if ball.xcor() > 380:
        ball.reset_position()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_score += 1
        scoreboard.refresh()

screen.exitonclick()

