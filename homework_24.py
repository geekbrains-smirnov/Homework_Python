'''3) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Пример:
- 6782 -> 23
- 0, 56 -> 11'''

from functools import reduce

n =input('Введите вещественное число: ')
value = ''.join(i for i in str(n) if i != '.')
result = reduce(lambda x, y: int(x)+int(y), value)
print(result)