import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.move, "Up")

car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
level = 1
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) <= 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() >= 280:
        level += 1
        player.goto(0, -280) 
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()