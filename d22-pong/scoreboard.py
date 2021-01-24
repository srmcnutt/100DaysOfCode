from turtle import Turtle
import random


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.penup()
        self.color("yellow")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.clear()
        self.goto(-50, 300)
        self.write(
            f"Player1: {self.l_score}       Player2: {self.r_score}",
            font=("Arial", 20, "bold"),
            align="center",
        )

        def l_point(self):
            self.l_score += 1
            self.refresh()

        def r_point(self):
            self.r_score += 1
            self.refresh()
