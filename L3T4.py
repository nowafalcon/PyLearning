# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в
# виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной
# функции возведения числа в степень.
x = input("Введите вещественное число Х: ")
y = input("Введите отрицательное значение Y: ")
"""

"""


def my_func1(x, y):
    try:
        if int(y) < 0:
            z = (1 / float(x)) ** abs(int(y))

        else:
            z = float(x) ** abs(int(y))
        print(f'My_Func1: X ^ Y = {z}')
        return
    except ValueError or TypeError:
        print("Попробуйте ввести подходящее число ^_^/`")


my_func1(x, y)


def my_func2(x, y):
    y = int(y)
    x = 1 / float(x)
    x2=x
    while y < -1:
        x2=x2*x
        y += 1
    print(f'My_Func2: X ^ Y = {x2}')
    return (x2)


my_func2(x, y)
