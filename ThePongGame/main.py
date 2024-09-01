from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time

screen = Screen()
screen.title("Abhiram's Pong")
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

game_on = True
while game_on:
	time.sleep(ball.move_speed)
	ball.move()
	screen.update()

	if ball.ycor() > 280 or ball.ycor() < -280:
		ball.bounce()

	if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
		ball.collision()
	elif ball.xcor() > 380:
		ball.restart()
		scoreboard.left_point()

	if ball.distance(left_paddle) < 50 and ball.xcor() < -320:
		ball.collision()
	elif ball.xcor() < -380:
		ball.restart()
		scoreboard.right_point()

screen.exitonclick()
