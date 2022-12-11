try:
    R = float(input("Введите радиус: "))
    X = float(input("Введите х: "))
    Y = float(input("Введите у: "))
except Exception as e:
    print(e)
    print(e.__doc__)
    exit(1)

try:
    print('Start')
    if ((0 <= X <= R) and (0 <= Y <= R) and (R**2 <= X**2 + Y**2)) or ((R**2 >= X**2 + Y**2) and (Y >= X + R)) \
            or ((-R <= X <= 0) and (-R <= Y <= 0) and (R**2 <= X**2 + Y**2)) or ((R**2 >= X**2 + Y**2) and (Y <= X - R)):
        print('Попал!')
    else:
        print("Не попал!")
except Exception as e:
    print(e)
    print(e.__doc__)
    exit(1)
