import turtle as t
from random import choice, randint 

t.colormode(255)
tim = t.Turtle()
tim.pensize(10)
t.speed(9)

########### Challenge 4 - Random Walk ########
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def random_color():
    r  = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rgb = (r,g,b)
    return rgb

directions = [0,  90,  180,  270]

for _ in range (100):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(choice(directions))

