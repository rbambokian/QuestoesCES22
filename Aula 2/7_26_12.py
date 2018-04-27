import turtle, math

def moving_turtle(t, list):
    for (x1, x2) in list:
        t.forward(x1)
        t.right(x2)

wn = turtle.Screen()
wn.title("Aula 2. Exercício 7.26.12")

tutu = turtle.Turtle()
tutu.color("black")
tutu.left(90)

moving_turtle(tutu, [(50, 30), (50, 120), (50, 75), (50*math.sqrt(2), 225), (50, 270), (50, 270), (50, 225), (50*math.sqrt(2), 0)])


