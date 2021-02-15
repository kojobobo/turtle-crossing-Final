from turtle import Turtle
import random

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
C_LIST = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        color = random.choice(C_LIST)
        self.color(color)
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.shapesize(1, 1, 1)
        self.speed(0)

    def move_u(self):
        self.forward(20)

    def move_d(self):
        self.back(20)

    def restart(self):
        self.goto(STARTING_POSITION)

    def bye(self):
        self.bye()
