from turtle import Turtle, Screen

my_turtle = Turtle()


def turn_right():
    my_turtle.right(5)


def turn_left():
    my_turtle.left(5)


def move_backward():
    my_turtle.back(10)


def move_forward():
    my_turtle.forward(10)


my_screen = Screen()


def clear_screen():
    my_screen.reset()


my_screen.onkey(key="w", fun=move_forward)
my_screen.onkey(key="a", fun=turn_left)
my_screen.onkey(key="s", fun=move_backward)
my_screen.onkey(key="d", fun=turn_right)
my_screen.onkey(key="c", fun=clear_screen)


my_screen.listen()
my_screen.exitonclick()
