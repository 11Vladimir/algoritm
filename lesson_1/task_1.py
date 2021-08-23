#!/usr/bin/python3.8


# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.


def math_operation(num):
    """Display the sum and the product of digits of the number entered by the user
    

    Parameters:
    num (int): number entered by the user

    Returns:
    summ (int): Returning sum digits
    mult (int): Returning product digits
    """

    summ = 0
    mult = 1

    while num > 0:
        digit = num % 10
        if digit:
            summ += digit
            mult *= digit
        num //= 10
    print('Сумма цифр числа:', summ, '\n' 'Произведение цифр числа:', mult)


if __name__ == '__main__':
    number = int(input('Введите число: '))
    math_operation(num=number)
