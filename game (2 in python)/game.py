# GAME (2) (მომხმარებელი ირჩევს ყველაფერს როგორც უნდა და კამათელის პრინციპით გადაადილდება.)
from turtle import*
import random

# dict
dict=[1,2,3,4,5,6]

# user:
x=input("hi, do you want play? ")
if x=="yes":
    bgcolor(input("choose bgcolor: "))
    shape(input("choose shape: "))
    width(int(input("enter width: ")))
    num=int(input("choose number more then 20: "))
    pencolor(input("enter pencolor: "))

# number and something... 
    if num<20:
        print("ERROR")
    elif num>=20:
        y=input("are you sure that you want play? ")
        if y=="yes":
            c=int(input("how many do you want? "))
            
            # range
            if c>0:
                d=input("right or left: ")
                # right
                if d=="right":
                        for i in range(c):
                            dict_output=random.choice(dict)
                            print(dict_output)
                            print("forward is "+str(dict_output*c))
                            right(90)
                            forward(dict_output*num)
                            stamp()
                # left
                elif d=="left":
                        for i in range(c):
                            dict_output=random.choice(dict)
                            print(dict_output)
                            print("forward is "+str(dict_output*c))
                            left(90)
                            forward(dict_output*num)
                            stamp()   
                # else
                else:
                    print("ERROR")
                    clearscreen() 
            # range         
            if c<=0:
                clearscreen()
                print("ERROR")
        elif y=="no":
            print("bye")
# user (2)
elif x=="no":
    print("goodbye")
else:
    print("error")
exitonclick()