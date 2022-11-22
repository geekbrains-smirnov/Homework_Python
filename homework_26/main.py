import interface as i
import out_put as o

def main():
    print('Для входа в меню учителя введите "5": ')
    print('Для входа в меню ученика введите "6": ')
    start = int(input())
    if start == 5:
        i.button_click()
    if start == 6:
        o.write_file()
    

if __name__ == '__main__':
    main()