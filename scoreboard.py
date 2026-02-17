from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as data:
            self.high_score=int(data.read())
        self.color("white")
        self.penup()
        self.goto(x=0,y=260)
        self.hideturtle()
        self.update()
        

    def update(self):
        self.clear()
        self.write(f"score: {self.score} High Score:{self.high_score}", align="center",font=("Arial",24,"normal"))
    
    def increase_score(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
        self.score=0
        with open("data.txt" , mode="w") as file:
            file.write(f"{self.high_score}")
            
        self.update()
    
    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER.", align="center",font=("Arial",24,"normal"))
