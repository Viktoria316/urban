'''
Практическая работа по уроку "Организация программ и методы строк"



Цель: Написать программу на языке Python с использованием Pycharm для работы с методами строк и организации программ.



1. В проекте, где вы решаете домашние задания, создайте модуль 'module_1_4.py' и напишите весь код в нём.



2. Организуйте программу:

Создайте переменную my_string и присвойте ей значение строки с произвольным текстом (функция input()).
Вывести количество символов введённого текста
3. Работа с методами строк:

Используя методы строк, выполните следующие действия:

Выведите строку my_string в верхнем регистре.
Выведите строку my_string в нижнем регистре.
Измените строку my_string, удалив все пробелы.
Выведите первый символ строки my_string.
Выведите последний символ строки my_string.
Примечания:

Для вывода значений на экран используйте функцию print().
Для вызова методов строк используйте операцию точки '.'.
Дополнительно о всех методах строк можно узнать здесь.
Пример результата выполнения программы:



Код:

name = input()

print(name.upper())



Ввод в консоль:

Urban



Вывод на консоль:

URBAN



Напишите код к домашнему заданию в ответе (комментарии).



Успехов!


'''

# 1
my_string = input()

# 2
print(len(my_string))

# 3

# 3.1
print(my_string.upper())
# 3.2
print(my_string.lower())
# 3.3
print(my_string.replace(' ', ''))

# 4
print(my_string[0])

# 5
print(my_string[-1])

