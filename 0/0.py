#exp 1
# three circles and a square.

import turtle
# bg 
turtle.bgcolor("blue")
pen = turtle.Turtle()
pen.shape("arrow")

# speed 
pen.speed(10)

# first circle 
pen.begin_fill()
pen.color("grey")
pen.circle(140)
pen.end_fill()

# second circle 
pen.begin_fill()
pen.color("yellow")
pen.circle(70)
pen.end_fill()

# first square
pen.begin_fill()
pen.penup()
pen.fillcolor("green")
pen.forward(90)
pen.pendown()
pen.forward(90)
pen.right(90)
pen.forward(90)
pen.right(90)
pen.forward(90)
pen.right(90)
pen.forward(90)
pen.end_fill()
pen.hideturtle()

# third circle
pen=turtle.Turtle()
pen.begin_fill()
pen.color("brown")
pen.forward(300)
pen.circle(100)
pen.end_fill()
pen.hideturtle()

turtle.done()

