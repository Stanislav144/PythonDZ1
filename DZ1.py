# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

a = int(input('Введите число '))

if a == 6 or a == 7:
    print('Выходной')
elif a <= 0 or a < 6:
    print('Не выходной')