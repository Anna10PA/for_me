# deposit 
print("Hello")
# operation permition (1)
operation=input("Are you sure to perform the operation? ")
if operation=="yes":
    # money permition
    money=int(input("How much do you want to deposit in your account?: "))
    if money>0:
        # cource 
        cource=input("It's $ or lari: ")
        # cource $
        if cource=="$":
            print("Now in your account you have "+str(money)+"$")
            add=input("Do you want add another $?: ")
            # add money
            if add=="yes":
                new_deposit=int(input("Enter: "))
                print("Now you have "+str(money+new_deposit)+cource+", have a good day")
            elif add=="no":
                print("goodbay")
            else:
                print("ERROR")
        # cource lari
        elif cource=="lari":
            print("Now inn your account you have "+str(money)+"₾")
            add=input("Do you want add another ?: ")
            #add money
            if add=="yes":
                new_deposit=int(input("Enter: "))
                print("Now you have "+str(money+new_deposit)+cource+", have a good day")
            elif add=="no":
                print("goodbay")
            else:
                print("ERROR")
        else:
            print("Sorry, but you cannot deposit the amount of this course.")
    # money permition (2)
    elif money<=0:
        print("The operation cannot be performed")
    else:
        print("ERROR")
# operation permition (2)
elif operation=="no":
    print("goodbye")
else:
    print("ERROR")
#end
    
		
