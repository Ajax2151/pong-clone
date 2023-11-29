from turtle import Turtle
MOVE_DISTANCE = 10
BALL_COLOR = ["chartreuse", "red", "light sky blue"]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color(BALL_COLOR[0])
        self.shape("circle")
        self.penup()
        self.x_move = MOVE_DISTANCE
        self.y_move = MOVE_DISTANCE
        self.move_speed = 0.1

    def move(self):
        """Moves ball towards top right corner of screen until interrupted"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_bounce(self):
        """Bounces ball off of top or bottom walls"""
        self.y_move *= -1

    def color_change(self):
        """Change color of ball depending on which
        paddle it last hit or if the ball has been reset"""
        if self.xcor() == 0 and self.ycor() == 0:
            self.color(BALL_COLOR[0])
        elif self.xcor() > 329:
            self.color(BALL_COLOR[1])
        elif self.xcor() < -329:
            self.color(BALL_COLOR[2])

    def paddle_bounce(self):
        """Bounces ball off of side paddles and changes color of ball"""
        self.x_move *= -1
        self.move_speed *= 0.9
        self.color_change()

    def reset_position(self):
        """Resets ball to center after each point,
        reverses direction towards paddle of player who just scored."""
        self.home()
        self.move_speed = 0.1
        self.paddle_bounce()


