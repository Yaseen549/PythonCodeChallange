import random
import turtle
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(500,400)

cross_line = Turtle()
cross_line.hideturtle()
cross_line.penup()
cross_line.goto(x=200, y=-200)
cross_line.pendown()
cross_line.goto(x=200, y=200)

colors = ["red", "green", "orange", "yellow", "blue", "purple"]
y_pos = [-100, -60, -20, 20, 60, 100]

bet_color = screen.textinput("Enter user color", "Tutle color")

all_turtles = []
for each_turtle in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[each_turtle])
    new_turtle.goto(x=-230, y=y_pos[each_turtle])
    all_turtles.append(new_turtle)

if bet_color:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 180:
            is_race_on = False
            win_color = turtle.pencolor()
            if win_color == bet_color:
                print(f"{win_color} won!")
            else:
                print(f"{bet_color} lost!")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()