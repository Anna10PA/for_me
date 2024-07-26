from turtle import*

bgcolor("black")
width(2)
speed(100)

# squares

for i in range(18):
    for colors in ["red", "blue", 'dark green', "yellow"]:
        color(colors)
        for i in range(4):
            forward(200)
            left(90)
        forward(2*i)
        left(i+5)

# end
exitonclick()
