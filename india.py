import turtle
import time
t=turtle.Turtle()
t.color("blue")
t.pensize(4)
t.penup()
t.goto(0,-65)
t.pendown()
t.circle(65)
t.left(90)
t.fd(130)
t.penup()
for i in range(24):
    t.bk(65)
    t.left(15)
    t.pendown()
    t.fd(65)
t.penup()
t.goto(-250,195)
t.right(90)
t.color("black")
t.pendown()
t.begin_fill()
t.color("orange")
for i in range(2):
    t.fd(500)
    t.right(90)
    t.fd(130)
    t.right(90)
t.end_fill()
t.penup()
t.goto(-250,-65)
t.pendown()
t.begin_fill()
t.color("green")
for i in range(2):
    t.fd(500)
    t.right(90)
    t.fd(130)
    t.right(90)
t.end_fill()
t.hideturtle()
