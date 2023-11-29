from turtle import Turtle
MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.setheading(90)
        self.penup()
        self.goto(position)

    def up(self):
        """Moves paddle towards top of screen"""
        self.forward(MOVE_DISTANCE)

    def down(self):
        """Moves paddle towards bottom of screen"""
        self.back(MOVE_DISTANCE)

