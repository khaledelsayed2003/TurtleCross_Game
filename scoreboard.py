from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("green")
        self.hideturtle()
        self.penup()
        self.goto(-230, 265)
        self.write(f"Level: {self.score}", align= "center", font=("Courier", 15, "normal"))
        
    
    
    def refresh(self):
        self.clear()    # to delete the previous score
        self.score += 1
        self.write(f"Level: {self.score}", align= "center", font=("Courier", 15, "normal")) 
        
    
    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write(f"Game Over", align= "center", font=("Courier", 25, "normal")) 