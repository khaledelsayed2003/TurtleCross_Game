from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager, STARTING_MOVE_DISTANCE
import time

screen = Screen()
screen.setup(width= 600, height= 600)
screen.title("TurtleCross — A Python Turtle Game")
screen.tracer(0)


player = Player()

screen.listen()
screen.onkey(fun= player.go_up, key="Up")

car = CarManager()


game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    
    car.create_car()
    car.move_cars()
        
    
    #Detect when the Turtle collides with a Car 
    for c in car.all_cars:
        if player.distance(c) <= 20:
            game_is_on = False
            
    
    #Detcet successful crossing & increase level(increase cars speed)
    if player.is_player_reach_goal():
        player.go_to_starting_position()
        car.level_up()
        
    
    
            

        
    
    




























screen.exitonclick()