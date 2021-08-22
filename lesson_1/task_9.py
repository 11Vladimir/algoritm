#!/usr/bin/python3.8


# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).


def middle_number(a: int, b: int, c: int) -> str:
    if b < a < c or c < a < b:
        print('Среднее:', a)
    elif a < b < c or c < b < a:
        print('Среднее:', b)
    else:
        print('Среднее:', c)

if __name__ == '__main__':
    user_input = input('Введите три числа, через запятую: ')
    a, b, c = map(int, user_input.split(','))
    middle_number(a, b, c)
