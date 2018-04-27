import turtle

def create_star():
    wn = turtle.Screen()
    wn.title("Aula 2. Exercício 4.9.9")
    t = turtle.Turtle()
    t.hideturtle()
    t.left(108)
    t.forward(100)
    for i in range(4):
        t.left(144)
        t.forward(100)

create_star()
