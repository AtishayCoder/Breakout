from turtle import Turtle
import random

COLORS = ['red', 'orange', 'yellow', 'green', 'pink', 'blue', 'aquamarine']


class Brick(Turtle):
    def __init__(self, position_to_create):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(position_to_create)
