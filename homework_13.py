'''Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10'''


print('Введите число:')
n = int(input())
b = 0
temp = []
while n > 0:
    b = n % 2
    n = n // 2
    temp.append(b)
print(temp)
