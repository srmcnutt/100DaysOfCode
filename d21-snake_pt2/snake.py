from turtle import Turtle

X = 0
Y = 0
PENSIZE = 20
FORWARD = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.snake_length = 3
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.pensize(PENSIZE)
        new_segment.pencolor("white")
        new_segment.fillcolor("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

        # spawn our starter snake

    def create_snake(self):
        segments = self.segments = []
        snake_length = self.snake_length
        x = X
        y = Y
        for _ in range(self.snake_length):
            self.add_segment((x, y))
            x -= 20

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.head.forward(FORWARD)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

