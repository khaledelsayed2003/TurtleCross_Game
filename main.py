from turtle import Turtle, Screen

screen = Screen()
screen.setup(width= 600, height= 600)
screen.title("TurtleCross — A Python Turtle Game")



turtle = Turtle()
turtle.shape("turtle")
turtle.penup()
turtle.setheading(90)
turtle.goto(0, -280)


def move_forward():
    turtle.forward(10)


screen.listen()
screen.onkey(fun= move_forward, key="Up")
































screen.exitonclick()