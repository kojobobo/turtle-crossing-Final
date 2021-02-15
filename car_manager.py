from turtle import Turtle

import random
MOVE_INCREMENT = 1
SQUISH_ZONE = range(-20, 20)
C_LIST = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []

    def create_cars(self):
        for y in range(-205, 250, 60):
            new_car = Turtle(shape="square")
            new_car.penup()
            color = random.choice(C_LIST)
            xcor = random.randint(-350, 350)
            new_car.color(color)
            new_car.goto(xcor, y)
            new_car.setheading(180)
            new_car.shapesize(1.5, 1.5, 2)
            new_car.speed(0)
            self.cars.append(new_car)

    def move(self, MOVE_INCREMENT, turtle_y):

        for car in self.cars:
            car_top = int(car.ycor() - 15)
            car_bottom = int(car.ycor() + 15)
            car_lane = range(car_top, car_bottom)
            car_location = car.xcor()

            if turtle_y in car_lane and car_location in SQUISH_ZONE:
                print('squish')
                game_over = True
                return game_over

            car.forward(MOVE_INCREMENT)

            if car.xcor() < -400:
                car.setx(400)

    def done(self):
        for car in self.cars:
            car.goto(1000, 1000)
