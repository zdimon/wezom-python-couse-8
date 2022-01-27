print('Simple Calculator')
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
oper = input("Operation: ")
if oper == '+':
    print('Сумма равна =', num1 + num2)
elif oper == '-':
    print('Разность равна =', num1 - num2)
elif oper == '/':
    print('Деление чисел равно =', num1 / num2)
elif oper == '*':
    print('Умножение чисел равно =', num1 * num2);
else:
    print('Нет такой операции')