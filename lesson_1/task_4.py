#!/usr/bin/python3.8


# 4. Написать программу, которая генерирует в указанных пользователем границах:

#     случайное целое число;
#     случайное вещественное число;
#     случайный символ.

#     Для каждого из трех случаев пользователь задает свои границы диапазона. 
#     Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. 
#     Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random


def int_generator(element1: int, element2: int) -> int:
    return random.randint(element1, element2) if element1 < element2 else random.randint(element2, element1)   


def float_generator(element1: int, element2: int) -> int:
    return random.uniform(element1, element2) if element1 < element2 else random.uniform(element2, element1)


def char_generator(element1: str, element2: str) -> str:
    return chr(random.randint(ord(element1), ord(element2))) if element1 < element2 else chr(random.randint(ord(element2), ord(element1)))


if __name__ == '__main__':
    user_input = input('Введите границы для генерации случайного значения, через запятую: ')
    if user_input.replace(', ', '').isdigit():
        element1, element2 = map(int, user_input.split(','))
        print(int_generator(element1, element2))
        print(float_generator(element1, element2))
    else:
        element1, element2 = user_input.split(', ')
        print(char_generator(element1, element2))
