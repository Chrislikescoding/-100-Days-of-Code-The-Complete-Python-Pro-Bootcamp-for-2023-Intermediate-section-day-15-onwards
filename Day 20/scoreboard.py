from turtle import Turtle
ALIGNMENT="center"
FONT=("courier",24,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 280)
        self.hideturtle()
        self.high_score=self.retrieve_txt()
        self.score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        print(f"high score {self.high_score}")
        self.clear()
        self.write(f"Score:{self.score} High score {self.high_score}:", align=ALIGNMENT, font=FONT)


    def update_txt_file(self):
        with open ('data.txt',mode='w') as file:
            file.write(str(self.high_score))

    def retrieve_txt(self):
        with open ('data.txt',mode='r') as file:
            return int(file.readline())

    def increase_score(self):
        self.score+=1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
           self.high_score = self.score
           self.update_txt_file()
           self.score=0
           self.update_scoreboard()
