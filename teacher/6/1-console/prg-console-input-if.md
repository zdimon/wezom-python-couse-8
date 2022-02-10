# Ввод с клавиатуры. Условия.

## Оператор input.

Для того, чтобы получить данные от пользователя в консоле, вводимые с клавиатуры, используется оператор input.

Например.

    print('Enter your name:')
    x = input()
    print('Hello, ' + x)
    
При этом все что вводит пользователь присвоится переменной x.


![if input]({path-to-subject}/images/1.png)  

    print('Инициализация')
    q = 'Какой у вас вес?'
    print(q)
    print("Сбор данных")
    ves = input()
    print("Анализ данных"
    print("Вы весите " + ves + " кг.")
    ves = int(ves)
    if ves < 30:
        print("Вы худой")

    elif ves >30 and ves<60:
        print("Так держать!")

    else:
        print("Многовато однако!")


