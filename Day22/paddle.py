import time
from turtle import Turtle, Screen

x=350
y=0

class Paddle(Turtle):
   def __init__(self,x,y):
       super().__init__()
       self.shape("square")
       self.color("white")
       self.shapesize(stretch_wid=5, stretch_len=1)
       self.penup()
       self.goto(x, y)



   def up(self):
      new_y = self.ycor() +20
      self.goto(self.xcor(),new_y)

   def down(self):
       new_y = self.ycor() - 20
       self.goto(self.xcor(), new_y)

