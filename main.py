import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from board import create_b

MOVE_INCREMENT = 10
screen = Screen()
screen.colormode(255)
screen.setup(width=1200, height=600)
screen.tracer(0)
screen.title("FroggerZ")
screen.listen()
print(screen.turtles())
create_b()
turtle = Player()
scoreboard = Scoreboard()
screen.onkeypress(turtle.move_u, "Up")
screen.onkeypress(turtle.move_d, "Down")
game_is_on = True
car = CarManager()
cars = car.create_cars()


while game_is_on:
    time.sleep(0.1)
    turtle_y = turtle.ycor()
    game_over = car.move(MOVE_INCREMENT, turtle_y)

    if game_over:
        scoreboard.game_over()
        game_is_on = False

    if turtle.ycor() > 260:
        scoreboard.lx_score()
        car.create_cars()
        turtle.restart()
        MOVE_INCREMENT += 3
        time.sleep(0.01)

    screen.update()

screen.exitonclick()