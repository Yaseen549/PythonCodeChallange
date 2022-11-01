import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(height=400, width=500)
user_bet = screen.textinput(title="Enter color", prompt="What color")
colors = ["red", "green","orange","yellow","blue", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []

for name in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.up()
    new_turtle.color(colors[name])
    new_turtle.goto(x=-230, y=y_positions[name])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you won! {winning_color} turtle is the winner")
            else:
                print(f"you lost! {winning_color} turtle is the winner")
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)

screen.exitonclick()