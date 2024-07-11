
#calculator 

number_1=float(input("please enter first number: "))
operation=input("please enter the operator you want (+ - * / ** // or %): ") 
number_2=float(input("please enter second number: "))

# conditions 
if operation== "+": 
    result = number_1 + number_2
    print(result)

elif operation=="-":
    result = number_1 - number_2
    print(result)

elif operation=="*":
    result = number_1 * number_2
    print(result)

elif operation=="/":
    result = number_1 / number_2
    print(result)

elif operation=="**":
    result = number_1 ** number_2
    print(result)

elif operation=="//":
    result = number_1 // number_2
    print(result)

elif operation=="%":
    result = number_1 % number_2
    print(result)

# end
