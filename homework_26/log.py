def loger(dir):
    with open('school_base.txt', 'a', encoding='utf_8') as data:
        rec = dir
        data.write(str(rec)+ ';')