from turtle import Turtle
FONT = ("Courier New", 60, "bold")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Prints and updates player scoreboards"""
        self.clear()
        self.goto((-200, 200))
        self.color("light sky blue")
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto((200, 200))
        self.color("red")
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        """Adds 1 point to left player's scoreboard"""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """Adds 1 point to right player's scoreboard"""
        self.r_score += 1
        self.update_scoreboard()

    def end_of_game(self):
        """Determines and prints winner based on scores"""
        if self.r_score > self.l_score:
            self.home()
            self.color("red")
            self.write("RED WINS!", align=ALIGNMENT, font=FONT)
        else:
            self.home()
            self.color("light sky blue")
            self.write("BLUE WINS!", align=ALIGNMENT, font=FONT)
