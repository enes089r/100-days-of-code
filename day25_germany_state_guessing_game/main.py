import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=500, height=593)
image = "germany_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("germany_states.csv")

# Dil secimi: DE (Almanca) veya EN (Ingilizce)
lang = screen.textinput(title="Sprache / Language",
                        prompt="Sprache waehlen / Choose language (DE/EN):")
lang = (lang or "DE").strip().upper()
if lang not in ("DE", "EN"):
    lang = "DE"

col = "state_de" if lang == "DE" else "state_en"
all_states = data[col].to_list()
guessed_states = []

if lang == "DE":
    title_tpl = "{n}/16 richtig"
    prompt_txt = "Wie heisst ein Bundesland?"
else:
    title_tpl = "{n}/16 correct"
    prompt_txt = "Name a German state:"

while len(guessed_states) < 16:
    answer = screen.textinput(title=title_tpl.format(n=len(guessed_states)),
                              prompt=prompt_txt)
    if answer is None:
        break
    answer = answer.title()

    if answer == "Exit":
        missing = [s for s in all_states if s not in guessed_states]
        pandas.DataFrame(missing).to_csv("states_to_learn.csv")
        break

    match = data[(data["state_de"].str.title() == answer) |
                 (data["state_en"].str.title() == answer)]

    if len(match) > 0:
        official = match[col].item()
        if official not in guessed_states:
            guessed_states.append(official)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(match.x.item(), match.y.item())
            t.write(official, align="center", font=("Arial", 8, "normal"))

screen.exitonclick()
