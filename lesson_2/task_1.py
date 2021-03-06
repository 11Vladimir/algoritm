#!/usr/bin/python3.8


# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. 
# Числа и знак операции вводятся пользователем. 
# После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений. 
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. 
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), 
# то программа должна сообщать ему об ошибке и снова запрашивать знак операции. 
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.


def math_operation(num1: int, num2: int, symbol: str) -> str:
    if symbol == '+':
        return f'Сумма равна: {num1 + num2}'
    elif symbol == '-':
        return f'Разность равна: {num1 - num2}'
    elif symbol == '*':
        return f'Произведение равно: {num1 * num2}'
    elif symbol == '/' and num2 != 0:
        return f'Деление равно: {num1 / num2}'
    return 'Неверная операция'


if __name__ == '__main__':
    while True:
        num1, num2, symbol = input('Введите значение и знак операции, через запятую: ').split(', ')
        if symbol == '0':
            break
        print(math_operation(int(num1), int(num2), symbol))
