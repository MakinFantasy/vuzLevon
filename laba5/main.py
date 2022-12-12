import numpy as np


def initM():
    try:
        m = int(input('Введите кол-во строк: '))
        n = int(input('Введите кол-во стобцов: '))
        matr1 = np.random.randint(-10, 10, (m, n))
        print(matr1)
        print()
        matr2 = np.random.randint(-10, 10, (m, n))
        print(matr2)
        return [matr1, matr2]
    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)


def addM(a, b):
    try:
        res = []
        for i in range(len(a)):
            row = []
            for j in range(len(a[0])):
                row.append(a[i][j]+b[i][j])
            res.append(row)
        return res
    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)


def subM(a, b):
    try:
        res = []
        for i in range(len(a)):
            row = []
            for j in range(len(a[0])):
                row.append(a[i][j]-b[i][j])
            res.append(row)
        return res
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
        return transposed_matr
    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)

def main():
    try:
        res = initM()
        matr_sum = addM(res[0], res[1])
        print('Сумма матриц: ', matr_sum, '\n')
        matr_sub = subM(res[0], res[1])
        print("Разность матриц: ", matr_sub, '\n')
        matr_trans_first = transposeM(res[0])
        print('Транспонирование первой матрицы: ', matr_trans_first, '\n')
        matr_trans_second = transposeM(res[1])
        print('Транспонирование второй матрицы: ', matr_trans_second, '\n')
    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)


main()
