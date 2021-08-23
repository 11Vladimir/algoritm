#!/usr/bin/python3.8


# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.


def is_leap(year):
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        return 'Невисокосный'
    return 'Високосный'

if __name__ == '__main__':
    year = int(input('Введите год: '))
    print(is_leap(year))
