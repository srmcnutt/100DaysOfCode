from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.x = x
        self.speed("fastest")
        self.color("white")
        self.shape("square")
        self.penup()
        self.pensize(20)
        self.shapesize(5, 1)
        self.goto(x, 0)

    def go_up(self, steps):
        y = self.ycor() + 10
        self.sety(y)

    def go_down(self):
        y = self.ycor() - 10
        self.sety(y)

