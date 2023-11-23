import turtle
from turtle import Turtle
import random

timmy = Turtle()
turtle.colormode(255)


def pic_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_color = (r, g, b)
    return random_color


timmy.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(pic_colour())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(2)
screen = turtle.Screen()
screen.exitonclick()
