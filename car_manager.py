from turtle import Turtle
from car_color import car_colors
from random import choice, randint

STARTING_MOVE_DISTANCE = 5

class CarManager():
    
    def __init__(self):
        self.all_cars = []
        
        
    def create_car(self):
        random_chance = randint(1, 6)  # to reduce the number of cars that have been made.
        if random_chance == 1:         
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid= 1, stretch_len= 2)
            new_car.penup()
            new_car.color(choice(car_colors))
            random_y = randint( -250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
       
        
    def move_cars(self):
        for car in self.all_cars:
            car.goto(car.xcor() - STARTING_MOVE_DISTANCE, car.ycor())