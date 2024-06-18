from turtle import Turtle, Screen
from random import randint

STARTING_XCOR = -230
STARTING_YCOR = -70

my_screen = Screen()
my_screen.setup(width=500, height=400)
user_bet = my_screen.textinput(
    title="Make Your Bets!",
    prompt="Which turtle do you think will win? (All turtles are in the color of VIBGYOR, except I.)"
).lower()
is_game_on = False

turtles = []
for _ in range(6):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtles.append(turtle)

colors = ["purple", "blue", "green", "yellow", "orange", "red"]
turtle_count = 0
for turtle in turtles:
    turtle.color(colors[turtle_count])
    turtle.goto(STARTING_XCOR, STARTING_YCOR + (turtle_count * 30))
    turtle_count += 1

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_game_on = False
            if user_bet == turtle.pencolor():
                print(f"You've won! The {user_bet.capitalize()} turtle indeed won the race.")
            else:
                print(f"Sorry, but you have lost the game. {(turtle.pencolor()).capitalize()} turtle is the winner.")
        else:
            random_distance = randint(1, 10)
            turtle.forward(random_distance)

my_screen.exitonclick()
