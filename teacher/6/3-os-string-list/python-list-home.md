# Домашнее задание. Списки.

1. Используя генератор списков, создать список, заполненый квадратами целых чисел от 1 до 5.

2. Используя генератор списков, создать список, заполненый 10 случайными числами от 1 до 10, удалить из него повторяющиеся значения.

3. Считать имена файлов внутри текущего каталога и вывести их на экран в виде списка, отсортированного по алфавиту.

4. Дана строка 'user1:23:user2:45:user3:37'

Преобразовать ее в список.

    ['user1',23,'user2',45,'user3',37]

затем получившейся список превратить в следующие форматы списков

    [['user1',23],['user2',45],['user3',37]]
    
    [['user1','user2','user3'],['23','45','37']]


## Игра блек-джек

Дано два списка, с 4-мя мастями и 9 картами.

    faces = [1,2,3,4]
    cards = [2,3,4,5,6,7,8,9,10]

Необходимо создать новый список колоды карт, в которой будет 36 карт по 9 каждой масти.
При этом числа будут повторятся т.е. в колоде будет четыре двойки, четыре тройки и т.д.

В начале игры (запуске программы) пользователю сдается 2 случайные карты (числа).
Подсчитывается кол-во набранных очков, и выводится результат и предложение взять еще карту или отказаться.

Например: 

У вас такие карты - 3,5 общее количество очков - 8
Хотите взять еще? д\н

Если пользователь соглашается, ему выдается еще одна карта и процесс повторяется пока будет набрано больше 21 очка. 

В этом случае пользователю говорят что он проиграл и предлагают повторить игру или выйти из программы.

В случае если пользователь отказывается брать карту вступает в игру компьютер.

Он берет случайные карты до тех пор пока не наберет от 18 очков (включительно) до 21.

Если количество баллов, набранных компьютером находится между 18 и 21 компьютер прекращает брать карты, сравнивает свои очки с очками пользователя и определяет победителя или ничью.

Если компьютер набрал больше 21 то он проигрывает и пользователю предлагается продолжить игру или выйти.







    

    
Вопрос что делает этот код?

    a = [input() for i in range(int(input()))]
    
    a = [1,2,3,4]
    b = a[:]

