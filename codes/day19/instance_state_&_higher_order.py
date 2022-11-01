import random
import turtle
from turtle import Turtle, Screen

is_game_on = False
screen = Screen()
screen.setup(width=500, height=400)

y_pos = [-100, -60, -20, 20, 60, 100]
colors = ["red", "green", "yellow", "orange", "purple", "blue"]

user_bet = screen.textinput(title="Turtle Game", prompt="Enter Turtle color to bet")

all_turtles = []
for num_of_turtles in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.up()
    new_turtle.color(colors[num_of_turtles])
    new_turtle.goto(x=-230, y=y_pos[num_of_turtles])
    all_turtles.append(new_turtle)

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"{winning_color} has won!")
            else:
                print(f"{user_bet} has lost")
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)


screen.exitonclick()