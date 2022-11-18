def loger(dir):
    with open('note.txt', 'a') as data:
        rec = dir + ';\n'
        data.write(str(rec))