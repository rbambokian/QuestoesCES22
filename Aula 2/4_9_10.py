import turtle 

def create_five_stars():
    wn = turtle.Screen()
    wn.title("Aula 2. Exercício 4.9.10")
    wn.bgcolor("lightgreen")
    t = turtle.Turtle()
    t.color("coral")
    t.hideturtle()
    t.penup()
    t.setpos(-200,0)
    t.showturtle()
    t.pendown()

    for j in range(5):
        for i in range(5):
            t.forward(100)
            t.right(144)
        t.penup()
        t.forward(350)
        t.right(144)
        t.pendown()

    t.hideturtle()
    window.mainloop()
    
create_five_stars()

