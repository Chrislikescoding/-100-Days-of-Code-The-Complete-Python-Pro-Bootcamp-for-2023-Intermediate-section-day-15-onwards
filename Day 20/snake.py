import time
from turtle import Turtle, Screen
MOVE_DISTANCE=20
OFFSET_AMOUNT=20

UP = 90
DOWN=270
LEFT=180
RIGHT=0

x = 0
y = 0

class Snake():
   def __init__(self):
    self.snake_pieces = []
    self.create_snake()
    self.head=self.snake_pieces[0]


   def create_snake(self):
       for t in range(0, 3):
           self.add_snake_piece(x,y)
 #      return (snake_pieces)

   def add_snake_piece(self,x,y):
       self.snake_piece = Turtle()
       self.snake_piece.penup()
       self.snake_piece.goto(x, y)
       self.snake_piece.color("white")
       self.snake_piece.shape("square")
       x -= OFFSET_AMOUNT
       self.snake_pieces.append(self.snake_piece)

   def extend(self):
       self.add_snake_piece(x,y)

   def reset(self):
       for snake_piece in self.snake_pieces:
           snake_piece.goto(1000,1000)

       self.snake_pieces.clear()
       self.create_snake()
       self.head = self.snake_pieces[0]


   def move_snake(self):
       time.sleep(0.1)

       for piece in range(len(self.snake_pieces) - 1, 0, -1):
           new_x = self.snake_pieces[piece - 1].xcor()
           new_y =self.snake_pieces[piece - 1].ycor()
           self.snake_pieces[piece].goto(new_x, new_y)
       self.head.forward(20)

   def up(self):
       if self.head.heading() !=DOWN:
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