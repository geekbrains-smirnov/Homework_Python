'''Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19'''


list = [1.1, 11.2, 3.1, 5, 10.01]


temp = []
for i in list:
    temp.append(i % 1)


def result_list(list):
    result = 0
    min = temp[0]
    max = temp[0]
    for i in temp:
        for j in temp:
            if i < min and i != 0:
                min = i
            elif j > max:
                max = j
    result = max - min
    return round(result, 2)


print(temp)
print(result_list(list))