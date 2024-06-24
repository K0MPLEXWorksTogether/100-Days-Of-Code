from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_xcor = randint(a=-280, b=280)
        random_ycor = randint(a=-280, b=280)
        self.goto(x=random_xcor, y=random_ycor)