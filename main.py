import turtle
import pandas

screen = turtle.Screen()
screen.title("Judetele Romaniei")
screen.setup(width=1000, height=712)
image = "judete_goale.gif"
screen.addshape(image)

turtle.shape(image)

# Linii de cod pentru aflarea coordonatelor județelor

# def get_mouse_click(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click)


def write_county(x, y):
    county = turtle.Turtle()
    county.penup()
    county.hideturtle()
    county.goto(x, y)
    county.write(f"{answer}", font=("Arial", 12, "normal"))


counties = pandas.read_csv("42_counties.csv")

counties_list = counties["county"].to_list()
guessed_counties = []
score = 0

while len(guessed_counties) < 42:

    answer = screen.textinput(title=f"Correct {score}/42", prompt="Write a county (or 'exit'):").title()

    if answer == "Exit":
        break
    if answer in counties_list:
        choice = counties[counties.county == answer]
        write_county(int(choice.x), int(choice.y))
        counties_list.remove(answer)
        guessed_counties.append(answer)
        score += 1

counties_dict = {"county": counties_list}
counties_to_learn = pandas.DataFrame(counties_dict)
counties_to_learn.to_csv("./counties_to_learn.csv")
