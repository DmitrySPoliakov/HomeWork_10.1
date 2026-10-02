import pytest
from src.widget import get_date, mask_account_card


# --- Тестирование mask_account_card ---
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("Visa Gold 7000792289606361", "Visa Gold 7000 79** **** 6361"),  # Проверка ветки else (карта)
        ("Mastercard 1234567890123456", "Mastercard 1234 56** **** 3456"),
        ("Счет 73654108430135874305", "Счет **4305"),  # Проверка ветки if (счет)
        ("Maestro 123456", "Maestro 1234 56** **** "),  # Проверка короткого номера карты
    ],
)
def test_mask_account_card(input_str: str, expected: str) -> None:
    """Тестирует корректность распознавания карт и счетов, а также ветвление if/else."""
    assert mask_account_card(input_str) == expected


def test_mask_account_card_empty() -> None:
    """Проверяет устойчивость функции к пустой строке (ожидаем IndexError)."""
    with pytest.raises(IndexError):
        mask_account_card("")


# --- Тестирование get_date ---
@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2024-07-11T02:26:18.671407", "11.07.2024."),  # Стандартный ISO формат с точкой на конце
        ("2026-10-02T15:30:00", "02.10.2026."),  # Формат без миллисекунд с точкой на конце
    ],
)
def test_get_date(date_str: str, expected: str) -> None:
    """Тестирует правильность преобразования даты в формат ДД.ММ.ГГГГ."""
    assert get_date(date_str) == expected


def test_get_date_empty() -> None:
    """Проверяет поведение функции при передаче пустой строки (ожидаем ValueError)."""
    with pytest.raises(ValueError):
        get_date("")
