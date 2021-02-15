from turtle import Turtle
FONT = ("Courier", 24, "normal")
FONT2 = ("Courier", 50, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.color((222, 201, 136))
        self.hideturtle()
        self.penup()
        self.goto(-540, 250)
        self.write(f"Level = {self.l_score}", align="left", font=FONT)

    def lx_score(self):
        self.l_score += 1
        self.clear()
        self.write(f"Level = {self.l_score}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 235)
        self.color(0, 0, 0)
        self.write("GAME OVER", align="center", font=FONT2)
