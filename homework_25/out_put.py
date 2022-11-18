def write_file():
    with open('note.txt', 'r') as data:
        value = ''.join(i for i in data.readlines())
        print(value)