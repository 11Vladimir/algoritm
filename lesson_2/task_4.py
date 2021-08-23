#!/usr/bin/python3.8


# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.


def sum_sequence(number: int) -> str:
    summa = 0
    for i in range(number):
        summa += 1 / (-2) ** i
    return f'Сумма последовательности = {summa}'


if __name__ == '__main__':
    number = int(input('Введите длинну последовательности: '))
    print(sum_sequence(number))
