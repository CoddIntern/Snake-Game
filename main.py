
from snake import Snake

def snake_game():
    timmy = Snake()
    timmy.move_snake()
    timmy.my_screen.exitonclick()

snake_game()