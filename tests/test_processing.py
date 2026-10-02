from typing import Any, Dict, List
import pytest
from src.processing import filter_by_state, sort_by_date


# --- Тестирование filter_by_state ---
@pytest.mark.parametrize(
    "state, expected_count",
    [
        ("EXECUTED", 2),
        ("PROCESSING", 1),
        ("CANCELED", 1),
        ("PENDING", 0),  # Отсутствующий статус
    ],
)
def test_filter_by_state(sample_data: List[Dict[str, Any]], state: str, expected_count: int) -> None:
    result = filter_by_state(sample_data, state=state)
    assert len(result) == expected_count
    for item in result:
        assert item["state"] == state


# --- Тестирование sort_by_date ---
def test_sort_by_date_descending(sample_data: List[Dict[str, Any]]) -> None:
    """Тест сортировки по убыванию (по умолчанию)"""
    result = sort_by_date(sample_data)
    # Проверяем, что самый первый элемент — самый свежий (2021 год)
    assert result[0]["id"] == 11914217
    # Последний — самый старый (2018-06-30)
    assert result[-1]["id"] == 939719570


def test_sort_by_date_ascending(sample_data: List[Dict[str, Any]]) -> None:
    """Тест сортировки по возрастанию (reverse=False)"""
    result = sort_by_date(sample_data, reverse=False)
    # Теперь первый элемент должен быть самым старым
    assert result[0]["id"] == 939719570
    assert result[-1]["id"] == 11914217


def test_sort_by_date_missing_key() -> None:
    """Проверка устойчивости, если в словаре нет ключа 'date'"""
    # Добавляем явное указание типа List[Dict[str, Any]]:
    data_without_date: List[Dict[str, Any]] = [
        {"id": 1, "date": "2023-01-01T00:00:00"},
        {"id": 2},  # Нет ключа date
    ]
    result = sort_by_date(data_without_date)
    assert len(result) == 2
