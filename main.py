from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)  # this is for to move change dom't want to see that moving different well wewnat to see them in single row to move

snake=Snake()
food=Food()
score=Score()
screen.listen()
screen.onkey(snake.up,"Up")   # here snake is object and . for attribute to get the function 
# generally we use if we have same file then we call direct fuction here we have different file so 
# we declare object and function 
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on =True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # Detect the collosion of the food 
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    

    # Detect the collosion with wall
    if snake.head.xcor()>280 or  snake.head.xcor() <-280 or snake.head.ycor() >280 or snake.head.ycor() <-280:
        game_is_on=False
        score.reset()
        score.gameover()
       
    
    # detect thecollosion with snake tail
    for segment in snake.segment:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on=False
            score.reset()
            score.gameover() 

  

screen.exitonclick()