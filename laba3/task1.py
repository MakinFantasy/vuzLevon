from math import *

from math import *


def initParams():
    CONST_RADIUS = 2
    X_START = float(input('Enter x start: '))
    X_END = float(input('Enter x end: '))
    X_DELTA = float(input('Enter dx: '))
    if X_START > X_END or X_DELTA < 0:
        print('Enter correct start vlaues')
        exit(1)
    return [X_START, X_END, X_DELTA, CONST_RADIUS]


def mainLine():
    print("+" + "-" * 8 + "+" + "-" * 8 + "+")


def columns():
    print('I   X    I    Y   I')


def data(array):
    print('Xbeg= ' + str(array[0]) + " Xend= " + str(array[1]) + '\n' + '  Dx=  ' + str(array[2]))


def calculate():
    try:

        params = initParams()

        mainLine()

        columns()

        mainLine()

        x, end, dx, r = params[0], params[1], params[2], params[3]
        data(params)
        counter = 0
        while x <= end + 1:

            if x <= -2.5:
                y = -6 / 7 * x - 36 / 7
            elif -2.5 < x <= 2:
                y = 0.10101010 ### incorrect  expr for y
            elif 2 < x:
                y = -2 * x + 10

            print("I{0: 7.2f} I{1: 7.2f} I".format(x, y))

            x += dx

        mainLine()

    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)


if __name__ == '__main__':
    calculate()
