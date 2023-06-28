import time
from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
from food import Food

screen = Screen()
screen.setup = (600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on= True

while game_is_on:
    screen.update()
    snake.move_snake()
    if snake.head.distance(food)<15:
        scoreboard.increase_score()
        food.refresh()
        snake.extend()
    if snake.head.xcor() > 360 or  snake.head.xcor()< -360 or snake.head.ycor() > 360 or  snake.head.ycor()< -360:
        scoreboard.reset()
        snake.reset()
    for piece in snake.snake_pieces:
        if piece == snake.head:
            pass
        elif snake.head.distance(piece)<10:
            scoreboard.reset()
            snake.reset()




screen.exitonclick()