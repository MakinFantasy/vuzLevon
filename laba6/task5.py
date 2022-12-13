import numpy as np


file = open('input3.txt')
res = open('out3.txt', 'a')


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


def initM():
    try:
        matr = int(file.readline())
        matrix_list = []
        for i in range(matr):
            matrix = []
            rows = int(file.readline())
            for i in range(rows):
                row = []
                arr = file.readline().split(' ')
                if not(len(arr) == 1 and arr[0] == ''):
                    for el in arr:
                        row.append(int(el))
                matrix.append(row)
            matrix_list.append(matrix)
        for i in range(len(matrix_list)):
            res.write(str(matrix_list[i]) + '\n')
            clear_line()
        return matrix_list
    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)


def addM(a, b):
    try:
        arr = []
        for i in range(len(a)):
            row = []
            for j in range(len(a[0])):
                row.append(a[i][j]+b[i][j])
            arr.append(row)
        res.write("Сумма: " + str(arr))
    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)


def subM(a, b):
    try:
        arr = []
        for i in range(len(a)):
            row = []
            for j in range(len(a[0])):
                row.append(a[i][j]-b[i][j])
            arr.append(row)
        res.write('Разность: ' + str(arr))
    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)


def transposeM(matr):
    try:
        transposed_matr = [[0 for j in range(len(matr))] for i in range(len(matr[0]))]
        for i in range(len(matr)):
            for j in range(len(matr[0])):
                transposed_matr[j][i] = matr[i][j]
        res.write('Транспонированая матрица: ' + str(transposed_matr))
    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)


def main():
    try:
        clear_file()
        result = initM()
        clear_line()
        addM(result[0], result[1])
        clear_line()
        subM(result[0], result[1])
        clear_line()
        transposeM(result[0])
    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)


main()
