import turtle

wn = turtle.Screen()
wn.bgcolor("coral")
tutu = turtle.Turtle()
tutu.color("blue violet")
tutu.hideturtle()
wn.title("Aula 1. Exercício 11")

tutu.left(108)
tutu.forward(150)
for i in range(4):
    tutu.left(144)
    tutu.forward(150)
