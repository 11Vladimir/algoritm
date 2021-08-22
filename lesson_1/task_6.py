#!/usr/bin/python3.8


# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.


def position_letter(char: int) -> str:
    return f'Это буква: {chr(char + 64)}'


if __name__ == '__main__':
    char = int(input('Введите номер буквы в алфавите от 1 до 26: '))
    print(position_letter(char))
