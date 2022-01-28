indicator = 'n'
while indicator == 'n':
    str = "2+5+7+12"
    num_list = str.split('+')
    print(num_list)
    rezult = 0
    for num in num_list:
        rezult = rezult + int(num)
    print(rezult)
    indicator = input('Exit? y/n: ')