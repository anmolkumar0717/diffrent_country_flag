import turtle
t1=turtle.Turtle()
t1.penup()
t1.goto(-250,195)
t1.color("black")
t1.pendown()
t1.begin_fill()
t1.color("red")
for i in range(2):
    t1.fd(500)
    t1.right(90)
    t1.fd(130)
    t1.right(90)
t1.end_fill()

t1.goto(-250,65)
t1.color("black")
t1.pendown()
t1.begin_fill()
t1.color("yellow")
for i in range(2):
    t1.fd(500)
    t1.right(90)
    t1.fd(130)
    t1.right(90)
t1.end_fill()
t1.goto(-250,-65)
t1.color("black")
t1.pendown()
t1.begin_fill()
t1.color("green")
for i in range(2):
    t1.fd(500)
    t1.right(90)
    t1.fd(130)
    t1.right(90)
t1.end_fill()
t1.hideturtle()
