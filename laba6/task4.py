from random import *

file = open('input2.txt')
res = open('out2.txt', 'a')


def clear_file():
    try:
        res.truncate(0)
    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)


def clear_line():
    try:
        res.write('\n')
    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)


def init():
    try:
        line = file.readline().split(' ')
        values = [int(el) for el in line]
        print(values)
        return values
    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)


def less_y_sum(y, array):
    new_arr = [i for i in array if abs(i) < y]
    to_return = [i for i in array if abs(i) >= y]
    result = sum(new_arr)
    res.write('Сумма: ' + str(result))
    return to_return


def multiplication(array):
    result = 1
    for i in array:
        result *= i
    res.write('Произведение: ' + str(result))
    return result


def main():
    clear_file()
    arr = init()
    y = float(input('Введите значение y: '))
    sum = less_y_sum(y, arr)
    clear_line()
    multiplication(sum)

main()
