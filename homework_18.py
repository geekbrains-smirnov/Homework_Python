'''Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и вывести многочлен степени k.

Пример:

- k=2 => 2*x² + 4*x + 5 = 0 

k = 6
    ix^6 + ax^5 + bx^4+ cx^3 + dx^2 + ex + h = 0

    a, b, c, d, e, h - рандом'''


from random import randint, choice


n = int(input('Введите степень: '))
k_list = [randint(0, 10) for i in range(10)]
k = choice(k_list)


def polynomial(n):
    pol_member = []
    pol_member.append(str(choice(k_list)))
    pol_member.append('* x ^')
    pol_member.append(str(n))
    pol_member.append('+')
    polm_str = " ".join(pol_member)
    while n - 1 > 0:
        pol_member.append(str(choice(k_list)))
        pol_member.append('* x ^')
        pol_member.append(str(n-1))
        pol_member.append('+')
        polm_str = " ".join(pol_member)
        n -= 1
    print(f'{polm_str} = 0')


polynomial(n)