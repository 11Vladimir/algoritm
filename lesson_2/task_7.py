#!/usr/bin/python3.8


# 7. Напишите программу, доказывающую или проверяющую, 
# что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.


def current(n):
    return n * (n + 1) / 2


def next(n):
    return (n + 1) * (n + 2) / 2


if __name__ == '__main__':
    for i in range(1000):
        print(current(i + 1) == next(i))
