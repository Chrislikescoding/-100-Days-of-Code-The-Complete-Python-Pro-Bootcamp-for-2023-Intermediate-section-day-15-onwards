from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1.5, stretch_wid=1.5)
        self.color("white")
        self.ymove=10
        self.xmove=10
        self.move_speed = 0.1



    def move(self):
        new_x = self.xcor()+ self.xmove
        new_y = self.ycor()+ self.ymove
        self.goto(new_x, new_y)

    def bounce_y(self):
        print("bounce y")
        self.ymove *=-1

    def bounce_x(self):
        print("bounce x")
        self.xmove *=-1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()