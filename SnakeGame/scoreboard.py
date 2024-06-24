from turtle import Turtle


class ScoreBoard:

    def __init__(self):
        self.score = 0
        self.scoreboard = Turtle()
        self.scoreboard.penup()
        self.scoreboard.color("white")
        self.scoreboard.hideturtle()
        self.write()

    def increment(self):
        self.score += 1
        self.write()

    def write(self):
        self.scoreboard.clear()
        self.scoreboard.goto(0, 250)
        self.scoreboard.write(f"Score: {self.score}", align="center", font=("Monospace", 18, "normal"))
        self.scoreboard.penup()

    def game_over(self):
        self.scoreboard.goto(0, 0)
        self.scoreboard.write("GAME OVER", align="center", font=("Monospace", 18, "bold"))