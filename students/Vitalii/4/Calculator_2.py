number_1 = int(input("Введите 1 число:"))
print ("Первое число = ", number_1)
number_2 = int(input ("Введите 2 число:"))
print ("Второе число = ", number_2)
deystvie = input("Напишите на выбор: + или - или / или * ")
if deystvie == "+":
    print ("Результат = ", number_1 + number_2)
if deystvie == '-':
    print ("Результат = ", number_1 - number_2)
if deystvie == '/':
    print ("Результат = ", number_1 / number_2)        
if deystvie == '*':
    print ("Результат = ", number_1 * number_2) 
else:
    print("Попробуйте еще раз")