from math import *

file = open('input1.txt')
res = open('out1.txt', 'a')


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


def main():
    try:
        res.write("Первая формула: " + "\n")
        arr = file.readline().split(' ')
        values = []
        for el in arr:
            values.append(int(el))
        for i in range(len(values) - 1):
            print('Тест ', i + 1)
            a = values[i]
            b = values[i + 1]
            try:
                z = a ** sqrt(log(b, a)) - b ** sqrt(log(a, b)) + tan(a * b + 3 * pi / 2)
                res.write("Тест" + str(i + 1) + ": " + "a=" + str(a) + " " + "b=" + str(b) + ": " + str(z) + '\n')
            except Exception as e:
                res.write("Тест" + str(i + 1) + ": " + "a=" + str(a) + " " + "b=" + str(b) + ": " + "ОДЗ" + '\n')

        # print("Вторая формула: ", '\n')
        # for j in range(5):
        #     print('Тест ', j + 1)
        #     a = int(input("Введите параметр а: "))
        #     b = int(input("Введите параметр b: "))
        #     try:
        #         z = tan(a * b + (3 / 2) * pi)
        #         print("Ответ: ", z)
        #     except Exception as e:
        #         print("Ответ: ОДЗ")
    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)


try:
    clear_file()
    main()
    clear_line()
except Exception as e:
    print(e)
    print(e.__doc__)
    exit(1)
