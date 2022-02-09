print('Введите целое число(можно отрицательное), нажимайте enter')
print(' для окончания ввода просто нажмите enter')
Z = int(input('-->> '))
list_Z = []
while True:
    try:
        list_Z.append(Z)
        Z = int(input('-->> '))
    except:
        break
print(list_Z)
coeff = int(input("Введите коэффициент: "))
print(sum(list_Z)*coeff)

