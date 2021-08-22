#!/usr/bin/python3.8


# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b
# , проходящей через эти точки.


def equation(x1: int, y1: int, x2: int, y2: int) -> str:
    """
    Find straight equation like y=kx+b.


    Params:
    :x1: integer input
    :y1: integer input
    :x2: integer input
    :y1: integer input


    Returns:
    Equation like y=kx+b: type string
    """
    
    k = (y1 - y2) / (x1 -x2)
    b = y2 * k * x2
    result = f'y = {k:.2f}*x + {b:.2f}'

    return result

if __name__ == '__main__':
    x1, y1 = map(float, input('Координаты точки A(x1;y1), через запятую: ').split(','))
    x2, y2 = map(float, input('Координаты точки B(x2;y2), через запятую: ').split(','))

    print(equation(x1, y1, x2, y2))
