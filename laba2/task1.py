from math import *


try:
    x = float(input('Введите x: '))
    if x <= -2.5:
        y = -6 / 7 * x - 36 / 7
    elif -2.5 < x <= -1:
        y = -4 * x ** 2 - 12 * x - 8
    elif -1 < x <= 0:
        y = -3 * x - 3
    elif 0 < x <= 1.5:
        y = 4 * x ** 2 - 4 * x - 3
    elif 1.5 < x <= 2:
        y = 12 * x - 18
    elif 2 < x:
        y = -2 * x + 10
except Exception as e:
    print(e)
    print(e.__doc__)
    exit(1)
print("x: {} y:{}".format(x, y))
