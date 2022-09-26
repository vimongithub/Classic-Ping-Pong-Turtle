from turtle import Turtle
FONT = ('corier', 15, 'normal')
ALIGNMENT = "right"
class Rscore(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(position)
        self.update_score()
    def update_score(self):
        self.write(f"SCORE: {self.score}", align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

