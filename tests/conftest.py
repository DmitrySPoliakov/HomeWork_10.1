from typing import Any, Dict, List
import pytest


@pytest.fixture
def sample_data() -> List[Dict[str, Any]]:
    """Базовый набор данных с корректными комбинациями state и date."""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:19.509775"},
        {"id": 939719570, "state": "PROCESSING", "date": "2018-06-30T02:08:58.425572"},
        {"id": 5942286, "state": "CANCELED", "date": "2018-07-21T14:54:14.394449"},
        {"id": 11914217, "state": "EXECUTED", "date": "2021-04-04T23:20:05.206878"},
    ]


@pytest.fixture
def data_with_missing_and_mixed_fields() -> List[Dict[str, Any]]:
    """Набор данных с граничными случаями: отсутствующие ключи, пустые значения и разные регистры."""
    return [
        {"id": 1, "state": "executed", "date": "2023-01-01T00:00:00"},  # Нижний регистр статуса
        {"id": 2, "state": "PENDING"},  # Отсутствует дата
        {"id": 3, "date": "2024-05-12T12:00:00"},  # Отсутствует статус state
        {"id": 4, "state": "", "date": ""},  # Пустые строки
    ]


@pytest.fixture
def data_same_dates() -> List[Dict[str, Any]]:
    """Набор данных с одинаковыми датами для проверки стабильности сортировки."""
    return [
        {"id": 10, "state": "EXECUTED", "date": "2025-10-02T15:30:00"},
        {"id": 20, "state": "EXECUTED", "date": "2025-10-02T15:30:00"},
    ]

