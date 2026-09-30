import math


def calculate_logarithm(number: int | float) -> float:
    if number <= 0:
        raise ValueError("Логарифм можно вычислить только для положительных чисел")
    return math.log(number)
