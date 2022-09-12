from turtle import Screen, Turtle
import time
from paddle import Paddle
from ball import Ball
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

r_puddle = Paddle(x=380, y=0)
l_puddle = Paddle(x=-380, y=0)
ball = Ball()
screen.listen()
screen.onkey(r_puddle.go_up, "Up")
screen.onkey(r_puddle.go_down, "Down")
screen.onkey(l_puddle.go_up, "w")
screen.onkey(l_puddle.go_down, "x")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    ball.move()

screen.exitonclick()