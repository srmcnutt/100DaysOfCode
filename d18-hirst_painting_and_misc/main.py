import colorgram
import turtle
from random import choice

color_list = [
    (131, 166, 205),
    (222, 148, 106),
    (31, 42, 61),
    (199, 134, 147),
    (165, 59, 48),
    (140, 184, 162),
    (39, 105, 157),
    (238, 212, 89),
    (152, 58, 66),
    (217, 81, 70),
    (169, 29, 33),
    (236, 165, 156),
    (50, 112, 90),
    (35, 61, 55),
    (17, 97, 71),
    (156, 33, 30),
    (231, 160, 165),
    (53, 44, 49),
    (170, 188, 221),
    (57, 51, 48),
    (189, 100, 110),
    (31, 60, 109),
    (103, 127, 161),
    (34, 151, 209),
    (174, 200, 188),
    (65, 66, 56),
]

turtle.colormode(255)

tim = turtle.Turtle()
tim.penup()
tim.speed("fastest")
tim.hideturtle()

tim.setposition(-300, -300)

for _ in range(5):
    for _ in range(10):
        tim.dot(20, choice(color_list))
        tim.forward(50)

    tim.dot(20, choice(color_list))
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)

    for _ in range(10):
        tim.dot(20, choice(color_list))
        tim.forward(50)

    tim.dot(20, choice(color_list))
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(0)

screen = turtle.Screen()
screen.exitonclick()
# rgb_colors = []
# colors = colorgram.extract("./image.jpg", 30)
# for color in colors:
#     r  = color.rgb.r
#     g  = color.rgb.g
#     b  = color.rgb.b
#     new_color=(r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
