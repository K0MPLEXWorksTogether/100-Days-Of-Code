from turtle import Turtle


class ScoreBoard:

    def __init__(self):
        self.score = 0
        with open("data.txt", "r") as data:
            self.high_score = int(data.read())
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
        self.scoreboard.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Monospace", 18, "normal"))
        self.scoreboard.penup()

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", "w") as data:
                data.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.write()

    """
    def game_over(self):
        self.scoreboard.goto(0, 0)
        self.scoreboard.write("GAME OVER", align="center", font=("Monospace", 18, "bold"))
    """