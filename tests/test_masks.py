import pytest
from src.masks import get_mask_account, get_mask_card_number  # Путь зависит от твоей структуры проекта


# --- Тестирование get_mask_card_number ---
@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),  # Стандартный номер
        ("1234567890123456", "1234 56** **** 3456"),  # Другой стандартный номер
        ("", " ** **** "),  # Граничный случай: пустая строка
        ("1234", "1234 ** **** "),  # Короткая строка (проверка срезов)
    ],
)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


# --- Тестирование get_mask_account ---
@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("73654108430135874305", "**4305"),  # Стандартный номер счета
        ("1234", "**1234"),  # Длина ровно 4 символа
        ("", "**"),  # Пустая строка
        ("12", "**12"),  # Длина меньше 4 символов
    ],
)
def test_get_mask_account(account_number: str, expected: str) -> None:
    assert get_mask_account(account_number) == expected
