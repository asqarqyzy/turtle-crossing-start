import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("The Turtle Crossing")

player = Player()

screen.listen()
screen.onkeypress(fun=player.move, key="Up")

car_manager = CarManager()
scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.cars_move()
    if player.ycor() > 280:
        player.start()
        scoreboard.level_up()
        car_manager.car_speed_add()
    for car in car_manager.cars:
        if player.distance(car) < 20:
            car_manager.restart()
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()