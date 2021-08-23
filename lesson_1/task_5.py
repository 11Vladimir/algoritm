#!/usr/bin/python3.8


# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.


def char_position(char1: int, char2: int) -> str:
    distance = abs((ord(char1) - 64) - (ord(char2) - 64)) - 1
    print(f'Буква "{char1}" {ord(char1) - 64}-я в алфавите\n'
          f'Буква "{char2}" {ord(char2) - 64}-я в алфавите\n'
          f'Между буквами {distance} букв')

if __name__ == '__main__':
    char1, chrar2 = input('Ведите две прописные буквы латинского алфавита, через запятую: ').split(', ')
    char_position(char1, chrar2)
