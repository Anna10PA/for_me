#ex1
import turtle 
turtle.bgcolor("sienna4")

# variable
a=turtle.Turtle()
b=turtle.Turtle()
c=turtle.Turtle()
d=turtle.Turtle()

#width
a.width(7)
b.width(7)
c.width(7)
d.width(7)

# colors
a.begin_fill()
a.color("red4")
a.end_fill()

b.begin_fill()
b.color("cyan")
b.end_fill()

c.begin_fill()
c.color("Orange")
c.end_fill()

d.begin_fill()
d.color("gold4")
d.end_fill()

# start square 
b.right(90)
c.right(180)
d.left(90)
a.forward(300)
b.forward(300) 
c.forward(300)
d.forward(300)
a.right(90)
a.forward(150)
b.right(90)
b.forward(150)
c.right(90)
c.forward(150)
d.right(90)
d.forward(150)
a.right(90)
a.forward(150)
b.right(90)
b.forward(150)
c.right(90)
c.forward(150)
d.right(90)
d.forward(150)
a.right(90)
a.forward(75)
b.right(90)
b.forward(75)
c.right(90)
c.forward(75)
d.right(90)
d.forward(75)
a.right(90)
a.forward(60)
b.right(90)
b.forward(60)
c.right(90)
c.forward(60)
d.right(90)
d.forward(60)

# Circle colors
a.begin_fill()
b.begin_fill()
c.begin_fill()
d.begin_fill()

a.fillcolor("firebrick1")
b.fillcolor("chartreuse")
c.fillcolor("yellow")
d.fillcolor("springgreen4")

a.right(90)
a.circle(30)
b.right(90)
b.circle(30)
c.right(90)
c.circle(30)
d.right(90)
d.circle(30)

a.end_fill()
b.end_fill()
c.end_fill()
d.end_fill()

turtle.done()