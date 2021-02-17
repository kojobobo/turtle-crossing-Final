from turtle import Turtle
FONT = ("Courier", 16, "normal")
FONT2 = ("Courier", 100, "bold")
FONT3 = ("Courier", 16, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()

    def score(self):
        self.color((222, 201, 136))
        self.goto(-575, 250)
        self.write(f"Level = {self.l_score}\nMax laps = {self.high_score}", align="left", font=FONT)
        self.goto(275, 275)
        self.write("Press Up to go forward", align="Left", font=FONT3)
        self.goto(275, 250)
        self.write("Press Down to go back", align="Left", font=FONT3)
        self.goto(-25, 250)
        self.write(f"Help our Turtle friend cross the road\nHe needs the excersize  ", align="Center", font=FONT3)


    def lx_score(self):
        self.l_score += 1
        self.clear()
        self.score()

    def game_over(self):
        if self.l_score > self.high_score:
            self.high_score = self.l_score
            self.clear()
            self.score()
        self.goto(0, -50)
        self.color(0, 0, 0)
        self.write("GAME OVER", align="center", font=FONT2)
        self.color((222, 201, 136))
        if self.l_score > self.high_score:
            self.high_score = self.l_score

    def restart(self):
        self.clear()
        self.l_score = 0
        self.score()

    def gameon(self):
        self.clear()
        self.score()
