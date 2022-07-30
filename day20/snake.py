from turtle import Turtle, Screen
import time


class Snake:

    def __init__(self):
        self.snake_segments = self.create_snake()

    def create_snake(self):
        i = 0
        snake_segments = []
        for _ in range(3):
            sub_snack = Turtle(shape='square')
            sub_snack.color('white')
            sub_snack.penup()
            sub_snack.setpos((0 - i, 0))
            snake_segments.append(sub_snack)
            i += 20
        return snake_segments

    def snake_move(self):
        for segment in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[segment - 1].xcor()
            new_y = self.snake_segments[segment - 1].ycor()
            self.snake_segments[segment].goto(new_x, new_y)

        self.snake_segments[0].forward(20)

    def up(self):
        self.snake_segments[0].setheading(90)

    def down(self):
        self.snake_segments[0].setheading(270)

    def left(self):
        self.snake_segments[0].setheading(180)

    def right(self):
        self.snake_segments[0].setheading(0)
