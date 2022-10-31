import turtle as tt
from turtle import Turtle, Screen
import random

t = Turtle()
# t.pensize(10)
# t.speed(10)
t.speed(11)
tt.colormode(255)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)


colors = ["green", "brown", "grey", "lightgreen", "yellow", "lightblue", "orange"]

directions = [0, 90, 180, 270]

# 3 Spiral Circles


def draw_spirograph(gap_size):
    for i in range(int(360/gap_size)):
        t.color(random_color())
        t.setheading(t.heading()+gap_size)
        t.circle(100)


draw_spirograph(5)

# 2 Random Walk
# def walk_random():
#     # angle = random.randint(0, 3) * 90
#     angle = random.choice(directions)
#     t.setheading(angle)
#     t.forward(25)
#
# for i in range(50):
#     # t.color(random.choice(colors))
#     t.color(random_color())
#     walk_random()


# 1 Draw the shapes
# def draw_shape(i):
#     for j in range(i + 3):
#         t.forward(100)
#         t.right(360 / (i + 3))
#
# for _ in range(7):
#     t.color(random.choice(colors))
#     draw_shape(_)

screen = Screen()
screen.exitonclick()
