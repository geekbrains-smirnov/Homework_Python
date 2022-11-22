from rec_data import str_parse
import log


def button_click():
    print('Введите "0" если ходите продолжить')
    print('Введите "1" если хотите закончить')
    flag = int(input())
    while flag == 0:
        dir = str_parse()
        log.loger(dir)
        print('Введите "0" если ходите продолжить')
        print('Введите "1" если хотите закончить')
        flag = int(input())
    print("Программа завершилась, Удачи!")