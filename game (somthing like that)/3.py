# თამაშის შექმნა (რაღაც ამდაგვარი)
# თამაშის პირობა: ამ შემთხვევაში არის ორი მოთამაშე (სამკუთხედი და კვადრატი). და ორივე გადაადგილდება კამათზე რაც ამოვა ის გამრავლებული 30-ზე.

import turtle
import random 
turtle.bgcolor("black")
a=turtle.Turtle()
b=a.clone()
 

# player_1 (cyan)
a.shape("arrow")
a.shapesize(2)
a.pensize(10)
a.begin_fill()
a.fillcolor()
a.color("cyan")
a.end_fill()
a.penup()
a.goto(-500, 200)
a.pendown()


# player_2 (light blue)
b.pensize(10)
b.shape("square")
b.shapesize(2)

# b=input("Hello player_2 choose color: red, blue, green: ")
# if b=="red":
#     b.colorfill("red")

# elif b=="blue":
#     b.colorfill("blue")

# elif b=="green":
#     b.colorfill("green")

b.begin_fill()
b.color("light blue")
b.penup()
b.goto(-500, -200)
b.pendown()
b.end_fill()

# circle (finish) for player_1 (a)
a.pensize(3)
a.penup()
a.forward(800)
a.right(90)
a.forward(20)
a.pendown()
a.circle(100)
a.left(90)
a.penup()
a.goto(-500, 200)
a.pendown()

# circle (finish) for player_2 (b)
b.pensize(3)
b.penup()
b.forward(800)
b.right(90)
b.forward(20)
b.pendown()
b.circle(100)
b.left(90)
b.penup()
b.goto(-500, -200)
b.pendown()

# dice number
dice = [1,2,3,4,5,6,7,8,9,10]

# propose dice number*30
for i in range(30):
    if a.pos() >= (300, 200):
        print("Player_1 Win")
        break
    elif b.pos()>=(300, -200):
        print("Player_2 win")
        break
    else: 
        a_turn=input("Player_1 press enter to role dice")    
        dice_outcome = random.choice(dice)
        print("Result is ") 
        print(dice_outcome)
        print("step will be ")
        print(30*dice_outcome)
        a.forward(30*dice_outcome)

        b_turn=input("Player_2 press enter to role dice")    
        dice_outcome = random.choice(dice)
        print("Result is ") 
        print(dice_outcome)
        print("step will be ")
        print(30*dice_outcome)
        b.forward(30*dice_outcome)

turtle.done()