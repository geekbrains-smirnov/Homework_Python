from rec_data import str_parse, column
import log


def button_click():
    print('Введите "0" если ходите продолжить')
    print('Введите "1" если хотите закончить')
    flag = int(input())
    while flag == 0:
        print('Для сохранения данных строкой нажмите "3"')
        print('Для сохранения данных столбцом, нажмите "4"')
        var = int(input())
        if var == 3:
            dir = str_parse()
            log.loger(dir)
            print('Введите "0" если ходите продолжить')
            print('Введите "1" если хотите закончить')
            flag = int(input())
            # if flag == 1:
            #     print("Программа завершилась, Удачи!")
            #     break
        if var == 4:
            dir = column()
            log.loger(dir)
            print('Введите "0" если ходите продолжить')
            print('Введите "1" если хотите закончить')
            flag = int(input())
            # if flag == 1:
            #     print("Программа завершилась, Удачи!")
            #     break
    print("Программа завершилась, Удачи!")
