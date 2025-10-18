from turtle import Turtle, Screen
from player import Player
import time

screen = Screen()
screen.setup(width= 600, height= 600)
screen.title("TurtleCross — A Python Turtle Game")
screen.tracer(0)


player = Player()

screen.listen()
screen.onkey(fun= player.move_forward, key="Up")





game_over = False
while not game_over:
    time.sleep(0.07)
    screen.update()
    
    
    




























screen.exitonclick()