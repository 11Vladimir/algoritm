#!/usr/bin/python3.8


# 2. Посчитать четные и нечетные цифры введенного натурального числа. 
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).


def even_odd_number(number: str) -> str:
    even = 0
    odd = 0
    for num in number:
        if int(num) % 2 == 0:
            even += 1
        else:
            odd += 1
    return f'Четных цифр {even}, нечетных цифр {odd}'


if __name__ == '__main__':
    number = input('Введите число: ')
    print(even_odd_number(number=number))
