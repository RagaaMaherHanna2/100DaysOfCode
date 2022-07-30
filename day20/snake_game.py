import time
from turtle import Turtle, Screen
from snake import Snake
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
new_snake = Snake()

screen.listen()
screen.onkey(new_snake.up, 'Up')
screen.onkey(new_snake.down, 'Down')
screen.onkey(new_snake.left, 'Left')
screen.onkey(new_snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    new_snake.snake_move()


screen.exitonclick()
