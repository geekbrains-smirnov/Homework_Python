'''2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.

[12,'sadf',5643] ---> ['sadf'] ,[12,5643]'''

lst = [12,'sadf',5643]
str_lst = list(filter(lambda x: type(x) == str, lst))
num_lst = list(filter( lambda x: type(x) == int, lst))
print(str_lst, num_lst)