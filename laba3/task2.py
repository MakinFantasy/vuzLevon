from math import *
from random import uniform

def mainLine():
    print(" " * 5 + "X" + " " * 10 + "Y" + " " * 7 + "Res" + " " * 5)
    print("-" * 32)



def startShooting():
    R = float(input('Enter radius: '))
    mainLine()
    for i in range(10):
        X = uniform(-2 * R, 2 * R)
        Y = uniform(-2 * R, 2 * R)
        try:
            if ( (-2*R <= X <= 0) and (-2 * R <=  Y <= 0) and (Y >= -X - 2*R)) \
                or ( (0 <= Y <= 2 * R) and (0 <= X <= 2 * R) and (X**2 + Y**2 >= R ** 2)):
                print("{0: 10.2f}{1: 10.2f}".format(X, Y) + "\tTrue")
            else:
                print("{0: 10.2f}{1: 10.2f}".format(X, Y) + "\tFalse")
        except Exception as e:
            print(e)
            print(e.__doc__)
            exit(1)


if __name__ == '__main__':
    startShooting()