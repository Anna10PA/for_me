name=input("persone name: ")
last_name=input("persone lastname: ")
money=float(input("How many: "))
if money >0:
    cource=input("lari or dolari: ")

    if cource=="lari":
        perm=input("Are you sure you want to transfer "+str(money)+" "+ "₾ "+"to "+name+" "+last_name+"? " )
        if perm=="yes":
            x=int(input("enter your card code: "))
            print("Registration completed, thanks for using")
        if perm=="no":
            print("goodbye")
    elif cource=="dolari":
        perm=input("Are you sure you want to transfer "+str(money)+" "+ "$ to"+name +" " + last_name+"? "  )
        if perm=="yes":
            x=int(input("enter your card code: "))
            print("Registration completed, thanks for using")
        if perm=="no":
            print("goodbye")
elif money <=0:
    print("ERROR")


