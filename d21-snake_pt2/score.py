from turtle import Turtle
import random


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("yellow")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.clear()
        self.goto(-50, 270)
        self.write(f"Score: {self.score}", font=("Arial", 20, "bold"))
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.color("white")
        self.write("Game Over", align="center", font=("Arial", 20, "bold"))

