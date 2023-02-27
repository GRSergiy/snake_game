from turtle import Turtle

POSITIONS = [(0,0), (-20,0), (-40,0)]
#starting positon of the snake

MOVE_DISTANCE = 20
#the snake moves forward for 20

UP=90
DOWN=270
LEFT=180
RIGHT=0
#directions in angles

class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]


    def create_snake(self):
    #create the list of turtle - snake in the center of the screen

        for position in POSITIONS:
            new = Turtle(shape="square")
            new.color("white")
            new.penup()
            new.goto(position)
            self.snakes.append(new)

    def neo(self):
    #this module adds a new turtle to the snake body

        news = len(self.snakes) - 1
        x_new = self.snakes[news].xcor()
        y_new = self.snakes[news].ycor()
        once = Turtle(shape="square")
        once.color("white")
        once.penup()
        once.goto(x_new, y_new)
        self.snakes.append(once)


    def move(self):
    #this module rearranges turtles, so the snake looks like a whole

        for new in range(len(self.snakes)-1,0,-1):
            x_new = self.snakes[new - 1].xcor()
            y_new = self.snakes[new - 1].ycor()
            self.snakes[new].goto(x_new, y_new)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
    #prevent to move in the opposite side and to listen the command

        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def reset(self):
    #this module sends away snake which is out of the game and creates a new one

        for one in self.snakes:
            one.goto(1000,1000)
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]