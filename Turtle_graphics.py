import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

timmy = Turtle()


def turn_around():
    timmy.shape("turtle")
    timmy.color("blue")
    # timmy.forward(100)
    # timmy.right(90)
    # timmy.forward(100)
    # timmy.right(90)
    # timmy.forward(100)
    # timmy.right(90)
    # timmy.forward(100)

    # for t in range(10):
    #     timmy.forward(10)
    #     timmy.penup()
    #     timmy.forward(10)
    #     timmy.pendown()


#
# def tri_angle():
#     for i in range(3):
#         timmy.forward(100)
#         timmy.right(120)
#
#
# def draw_square():
#     for i in range(4):
#         timmy.forward(100)
#         timmy.right(90)
#
#
# def draw_penta():
#     for i in range(5):
#         timmy.forward(100)
#         timmy.right(72)
#
#
# def draw_hexa():
#     for i in range(6):
#         timmy.forward(100)
#         timmy.right(60)
#
#
# def draw_hepta():
#     for i in range(7):
#         timmy.forward(100)
#         timmy.right(51.43)
#
# def draw_octa():
#     for i in range(8):
#         timmy.forward(100)
#         timmy.right(45)
#
# def draw_nona():
#     for i in range(9):
#         timmy.forward(100)
#         timmy.right(40)
#
# def draw_deca():
#     for i in range(12):
#         timmy.forward(100)
#         timmy.right(30)
#
# tri_angle()
# draw_square()
# draw_penta()
# draw_hexa()
# draw_hepta()
# draw_octa()
# draw_nona()
# draw_deca()

def pic_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_color = (r, g, b)
    return random_color


directions = [0, 90, 180, 270]

timmy.pensize(15)
timmy.speed(100)

for i in range(201):
    timmy.color(pic_colour())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))

#
# def draw_shape(num_slides):
#     angle = 360 / num_slides
#     for _ in range(num_slides):
#         timmy.forward(100)
#         timmy.right(angle)
#
#
#
# for shape_slide_n in range(3, 11):
#     timmy.color(random.choice(colors))
#
#     draw_shape(shape_slide_n)


#
screen = Screen()
screen.exitonclick()
