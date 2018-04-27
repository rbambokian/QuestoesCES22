import turtle, math

def moving_turtle(t, list):
    for (x1, x2) in list:
        t.forward(x1)
        t.right(x2)

wn = turtle.Screen()
wn.title("Aula 2. Exercício 7.26.13")

tutu = turtle.Turtle()
tutu.color("black")
tutu.left(90)

moving_turtle(tutu, [(50,270), (50,270), (50,330), (50,240), (50,240), (50,0)])
tutu.penup()
tutu.hideturtle()
tutu.setpos(130, 0)
tutu.pendown()
tutu.showturtle()
tutu.left(120)
moving_turtle(tutu, [(50, 240), (50, 240), (50, 90), (50, 90), (50, 90), (50, 135), (50*math.sqrt(2), 0)])
tutu.penup()
tutu.hideturtle()
tutu.setpos(0, 100)
tutu.left(180)
tutu.pendown()
tutu.showturtle()
moving_turtle(tutu, [(50, 90), (100, 90), (50, 135), (50*math.sqrt(2), 270), (50*math.sqrt(2), 270), (50*math.sqrt(2), 270), (50*math.sqrt(2), 135), (50, 90), (50, 0)])
tutu.penup()
tutu.hideturtle()
tutu.setpos(180, 100+50*math.sqrt(2))
tutu.pendown()
tutu.showturtle()
moving_turtle(tutu, [(50, 270), (50, 315), (50*math.sqrt(2), 225), (100, 135), (50*math.sqrt(2), 135), (100, 135), (50*math.sqrt(2), 45), (50, 90), (100, 90), (50, 135), (50*math.sqrt(2), 0)])
