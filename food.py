from turtle import Turtle
import random



class Food(Turtle):
#create a food for the snake in a random position

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len= 0.5, stretch_wid=0.5)
        self.refresh()
        self.color("red")
        self.speed("fastest")


    def refresh(self):
    #recreate the food in a random position

        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)