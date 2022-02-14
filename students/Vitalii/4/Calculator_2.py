number_1 = int(input("Введите 1 число:"))
print ("Первое число = ", number_1)
number_2 = int(input ("Введите 2 число:"))
print ("Второе число = ", number_2)
deystvie = input("Напишите на выбор: + или - или / или * ")
if deystvie == "+":
    print ("Результат = ", number_1 + number_2)
elif deystvie == '-':
    print ("Результат = ", number_1 / number_2)
elif deystvie == '*':
    print ("Результат = ", number_1 * number_2) 
elif deystvie == '/':
    if number_2 == int("0"):
        print("На ноль делить нельзя!")
    else:
        print ("Результат = ", number_1 / number_2)
        except Exception as e:
        print('Error')
        print(e)
else:
    print("Попробуйте еще раз")