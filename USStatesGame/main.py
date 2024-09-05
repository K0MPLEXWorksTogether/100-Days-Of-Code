import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
screen.setup(height=600, width=800)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

us_states_data = pandas.read_csv("50_states.csv")
us_states = us_states_data.state.to_list()

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()


guessed_states = []
while len(guessed_states) < 50:
	guess = turtle.textinput(title=f"[{len(guessed_states)}/50] States Correct", prompt="Guess a state that belongs to the US.").title()
	if guess == "Exit":
		break
	if guess in us_states:
		guessed_states.append(guess)
		state_row = us_states_data[us_states_data.state == guess]
		writer.goto(state_row.x.item(), state_row.y.item())
		writer.write(guess)

missed_states = [state for state in us_states if state not in guessed_states]
print("You missed the following states:")
for state in missed_states:
	print(state)

missed_data = pandas.Series(missed_states)
missed_data.to_csv("missed.csv")

screen.exitonclick()
