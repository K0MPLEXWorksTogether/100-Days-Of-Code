from turtle import Turtle, Screen
from colors import new_colors
import turtle as turtle_module
from random import choice

STARTING_XCOR = -225
STARTING_YCOR = -225

turtle_module.colormode(255)
turtle = Turtle()
turtle.penup()
screen = Screen()
turtle.setposition(STARTING_XCOR, STARTING_YCOR)
turtle.hideturtle()


def create_row():
    for num in range(10):
        turtle.dot(20, choice(new_colors))
        turtle.forward(50)


increment = 50
for _ in range(10):
    create_row()

    x_axis = turtle.xcor()
    y_axis = turtle.ycor()

    turtle.setposition(STARTING_XCOR, STARTING_YCOR + increment)
    increment += 50

screen.exitonclick()
