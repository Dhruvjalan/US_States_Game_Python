import turtle, pandas
data = pandas.read_csv("50_states.csv")
STATE_LIST = data["state"].to_list()
dict = data.to_dict()
print(dict)
final_dict ={}

for i in range(50):
    final_dict[dict['state'][i]]= (dict['x'][i], dict['y'][i])

print(final_dict)

# print(x_list, y_list)

screen = turtle.Screen()
screen.title("US STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
correct = 0
play = True
guessed_states=[]
unguessed_states=[]

while len(guessed_states)<50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 states Guessed Correctly",prompt="Type the name of state").title()
    if answer.title() in data["state"].to_list():
        print("CORRECT",answer)
        print(final_dict[answer])
        state = turtle.Turtle()
        state.penup()
        state.ht()
        state_data = data[data.state == answer]
        state.goto(state_data.x.item(), state_data.y.item())
        state.write(arg=answer, move=False,font=('Aerial',8,'normal'))



        guessed_states.append(answer)

    if answer=='Exit':
        break


for i in STATE_LIST:
    if i not in guessed_states:
        unguessed_states.append(i)


unguessed_states_dict= {
    "You Didnt Guess": unguessed_states
}

new = pandas.DataFrame(unguessed_states_dict)

screen.exitonclick()