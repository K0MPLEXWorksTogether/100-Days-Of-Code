from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """
    The class snake is responsible for all the properties and functionalities
    of the in-game snake.
    """

    def __init__(self):
        self.snake_angle = 0
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_body_part(position)

    def reset(self):
        for part in self.snake_body:
            part.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

    def add_body_part(self, pos):
        new_body_part = Turtle("square")
        new_body_part.color("white")
        new_body_part.penup()
        new_body_part.goto(pos)
        new_body_part.speed("fast")
        self.snake_body.append(new_body_part)

    def extend(self):
        self.add_body_part(self.snake_body[-1].position())

    def move(self):
        """
        Moves the snake object created.
        :return: None.
        """
        for body_part_number in range(len(self.snake_body) - 1, 0, -1):
            new_xcor = self.snake_body[body_part_number - 1].xcor()
            new_ycor = self.snake_body[body_part_number - 1].ycor()
            self.snake_body[body_part_number].goto(x=new_xcor, y=new_ycor)

        self.snake_body[0].forward(MOVE_DISTANCE)

    def up(self):
        """
        Moves the snake up.
        :return: None.
        """
        if self.snake_angle != DOWN:
            self.head.setheading(UP)
            self.snake_angle = UP

    def down(self):
        """
        Moves the snake down.
        :return: None.
        """
        if self.snake_angle != UP:
            self.head.setheading(DOWN)
            self.snake_angle = DOWN

    def left(self):
        """
        Moves the snake left.
        :return: None.
        """
        if self.snake_angle != RIGHT:
            self.head.setheading(LEFT)
            self.snake_angle = LEFT

    def right(self):
        """
        Moves the snake right.
        :return: None.
        """
        if self.snake_angle != LEFT:
            self.head.setheading(RIGHT)
            self.snake_angle = RIGHT
