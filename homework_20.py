'''Создайте программу для игры в ""Крестики-нолики"".'''


lst = [['00', '01', '02'],
       ['10', '11', '12'],
       ['20', '21', '22']]
for i in lst:
    print(' '.join(list(map(str, i))))
for i in range(9):
    if i % 2 == 0:
        print('Ход первого игрока: ')
        lst[int(input('->'))][int(input('->'))] = 'x'
        if lst[0][0] == lst[1][0] == lst[2][0]:
            for j in lst:
                print(' '.join(list(map(str, j))))
            print('Ура! Победил первый игрок!')
            break
        if lst[0][1] == lst[1][1] == lst[2][1]:
            for j in lst:
                print(' '.join(list(map(str, j))))
            print('Ура! Победил первый игрок!')
            break
        if lst[0][0] == lst[1][1] == lst[2][2]:
            for j in lst:
                print(' '.join(list(map(str, j))))
            print('Ура! Победил первый игрок!')
            break
        if lst[0][0] == lst[0][1] == lst[0][2]:
            for j in lst:
                print(' '.join(list(map(str, j))))
            print('Ура! Победил первый игрок!')
            break
        if lst[1][0] == lst[1][1] == lst[1][2]:
            for j in lst:
                print(' '.join(list(map(str, j))))
            print('Ура! Победил первый игрок!')
            break
        if lst[0][2] == lst[1][2] == lst[2][2]:
            for j in lst:
                print(' '.join(list(map(str, j))))
            print('Ура! Победил первый игрок!')
            break
        if lst[0][2] == lst[1][1] == lst[2][0]:
            for j in lst:
                print(' '.join(list(map(str, j))))
            print('Ура! Победил первый игрок!')
            break
        for j in lst:
            print(' '.join(list(map(str, j))))
    if i % 2 == 1:
        print('Ход второго игрока: ')
        lst[int(input('->'))][int(input('->'))] = 'O'
        if lst[0][0] == lst[1][0] == lst[2][0]:
            for j in lst:
                print(' '.join(list(map(str, j))))
            print('Ура! Победил второй игрок!')
            break
        if lst[0][1] == lst[1][1] == lst[2][1]:
            for j in lst:
                print(' '.join(list(map(str, j))))
            print('Ура! Победил первый игрок!')
            break
        if lst[0][0] == lst[1][1] == lst[2][2]:
            for j in lst:
                print(' '.join(list(map(str, j))))
            print('Ура! Победил второй игрок!')
            break
        if lst[0][0] == lst[0][1] == lst[0][2]:
            for j in lst:
                print(' '.join(list(map(str, j))))
            print('Ура! Победил второй игрок!')
            break
        if lst[1][0] == lst[1][1] == lst[1][2]:
            for j in lst:
                print(' '.join(list(map(str, j))))
            print('Ура! Победил второй игрок!')
            break
        if lst[0][2] == lst[1][2] == lst[2][2]:
            for j in lst:
                print(' '.join(list(map(str, j))))
            print('Ура! Победил второй игрок!')
            break
        if lst[0][2] == lst[1][1] == lst[2][0]:
            for j in lst:
                print(' '.join(list(map(str, j))))
            print('Ура! Победил второй игрок!')
            break
        for j in lst:
            print(' '.join(list(map(str, j))))
else:
    print('Ничья! Попробуйте снова!')
