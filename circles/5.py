from turtle import*

speed(30)
bgcolor("black")

# circles

for i in range(150):
    color("red")
    circle(i)
    color("blue")
    circle(i*1.2)
    right(10)
    color("violet")
    circle(i*0.8)
    right(2)
    forward(10)

# end
exitonclick()