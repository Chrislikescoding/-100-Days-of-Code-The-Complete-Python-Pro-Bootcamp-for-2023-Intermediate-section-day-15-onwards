import turtle
from random import randint
from turtle import Turtle, Screen

screen = Screen()

screen.setup = (800, 400)

new_turtle = ['tim', 'charlie', 'blue', 'lynx', 'lucy', 'fred']
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo']
race_is_on = False


# setting up screen

def create_turtles():
    x = -400
    y = -200
    for t in range(0, 6):
        new_turtle[t] = Turtle()
        new_turtle[t].penup()
        new_turtle[t].goto(x, y)
        new_turtle[t].color(colors[t])
        new_turtle[t].shape("turtle")
        new_turtle[t].shapesize(+3)
        y += 100


#def move_distance():


screen = Screen()

screen.setup = (800, 400)

create_turtles()

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")

if user_bet:
    race_is_on = True

while race_is_on:
    for t in range(len(new_turtle)):

        if new_turtle[t].xcor() > 230:
            winning_colour = new_turtle[t].pencolor()
            race_is_on = False
            #t=len(new_turtle) +1
            if winning_colour == user_bet:
                print(f"You've won! The {winning_colour} turtle is the winner")
            else:
                print(f"You've lost! The {winning_colour} turtle is the winner")

        new_turtle[t].forward(randint(1, 10))

screen.exitonclick()
