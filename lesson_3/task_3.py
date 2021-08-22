#!/usr/bin/python3.8


# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random



def change_min_max(lst):
    lst[lst.index(max(lst))], lst[lst.index(min(lst))] = lst[lst.index(min(lst))], lst[lst.index(max(lst))]
    return lst


if __name__ == '__main__':
    lst = sorted(random.sample(range(1, 50), 7))
    print (f'{lst}\n{change_min_max(lst)}')
