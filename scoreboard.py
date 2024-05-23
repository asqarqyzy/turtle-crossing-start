from turtle import Turtle
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-280, 260)
        self.hideturtle()
        self.level = 0
        self.show()

    def show(self):
        self.clear()
        self.write(f"Level: {self.level}", False, "left", FONT)

    def level_up(self):
        self.level += 1
        self.show()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game over", False, "center", FONT)

