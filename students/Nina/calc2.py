indicator = 'y'
while indicator == 'y' :
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    oper = input("Operations(+/-/*/: ") 
    if oper == '+' :
        print (n1+n2)
    elif oper == '-' :
        print (n1-n2)
    elif oper == '*' :
        print (n1*n2)
    elif oper == '/' :
        print (n1/n2)
    else : 
        print ("ERROR")
    indicator = input("продолжаем? y/n: ")
else :
    print("Игра закончена")