import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup = (800, 600)
screen.bgcolor("black")
screen.title("Pong Game")

screen.tracer(0)

l_paddle=Paddle(-350,0)
r_paddle=Paddle(350,0)
ball=Ball()

scoreboard=Scoreboard()
screen.listen()
screen.onkeypress(r_paddle.up,"Up")
screen.onkeypress(r_paddle.down,"Down")
screen.onkeypress(l_paddle.up,"w")
screen.onkeypress(l_paddle.down,"s")


game_is_on= True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 350 or ball.ycor()< -350 :
        print("top")
        ball.bounce_y()

    if ball.distance(r_paddle) < 50  and  ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        print("made contact")
        ball.bounce_x()

    if ball.xcor() > 350:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -350:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()