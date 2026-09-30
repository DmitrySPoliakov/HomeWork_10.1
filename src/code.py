
import math
from typing import Union


def up_first(msg: str) -> str:
    """Делает первую букву строки заглавной."""
    if msg:
        return msg[0].upper() + msg[1:]
    else:
        return msg


def calculate_logarithm(number: float) -> float:
    """Вычисляет натуральный логарифм (ln) для заданного числа.

    Args:
        number (float): Положительное число для вычисления логарифма.

    Returns:
        float: Значение натурального логарифма.

    Raises:
        ValueError: Если передано число меньше или равное нулю.
    """
    if number <= 0:
        raise ValueError(
            "Логарифм можно вычислить только для положительных чисел"
        )
    return math.log(number)


def revers_string(my_string: Union[str, int, float]) -> str:
    """Возвращает строку в обратном порядке."""
    return str(my_string)[::-1]
