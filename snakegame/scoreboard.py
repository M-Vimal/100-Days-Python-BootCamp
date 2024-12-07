from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.penup()
        self.speed('fastest')
        self.goto(0,270)
        self.count = 0
        self.updateScore()
    

    def updateScore(self):
        self.write(f"score {self.count}", move=False, align="center", font=("Arial", 16, "bold"))

    def increaseScore(self):
        self.count+=1
        self.clear()
        self.updateScore()

    def gameOver(self):
        self.goto(0,0)
        self.write(f"game over", move=False, align="center", font=("Arial", 16, "bold"))




