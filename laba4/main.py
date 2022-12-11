from random import *


def init():
    try:
        n = int(input('Введите кол-во элементов: '))
        array = []
        for i in range(n):
            array.append(randint(-5, 5))
        print(array)
        return array
    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)


def less_y_sum(y, array):
    new_arr = [i for i in array if abs(i) < y]
    to_return = [i for i in array if abs(i) >= y]
    result = sum(new_arr)
    # print(new_arr)
    print('Искомая сумма: ', result)
    return to_return


def multiplication(array):
    # print(array)
    result = 1
    for i in array:
        result *= i
    print('Искомое произведение: ', result)
    return result


def main():
    arr = init()
    y = float(input('Введите значение y: '))
    sum = less_y_sum(y, arr)
    multiplication(sum)

main()
