import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
race_on = True
user_pet = screen.textinput('Input your pet', 'type your pet color')

y = 100
all_turtles = []
for i in range(0, len(colors)):
    tim = Turtle(shape='turtle')
    tim.pu()
    tim.color(colors[i])
    tim.goto(x=-230, y=y)
    y -= 50
    all_turtles.append(tim)

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 250:
            race_on = False
            if turtle.pencolor() == user_pet:
                print('congratulations your pet has won')
            else:
                print('Sorry your pet has lost good luck another time')

        random_dis = random.randint(0, 10)
        turtle.forward(random_dis)

screen.exitonclick()

