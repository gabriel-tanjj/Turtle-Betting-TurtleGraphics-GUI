from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle do you think will win the race?").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [180, 108, 36, -36, -108, -180]
all_turtles = []

is_race_on = False

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            print(f"The winning turtle is {winning_color}")
            if winning_color == user_bet:
                print("You've won the bet!")
            else:
                print("You've lost the bet!")
            is_race_on = False
        random_distance = random.randint(1, 10)
        turtle.forward(random_distance)



screen.exitonclick()