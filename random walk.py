import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)

direction=[0,90,180,270]
tim=Turtle()

def move_shape(angle):
        tim.forward(30)
        tim.right(angle)

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r,g,b)
    return random_colour

move_turtle=True

while move_turtle== True:
   tim.width(8)
   tim.speed(10)
   tim.color(random_colour())
   angle=random.choice(direction)
   move_shape(angle)

screen = Screen()
screen.exitonclick()