import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")
# screen.onkey(player.go_left, "Left")
# screen.onkey(player.go_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carmanager.create_car()
    carmanager.move_cars()

    # detect collision
    for car in carmanager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # player reached other side
    if player.is_at_finish_line():
        player.go_to_start()
        carmanager.level_up()
        scoreboard.increase_level()
        scoreboard.refresh()


screen.exitonclick()