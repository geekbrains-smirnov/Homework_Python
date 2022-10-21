'''Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой, 
сколько указал пользователь(БЕЗ ИСПОЛЬЗОВАНИЯ МОДУЛЕЙ/БИБЛИОТЕК)'''


import math

n = int(input('Введите число: '))
def pi_num(n):
    p = math.pi
    print(p)
    count = 0
    for i in str(p):
        while count <= n + 1:
            count += 1
            print(i, end = '')
            break


pi_num(n)