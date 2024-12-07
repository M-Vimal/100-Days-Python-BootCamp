from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.tracer(0)


snake = Snake()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

food = Food()
score = ScoreBoard()
game = False
while not game:
    screen.update()
    time.sleep(0.10)
    snake.move()


    #to detect food collision
    if snake.head.distance(food) < 15:
        food.refresh() 
        score.increaseScore()

    #to detect wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.xcor() < -280:
        game = True
        score.gameOver()















screen.exitonclick()