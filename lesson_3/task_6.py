#!/usr/bin/python3.8


# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. 
# Сами минимальный и максимальный элементы в сумму не включать.


from random import random


def min_max_el(arr, num):
    min_id = 0
    max_id = 0
    for i in range(1, num):
        if arr[i] < arr[min_id]:
            min_id = i 
        elif arr[i] > arr[max_id]:
            max_id = i

    if min_id > max_id:
        min_id, max_id = max_id, min_id
    
    return min_id, max_id


def summa_elements(arr):
    summa = 0
    min_id, max_id = min_max_el(arr, len_arr)
    for i in range(min_id + 1, max_id):
        summa += arr[i]
    print(summa)


if __name__ == '__main__':
    len_arr = 10
    arr = [0] * len_arr
    for i in range(len_arr):
        arr[i] = int(random()*50)
    print(arr)
    summa_elements(arr)
