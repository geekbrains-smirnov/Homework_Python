'''Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).'''

print('Введите номер четврети:')
n = int(input())
if n == 1:
    print(f'Диапазон возможных координат {n} четверти X: от 1 до + бесконечности Y: от 1 до + бесконечности')
elif n == 2:
    print(f'Диапазон возможных координат {n} четверти X: от -1 до - бесконечности Y: от 1 до + бесконечности')
elif n == 3:
    print(f'Диапазон возможных координат {n} четверти X: от -1 до - бесконечности Y: от -1 до - бесконечности')
elif n == 4:
    print(f'Диапазон возможных координат {n} четверти X: от 1 до + бесконечности Y: от -1 до - бесконечности')