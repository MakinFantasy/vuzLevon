from math import *


try:
    x = float(input('Введите x: '))
    if x <= -2.5:
        y = -6/7*x - 36/7
    elif -2.5 < x <= 2:
        y = 0.10101010
    elif 2 < x:
        y = -2*x + 10
except Exception as e:
    print(e)
    print(e.__doc__)
    exit(1)
print("x: {:6.2f} y:{:6.2f}".format(x, y))
