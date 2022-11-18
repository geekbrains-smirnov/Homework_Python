from in_put import in_data


def str_parse():
    s = in_data()
    lst = ','.join(map(str, s))
    return lst


def column():
    s = in_data()
    lst = '\n'.join(map(str, s))
    return lst

    

