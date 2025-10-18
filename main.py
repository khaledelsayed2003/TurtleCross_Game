from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
import time

screen = Screen()
screen.setup(width= 600, height= 600)
screen.title("TurtleCross — A Python Turtle Game")
screen.tracer(0)


player = Player()

screen.listen()
screen.onkey(fun= player.go_up, key="Up")

car = CarManager()


game_over = False
while not game_over:
    time.sleep(0.05)
    screen.update()
    car.create_car()
    car.move_cars()
    
    




























screen.exitonclick()