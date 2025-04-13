
from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.t = Turtle()
        self.t.hideturtle()
        self.t.color("white")
        self.t.speed("fastest")
        self.t.penup()
        self.default_y = 600
        self.default_x = 600

    def refresh_score(self, score):
        self.t.clear()
        self.t.goto(x=0, y=(self.default_y/2 - 30))
        self.t.write(f"Your Score: {score}",
                align="center", font=("Arial", 16, "bold"))

    def game_over(self):
        self.t.goto(x=0, y=0)
        self.t.write(f"GAME OVER",
                align="center", font=("Arial", 16, "bold"))

