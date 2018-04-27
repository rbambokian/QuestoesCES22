import turtle
wn = turtle.Screen()
wn.bgcolor("coral")
tutu = turtle.Turtle()
tutu.shape("turtle")
color_list = ["yellow", "white", "purple", "blue"]
wn.title("Aula 1. Exercício 6")
for i in range(4):
    tutu.color(color_list[i])
    for j in range(3+i):
        tutu.forward(50)
        tutu.left(360/(3+i))
    tutu.penup()
    tutu.forward(200)
    tutu.left(100+10*i)
    tutu.pendown()
