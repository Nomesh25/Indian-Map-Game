import turtle
import pandas as pd

screen = turtle.Screen()
screen.setup(width=505, height=590)
screen.title("INDIAN STATE GUESSING GAME")
image = "india_map.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pd.read_csv("Book1.csv")
states = states_data["states"].to_list()
data = pd.read_csv("Book1.csv")
states_data = data.states.to_list()
guessed=[]

while(len(guessed)<29):
    answer = screen.textinput(title=f"{len(guessed)}/29 Guess the Indian State ", prompt="What's another state name?").title()
    if answer=="Exit":
        break
    if answer in states_data:

        guessed.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        state_data = data[data.states == answer]
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)


screen.exitonclick()
