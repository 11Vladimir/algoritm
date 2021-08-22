#!/usr/bin/python3.8


# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.


def naturalal_numbers():
    arr = [0] * 8
    for i in range(2, 100):
        for j in range(2, 10):
            if i % j == 0:
                arr[j - 2] += 1
    return arr 


if __name__ == '__main__':
        for el, ell in enumerate(naturalal_numbers()):
            print(f'{el + 1}. {el + 2} - {ell} раз(а)')
