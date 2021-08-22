#!/usr/bin/python3.8


# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.


def diplay_symbol():
    row = ''
    table = ''
    for char in range(32, 128):
        row += f'{char}: {chr(char)}\t'
        if not (char - 31) % 10:
            table += f'{row}\n'
            row = ''
    table += f'{row}\n'
    print(table)

if __name__ == '__main__':
    diplay_symbol()
