from math import log, tan, pi, sqrt


def calculate():
    try:
        print("Первая формула: ", '\n')
        for i in range(5):
            print('Тест ', i + 1)
            a = int(input("Введите параметр а: "))
            b = int(input("Введите параметр b: "))
            try:
                z = a ** sqrt(log(b, a)) - b ** sqrt(log(a, b)) + tan(a*b + 3*pi/2)
                print("Ответ: ", z)
            except Exception as e:
                print("Ответ: ОДЗ")

        print("Вторая формула: ", '\n')
        for j in range(5):
            print('Тест ', j + 1)
            a = int(input("Введите параметр а: "))
            b = int(input("Введите параметр b: "))
            try:
                z = tan(a*b + (3/2) * pi)
                print("Ответ: ", z)
            except Exception as e:
                print("Ответ: ОДЗ")
    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)


calculate()
