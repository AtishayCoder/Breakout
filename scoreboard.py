from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0

    def write_score(self):
        self.clear()
        self.goto(-60, 250)
        self.write(f"Score: {self.score}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)

    def win(self):
        self.goto(0, 0)
        self.write("You win!!!", align="center", font=FONT)


