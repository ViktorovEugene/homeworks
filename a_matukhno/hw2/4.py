# -*- coding: utf-8 -*-
"""
Задание 4: Чет-нечет.
УСЛОВИЕ:
Фрагмент кода, который принимает список любых чисел и фильтрует его по четным (удаляет нечетные),
если количество элементов в списке является четным и наоборот (удаляет четные, если элементов изначально нечетное количество).
Пример:
[3,7,12] >> [3,7]
[3,7,12,7] >> [12]
"""

s1 = [12, 3, 7, 12, 12, 12, 7]
s2 = [3, 7, 12, 7]


def task4(x):
    if x.__len__() % 2 == 1 or x.__len__() == 1:
        for i, el in enumerate(x):
            if el % 2 == 0:
                x[i] = 'x'
    elif x.__len__() % 2 == 0:
        for i, el in enumerate(x):
            if el % 2 != 0 or el == 1:
                x[i] = 'x'
    x = filter(lambda a: a != 'x', x)
    return x


if __name__ == '__main__':
    print task4(s1)
    print task4(s2)