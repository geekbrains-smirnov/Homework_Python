'''Задание 5 Реализуйте алгоритм перемешивания списка.'''


from random import randint
import random


print('Введите размер списка:')
n = int(input())


def mix_list(n):
    list_ = []
    list_1 = []
    for i in range(1, n+1):
        list_.append(randint(1, 100))
    list_1 = list_[:]
    list_length = len(list_1)
    for j in range(list_length):
        index_random = random.randint(0, list_length -1)
        temp = list_1[j]
        list_1[j] = list_1[index_random]
        list_1[index_random] = temp
    print(list_)
    print(list_1)


mix_list(n)
