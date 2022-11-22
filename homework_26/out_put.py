def write_file():

    with open('school_base.txt', 'r', encoding='utf_8') as data:
        value = ''.join(data.readlines()).split(';')
        search = str(input('Поиск(фамилия, имя, класс, предмет): '))
        for i in value:
            if search in i:
                print(i)