from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(0, 0)
        self.forward(60)

    def move(self):
        new_x = self.xcor() + 10
        if new_x >= 380:
            new_x = self.xcor() - 10
        self.goto(new_x, self.ycor())
        new_y = self.ycor() + 10
        if new_y >= 380:
            new_y = self.xcor() - 10
        self.goto(self.xcor(), new_y)
