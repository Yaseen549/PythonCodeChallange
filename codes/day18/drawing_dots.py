import random
import turtle as tt
from turtle import Turtle, Screen
# from colorgram import *
#
# colors = colorgram.extract('codes/day18/heirst-painting.jpg', 30)
# colors = colorgram.extract('heirst-painting.jpg', 30)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.b
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

tt.colormode(255)
t = Turtle()
t.penup()
xaxis, current_pos = -200, -200
t.setpos(xaxis, current_pos)
t.pendown()
t.hideturtle()
colors = [(253, 248, 248), (254, 252, 252), (231, 242, 242), (198, 32, 32), (250, 17, 17), (39, 189, 189), (38, 67, 67), (238, 5, 5), (229, 46, 46), (27, 158, 158), (215, 12, 12), (15, 16, 16), (199, 10, 10), (242, 252, 252), (244, 165, 165), (229, 122, 122), (73, 31, 31), (60, 8, 8), (224, 211, 211), (222, 8, 8), (10, 61, 61), (17, 43, 43), (47, 232, 232), (11, 239, 239), (79, 215, 215), (237, 222, 222), (73, 169, 169), (78, 201, 201), (50, 244, 244), (3, 40, 40)]
t.pensize(5)


def random_color():
    return random.choice(colors)


def change_position(yaxis):
    t.setpos(xaxis, yaxis)


def draw_dots():
    for i in range(10):
        t.color(random_color())
        t.dot(20)
        t.up()
        t.fd(50)

for j in range(10):
    draw_dots()
    current_pos += 50
    change_position(current_pos)


screen = Screen()
screen.exitonclick()