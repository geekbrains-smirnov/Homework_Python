'''Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
stroklst = "aaabbbbccbbb"
....
stroklst = "3a4b2c3b" '''





with open('input.txt', 'r') as spisok:
    # print(spisok.relstdline())
    lst = list(spisok.readline())
    result = ''
    i = 0
    while i < len(lst):
        count = 1
        while i + 1 < len(lst) and lst[i] == lst[i + 1]:
            count += 1
            i += 1
        result += str(count) + lst[i]
        i += 1
    print(result)
    new_file = open('output.txt', 'w')
    new_file.write(result)