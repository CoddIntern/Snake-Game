
import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=-0.5, stretch_wid=-0.5)
        self.color("blue")
        self.speed("fastest")
        self.default_y = int((600/2 - 30))
        self.default_x = int((600/2 - 30))
        self.refresh()

    def refresh(self):
        y_var = random.randint(-self.default_y, self.default_y - 30)
        x_var = random.randint(-self.default_x, self.default_x)
        self.goto(x_var, y_var)
