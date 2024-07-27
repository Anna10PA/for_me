# rock, paper, scissors 
import random
play=["scissors", "rock", "paper"]
play_output=random.choice(play)

# condition
a=input("hello, do you want play? yes or no: ")
if a=="yes":
    b=int(input("how many match do you want?: "))
elif a=="no":
    print("then goodbye")
else:
    print("I don't understang, start again")

# game
for i in range(b):
    p=input("Choose: rock, paper or scissors: ")
    # rock
    if p=="rock":
        bal=0
        print(play_output)
        if play_output=="paper":
                print("you won ")
        elif play_output=="rock":
                print("you lost")
        elif play_output=="scissors":
                print("play again")
    # paper
    elif p=="paper":
        print(play_output)
        if play_output=="paper":
                print("play again")
        elif play_output=="rock":
                print("you won")
        elif play_output=="scissors":
                print("play again")
    # scissors
    elif p=="scissors":
        print(play_output)
        if play_output=="paper":
            print("you won")
        elif play_output=="rock":
            print("play again")
        elif play_output=="scissors":
            print("play again")
    else:
        print("error")