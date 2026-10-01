import pytest

from src.calculate_logarithm import calculate_logarithm


def test_calculate_logarithm_with_negative_number():
    with pytest.raises(ValueError) as exc_info:
        calculate_logarithm(-1)

    # Проверяем, что сообщение об ошибке соответствует ожидаемому
    assert str(exc_info.value) == ("Логарифм можно вычислить только для "
                                   "положительных чисел")
