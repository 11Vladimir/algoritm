#!usr/bin/python3.9


# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, 
# заданный случайными числами на промежутке [-100; 100). 
# Выведите на экран исходный и отсортированный массивы. 
# Сортировка должна быть реализована в виде функции. 
# По возможности доработайте алгоритм (сделайте его умнее).


import random


arr = [random.randint(-100, 100) for _ in range(1, 10)]


def buble_sort(array):
    lenth_arr = len(array)
    for el in range(lenth_arr):
        for ell in range(0, lenth_arr - el - 1):
            if array[ell] < array[ell + 1]:
                array[ell], array[ell + 1] = array[ell + 1], array[ell]
    return(array)


print(f'Не отсортированный массив: {arr}')
print(f'Отсортированный массив методом пузырька, в обратном порядке: {buble_sort(arr)}')
