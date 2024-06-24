import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.title("Abhiram's Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer()

snake = Snake()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
food = Food()
scoreboard = ScoreBoard()

game_is_on = True
count = 0
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increment()
        scoreboard.write()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for body_part in snake.snake_body[1:]:
        if snake.head.distance(body_part) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
