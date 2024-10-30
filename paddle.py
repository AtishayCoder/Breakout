from turtle import Turtle

MOVE_DISTANCE = 10
Y_POS = -200


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.goto(0, Y_POS)
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len=4)
        self.width = 80
        self.height = 10

    def go_left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        self.goto(new_x, Y_POS)

    def go_right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        self.goto(new_x, Y_POS)
