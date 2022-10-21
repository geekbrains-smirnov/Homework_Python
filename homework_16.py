'''Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
N = 6 | N = 12 | 32 | 13 | 9 | 18 | 21
2 * 3 | 2 * 2 * 3 | 2 * 2 * 2 * 2 * 2 | 13 | 3 * 3 | 2 * 3 * 3 | 3*7'''


num = int(input('Введите число: '))


def factor(num):
    temp = []
    f = 2
    while f <= num:
        if num % f == 0:
            temp.append(f)
            num //= f
        else:
            f += 1
    if num < 1:
        temp.append(num)
    return temp


print(factor(num))