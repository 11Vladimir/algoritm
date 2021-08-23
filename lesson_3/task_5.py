#!/usr/bin/python3.8


# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.


numbers = [3, -5, 6, 2, 46, 86, 6, -3, 4, -600, 2, 2, 2, 5, 34, 6, 5, 4, -3, -600, -1145]
max = -1
for i, number in enumerate(numbers):
    if number < 0 and (max < 0 or abs(number) < abs(numbers[max])):
        max = i
print(max, numbers[max])
