from turtle import Turtle

class Ball(Turtle):

	def __init__(self):
		super().__init__()
		self.penup()
		self.shape("square")
		self.color("white")
		self.move_speed = 0.1

		self.xincre = 10
		self.yincre = 10

	def move(self):
		self.goto(self.xcor() + self.xincre, self.ycor() + self.yincre)

	def bounce(self):
		self.yincre *= -1

	def collision(self):
		self.xincre *= -1
		self.move_speed *= 0.9

	def restart(self):
		self.goto(0, 0)
		self.collision()
		self.move_speed = 0.1
