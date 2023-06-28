import turtle
from turtle import Turtle, Screen
import random

timmy_the_turtle=Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color(	"#FF1493","#5F9EA0")
timmy_the_turtle.shapesize(+4)
turtle.colormode(255)
# colours=["cornflower blue","deep pink","aquamarine","medium purple","red","cadet blue","gold","coral","dark green"]
# i=0
# while i < 4:
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)
#     i+=1
# i = 0
# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()
#
# Draw geometry objects from triangle to decahedron
#
def random_colour():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r,g,b)
    return random_colour

def draw_shape(sides, angle):
    x = range(1, sides +1)

    for n in x:
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)


for sides in range(3, 11):
   angle = int(360/sides)
   timmy_the_turtle.color(random_colour())
   draw_shape(sides,angle)



screen = Screen()
screen.exitonclick()
#

# for _ in range(4):
#      timmy_the_turtle.forward(100)
#      timmy_the_turtle.right(90)
#
# for _ in range(5):
#      timmy_the_turtle.forward(100)
#      timmy_the_turtle.right(72)
# #
# for _ in range(6):
#      timmy_the_turtle.forward(100)
#      timmy_the_turtle.right(60)
#
#
# #
# for _ in range(7):
#      timmy_the_turtle.forward(100)
#      timmy_the_turtle.right(51.4)
# #
# for _ in range(8):
#      timmy_the_turtle.forward(100)
#      timmy_the_turtle.right(45)
#
# for _ in range(9):
#      timmy_the_turtle.forward(100)
#      timmy_the_turtle.right(40)
#
# for _ in range(10):
#      timmy_the_turtle.forward(100)
#      timmy_the_turtle.right(36)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
