'''Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]'''


from operator import index


list = [2, 3, 4, 5, 6]


def result_list(list):
    temp = []
    temp1 = []
    result = 1
    for j in reversed(list):
            temp.append(j)
    for i in range(0, len(list)):
        result = (list[i] * temp[i])
        temp1.append(result)
    return temp1[:3]


print(result_list(list))
