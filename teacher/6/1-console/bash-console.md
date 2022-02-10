# Команды BASH

Вывод на экран

    echo $переменная | строка | "строка $переменная"

## Переменные и их вывод в консоль.

    #!/bin/bash 
    STR="Hello World!"
    echo $STR
    echo $PATH # переменная поиска команд
    echo "$PATH - переменная поиска" # форматирование строки
    
## Команда переправления вывода

    echo 'hello' > filename.txt
    echo 'hello' >> filename.txt

## Переменная PATH

    echo $PATH
    
- это мета где система ищет исполняемые файлы-команды, например python

    whereis python

- выведет все места где находятся файлы для питона

## Команда **pwd**.

- вывод текущей директории

## Смена директории. Команда **cd**

    cd ~ # домашняя директория
    
    cd / # корневая директория
    
    cd dirname/subdir # смена директории
    
    cd .. # поднятие на уровень вверх

    
## Просмотр директории. Команда **ls**.

    ls # краткий список
    ls -l # полный список
    ls -la # включая скрытые файлы
    ls -lh # c кратким размером
    
## Команда **grep**.

    grep -rn 'string' # поиск файлов со строкой с указанием номера строки
    
 
## Обединение команд оператор |.

    ls -la | grep 'substr' # поиск файлов и директорий содержащих подстроку    
    
    


## Команда **mkdir** (создание директории).

    mkdir dirname

## Команда rm.

    rm ./filename # удаление файла
    rm -R dirname # удаление директории и ее содержимого

## Команда **nano**.

    nano ./filename # редактирование файла
    
- ctrl+o - запись в файл

- ctrl+x - выход из редактора

## Команда cat

    cat filename
    
вывод содержимого файла

## Системная переменная $PS1

    echo $PS1
    PS1='>>>'
    export PS1='<<<'

## Команда **chmode**.

    chmode +x ./filename # сделать файл исполняемым
    chmod 777 ./filename # изменение прав на файл
    chmod 667 -R dirname # изменение прав на содержимое директории 
    
    
## Команда **chown**.

    chown -R user:user dirname # изменение владельца и группы директории и всего содержимого рекурсивно
    
    
## Строка, определяющая содержимое файла (на каком языке python, php, bash и т.д.).

    #!/bin/bash
    #!/usr/bin/env python   
    
# Язык bash

[Справочник по встроенным командам](https://www.gnu.org/software/bash/manual/html_node/Bash-Builtins.html)

## Перенаправление ввода-вывода

    >> > - перенаправляет в файл
    
    | - соединяет вывод одной команды со вводом другой
    
## Команда **source** и запуск bash скриптов.

    myscript # запуск команды (файла) из системных директорий
    ./myscript # запуск файла из текущей дериктории
    source ./myscript # запуск скрипта в текущей сессии терминала (оболочки) shell в ТЕКУЩЕМ процессе
    . ./myscript # аналог предыдущей команды
    
Использование точки говорит о текущей директории (не находящейся в переменной PATH) без точки интерпретатор будет искать файл в $PATH.   

Использование source позволяет менять окружение оболочки т.к. выполняется не в новом процессе как при обычном запуске (без source).
    
## Условие. Файл .bashrc

    cd () {
        builtin cd ${1:+"$@"} # выполняем оригинальную команду с параметрами
        if [ -f "env.sh" ] # проверяем существование файла
        then
         . ./env.sh # запускаем файл
        fi  
    }
    
    
    
    
    
    