import time
from turtle import Turtle, Screen
from food import Food
from scoreboard import Score

class Snake:
    def __init__(self):
        """Initializing screen attributes"""
        self.my_screen = Screen()
        self.my_screen.title("Snake!!!")
        self.default_y = 600
        self.default_x = 600
        self.my_screen.setup(height=self.default_y, width=self.default_x)
        self.my_screen.bgcolor("black")
        self.my_screen.tracer(0)
        self.UP = 90
        self.DOWN = 270
        self.LEFT = 180
        self.RIGHT = 0
        self.snake_object = []
        self.STARTING_POSITIONS = [(0, 0), (0, -20), (0, -40)]


    def create_snake(self):
        """Creating a snake from multiple snake objects"""
        for position in self.STARTING_POSITIONS:
            self.create_objects(position)

    def create_objects(self, position):
        t = Turtle(shape="square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.snake_object.append(t)


    def extend_snake(self):
        self.create_objects(self.snake_object[-1].position())

    def move_snake(self):
        """Function to keep snake moving"""
        self.create_snake()
        snake = self.snake_object
        still_playing = True
        head = snake[0]
        food = Food()
        score = 0
        scoreboard = Score()

        while still_playing:
            self.my_screen.update()
            time.sleep(0.1)
            for snake_object in range(len(snake) -1, 0, -1):
                new_x = snake[snake_object - 1].xcor()
                new_y = snake[snake_object - 1].ycor()
                snake[snake_object].goto(new_x, new_y)

            head.forward(20)


            if head.distance(food) < 15:
                food.refresh()
                self.extend_snake()
                score += 1
                scoreboard.refresh_score(score)

            # Collision with wall
            if (head.xcor() > (self.default_x/2 - 20) or head.xcor() < -(self.default_x/2 - 20)
                    or head.ycor() > (self.default_y/2 - 20) or head.ycor() < -(self.default_y/2 - 20)) :
                still_playing = False
                scoreboard.game_over()

            # Collision with tail
            for items in snake[1:]:
                if head.distance(items) < 10:
                    still_playing = False
                    scoreboard.game_over()

            self.my_screen.listen()

            def up():
                if head.heading() != self.DOWN:
                    head.setheading(self.UP)
            def down():
                if head.heading() != self.UP:
                    head.setheading(self.DOWN)
            def left():
                if head.heading() != self.RIGHT:
                    head.setheading(self.LEFT)
            def right():
                if head.heading() != self.LEFT:
                    head.setheading(self.RIGHT)


            self.my_screen.onkey(up, "Up")
            self.my_screen.onkey(down, "Down")
            self.my_screen.onkey(left, "Left")
            self.my_screen.onkey(right, "Right")
