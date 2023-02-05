import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)

tim=Turtle()
tim.speed("fastest")


def draw_circle(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_colour())
        tim.circle(100)
        current_heading=tim.heading()
        tim.setheading(tim.heading() + size_of_gap)

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r,g,b)
    return colour


draw_circle(15)


screen = Screen()
screen.exitonclick()