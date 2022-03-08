import random
from turtle import Turtle, Screen


def random_color():
    color_list = [(242, 230, 212), (243, 222, 234), (217, 230, 241), (222, 240, 231), (121, 177, 207), (223, 156, 89),
                  (210, 130, 165), (190, 172, 22), (233, 206, 100), (37, 114, 162)]
    new_color = random.choice(color_list)
    timmy_the_turtle.color(new_color)


screen = Screen()
screen.colormode(255)
timmy_the_turtle = Turtle()
timmy_the_turtle.speed(0)
timmy_the_turtle.pensize(5)
timmy_the_turtle.hideturtle()
timmy_the_turtle.penup()
timmy_the_turtle.goto(-200, -200)
random_color()
y = -150
count = 0


for _ in range(100):
    timmy_the_turtle.dot(20)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(50)
    random_color()
    count += 1
    if count % 10 == 0:
        timmy_the_turtle.setpos(-200, y)
        y += 50


screen.exitonclick()
