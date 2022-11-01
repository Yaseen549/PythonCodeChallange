from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)
# def turn_left():
#     tim.left(10)
def turn_left():
    tim.setheading(tim.heading() + 10)
def turn_right():
    tim.right(10)
def move_backward():
    tim.backward(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)  # either declare as key= and func= or
screen.onkey(clear, "c")     # you have to use function in front
screen.exitonclick()