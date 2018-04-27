import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tutu = turtle.Turtle()
tutu.color("blue")
tutu.shape("turtle")
wn.title("Aula 1. Exercício 12")

tutu.stamp()

for i in range(12):
    tutu.penup()
    tutu.left(30*i)
    tutu.forward(100)
    tutu.pendown()
    tutu.forward(20)
    tutu.penup()
    tutu.forward(20)
    tutu.stamp()
    tutu.forward(-140)
    tutu.left(-30*i)
