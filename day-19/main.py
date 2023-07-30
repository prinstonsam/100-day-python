from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

screen.textinput(title="Make your bet", prompt="color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

tims = []
start_point = -100


def check(val_tims):
    for tim_item in val_tims:
        if tim_item.xcor() > 250:
            return True
    return False


def find_won_tim(val_tims):
    result = None
    for tim_item in val_tims:
        if tim_item.xcor() > 250:
            result = tim_item
    return result


for i in range(0, 5):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    y = start_point + (i + 1) * 50
    tim.goto(x=-230, y=y)
    tims.append(tim)

is_race_on = True

won_tim = None
while is_race_on:
    for tim in tims:
        rand_distance = random.randint(0, 10)
        tim.forward(rand_distance)
    if check(tims):
        won_tim = find_won_tim(tims)
        is_race_on = False


print(f"Won: ${won_tim.color()}")

screen.exitonclick()
