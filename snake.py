from turtle import Turtle
STARTING_POSITION=[(0,0),(-20,0),(-40,0)]    # IN python we have to create constant with capital letters
MOVE_DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:
    
    def __init__(self):
        self.segment=[]
        self.create_snake()
        self.head=self.segment[0]
    
    def create_snake(self):
        for position in STARTING_POSITION:
           self.addsegment(position)
                                                    
    def addsegment(self,position):                                        # the two def are create snake
        new_segment=Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)

    def extend(self):                          # adds new segment to the snake 
        self.addsegment(self.segment[-1].position())    # so here position() is a method in turtle class thats get postion of the turtle

    def move(self):                                  # these function to move correct direction
        for seg_num in range(len(self.segment)-1,0,-1):  #so here it is written by range(start , stop , step)
            new_x=self.segment[seg_num-1].xcor()
            new_y=self.segment[seg_num-1].ycor()
            self.segment[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
    def up(self):
        if self.head.heading()!=DOWN:  # these condition is for to move only head torward staright not  not to move in at a time oppoitise direction towards head only 
            self.head.setheading(UP)                        
      
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
            
    