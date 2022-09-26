from turtle import Turtle
FONT = ('corier', 50, 'normal')
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.lscore = 0
        self.rscore = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.update_score()

    def update_score(self):
        self.goto(-100, 200)
        self.write(self.lscore, align="right", font=FONT)
        self.goto(100, 200)
        self.write(self.rscore, align="left", font=FONT)

    def l_point(self):
        self.lscore += 1
        self.clear()
        self.update_score()

    def r_point(self):
        self.rscore += 1
        self.clear()
        self.update_score()

