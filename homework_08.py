'''Задание 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на позициях a и b.
Значения N, a и b вводит пользователь с клавиатуры.'''


print('Задайте длинну списка:')
n = int(input())
print('Введите a, где а номер позиции числа из списка')
a = int(input())
print('Введите b, где b номер позиции числа из списка')
b = int(input())


def mult_num(n):
    list = []
    result = 1
    for i in range(1, n+1):
        list.append(-(n-i+1))
    for j in range(n+1):
        list.append(j)
    result = list[a] * list[b]
    print(list)
    print(f'Произведение элементов на позициях a: {list[a]} и b: {list[b]} равно: {result}')


mult_num(n)
