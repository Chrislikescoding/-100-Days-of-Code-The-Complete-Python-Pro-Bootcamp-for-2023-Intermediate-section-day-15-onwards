import colorgram
import turtle
import random
from turtle import Turtle, Screen

# after importing turtlr set colormode to use a tuple of 3 numeric values for red,green and blue
turtle.colormode(255)

tim=Turtle()
rgb_colors=[]
# colorgarm was used to create the list of colour tuples, taken from the included image of a Damien Hirst image
colors=colorgram.extract('image.jpg', 80)

color_list=[(239, 231, 235), (227, 236, 230), (198, 162, 101), (63, 90, 126), (139, 170, 191),
            (136, 91, 50), (132, 28, 53), (219, 205, 120), (29, 40, 65), (78, 16, 35), (149, 62, 85),
            (162, 155, 53), (184, 141, 158), (132, 182, 145), (48, 56, 99), (180, 97, 107),
            (56, 35, 22), (68, 130, 106), (98, 118, 166), (82, 148, 159), (221, 175, 187), (169, 206, 166),
            (90, 151, 96), (185, 97, 80), (163, 200, 213), (179, 188, 211), (80, 70, 39), (131, 37, 27),
            (45, 73, 76), (219, 177, 170), (24, 43, 43), (49, 88, 21)]

# remove pen and set co-ordinats to lower and further left as start position
tim.penup()
tim.goto(-200,-200)
tim.speed("fastest")
tim.hideturtle()

# simply draw a dot
def draw_dot():
        tim.dot(20,random_colour())
        tim.forward(50)

# retrieve random colour

def random_colour():
    colour = random.choice(color_list)
    return colour

#do 10 rows 10 times
for i in range(0,10):
    for x in range(0,10):
        draw_dot()

#reposition the turtle  then repeat

    tim.back(500)
    tim.left(90)
    tim.forward(50)
    tim.right(90)



screen = Screen()
screen.exitonclick()


