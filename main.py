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
screen.title("TurtleZ")
screen.listen()
print(screen.turtles())
create_b()
turtle = Player()
scoreboard = Scoreboard()
scoreboard.score()
# scoreboard.instruct()
screen.onkeyrelease(turtle.move_u, "Up")
screen.onkeyrelease(turtle.move_d, "Down")
game_is_on = True
car = CarManager()
cars = car.create_cars()


while game_is_on:
    time.sleep(0.1)
    turtle_y = turtle.ycor()
    game_over = car.move(MOVE_INCREMENT, turtle_y)

    if game_over:
        scoreboard.game_over()
        replay = screen.textinput("You have Squished our turtle friend", "Enter 1 to restart, 2 to continue 3 to quit:")

        if replay == "1":
            car.done()
            scoreboard.restart()
            car.create_cars()
            turtle.restart()
            screen.listen()

        elif replay == "2":
            turtle.restart()
            scoreboard.gameon()
            screen.listen()

        else:
            turtle.bye()

    if turtle.ycor() > 250:
        scoreboard.lx_score()
        car.create_cars()
        turtle.restart()
        MOVE_INCREMENT += 3
        time.sleep(0.01)

    screen.update()

screen.exitonclick()
