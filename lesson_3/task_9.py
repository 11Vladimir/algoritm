#!/usr/bin/python3.8


# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import random

M = 10
N = 5


def matrix():
    arr = []
    for _ in range(N):
        b = []
        for _ in range(M):
            n = int(random() * 200)
            b.append(n)
        arr.append(b)
    return arr


mx = -1
for j in range(M):
    mn = 200
    for i in range(N):
        if matrix()[i][j] < mn:
            mn = matrix()[i][j]
    if mn > mx:
        mx = mn
print(matrix(),'\n', "Максимальный среди минимальных: ", mx)
