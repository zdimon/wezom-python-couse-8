indicator = 'n'
while indicator == 'n':
    string = "2+4+6+8"
    number_list = string.split('+')
    print(number_list)
    rezult = 0
    for number in number_list:
        rezult = rezult + int(number)
    print(rezult)
    indicator = input('Exit? y or n')