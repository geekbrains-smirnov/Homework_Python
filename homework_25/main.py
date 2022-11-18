import interface as i
import out_put as o

def main():
    print('Для записи данных нажмите "5": ')
    print('Для чтения данных нажмите "6": ')
    start = int(input())
    if start == 5:
        i.button_click()
    if start == 6:
        o.write_file()
    

if __name__ == '__main__':
    main()

