'''Задание 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

Пример:

пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)'''


print('Введите проверочное число:')
n = int(input())


def num_list(n):
    temp = []
    result = 1
    for i in range(1, n + 1):
        result = result * i
        temp.append(result)
        
    print(temp)


num_list(n)