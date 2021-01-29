from turtle import Turtle

FONT = ("Courier", 10, "bold")


class writer(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()

    def writer(self, state, position):
        self.goto(position)
        self.write(state, align="left", font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align="left", font=FONT)
