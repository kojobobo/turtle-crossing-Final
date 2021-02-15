from turtle import Turtle
FONT = ("Courier", 28, "normal")
FONT2 = ("Courier", 50, "bold")
FONT3 = ("Courier", 16, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.color((222, 201, 136))
        self.hideturtle()
        self.penup()


    def score(self):
        self.goto(-540, 250)
        self.write(f"Level = {self.l_score}", align="left", font=FONT)

    def lx_score(self):
        self.l_score += 1
        self.clear()
        self.goto(-540, 250)
        self.write(f"Level = {self.l_score}", align="left", font=FONT)
        self.instruct()

    def game_over(self):
        self.goto(0, 235)
        self.color(0, 0, 0)
        self.write("GAME OVER", align="center", font=FONT2)


    def instruct(self):
        self.goto(275, 275)
        self.write("Press Up to go forward", align="Left", font=FONT3)
        self.goto(275, 250)
        self.write("Press Down to go back", align="Left", font=FONT3)

    def restart(self):
        self.color((222, 201, 136))
        self.clear()
        self.instruct()
        self.score()
