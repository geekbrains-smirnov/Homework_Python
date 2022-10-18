'''Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]'''


from audioop import reverse


fib1 = 0
fib2 = 1
fib3 = 0
fib4 = 1
 
temp = []
temp1 =[fib2]
temp2 = [fib3,fib4]
n = int(input())

 
for i in range(1, n):
    fib_sum = fib1 + (-fib2)
    fib1 = fib2
    fib2 = fib_sum
    temp1.append(fib2)
for j in range(1, n):
    fib_sum = fib3 + (fib4)
    fib3 = fib4
    fib4 = fib_sum
    temp2.append(fib4)
for i in reversed(temp1):
    temp.append(i)
for j in temp2:
    temp.append(j)


print(temp)
