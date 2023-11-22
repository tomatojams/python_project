import math


def power(x, y):
    return math.pow(x, y)


def cubic(x):
    return x**3


def divide(x, y):
    if y == 0:
        raise ValueError("0으로 나눌수없습니다.")
    return x / y


def factorial(x):
    return math.factorial(x)
