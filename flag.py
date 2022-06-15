import turtle
from turtle import*

def flag():
    #screen for output
    screen = turtle.Screen()

    # Defining a turtle Instance
    t = turtle.Turtle()
    speed(0)

    # initially penup()
    t.penup()
    t.goto(-400, 300)
    t.pendown()

    # Orange Rectangle
    #white rectangle
    t.color("green")
    t.begin_fill()
    t.forward(280)
    t.right(90)
    t.forward(580)
    t.right(90)
    t.forward(280)
    t.end_fill()


    t.penup()
    t.goto(400, -280)
    t.pendown()

    t.color("green")
    t.begin_fill()
    t.forward(280)
    t.right(90)
    t.forward(580)
    t.right(90)
    t.forward(280)
    t.end_fill()
    #to hold the
    #output window
    turtle.done()
