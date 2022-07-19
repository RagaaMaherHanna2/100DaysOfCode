import random
import turtle

# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()
tim = turtle.Turtle()
turtle.colormode(255)


def gen_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_shape(side_num):
    for _ in range(side_num):
        tim.forward(100)
        tim.right(abs(360 / side_num))


def draw_all():
    for side_num in range(3, 11):
        tim.color(gen_color())
        draw_shape(side_num)


def draw_circles(s):
    tim.speed('fastest')
    for i in range(int(360 / s)):
        i += 10
        tim.color(gen_color())
        tim.circle(100)
        tim.left(i)
    turtle.done()


draw_circles(5)
