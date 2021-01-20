import turtle as t 
from random import randint

def random_color():
    r = randint(0, 255)
    g = randint(0,  255)
    b = randint(0, 255)
    rgb = (r, g, b)
    return rgb

tim = t.Turtle()
tim.pensize(5)
t.colormode(255)
t.speed(9)

def draw_spirograph(size_of_gap):
    for _ in range (int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap )
        print(tim.heading())

draw_spirograph(10)

screen = t.screen()
screen.exitonclick()