from typing import Any, Dict, List


def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Фильтрует список словарей по значению ключа 'state'.
    Возвращает новый список, не изменяя исходный.
    """
    # Создаем новый пустой список для отфильтрованных данных
    filtered_list = []

    # Перебираем каждый словарь в исходном списке
    for item in data:
        # Проверяем, совпадает ли статус с искомым
        if item.get('state') == state:
            # Если совпадает, добавляем копию или сам словарь в новый список
            filtered_list.append(item)

    return filtered_list


def sort_by_date(data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список словарей по ключу 'date'.
    По умолчанию сортировка идет по убыванию (от самых свежих к более старым).
    """
    # Используем встроенную функцию sorted, которая возвращает НОВЫЙ список.
    # В качестве ключа сортировки (key) передаем lambda-функцию.
    # Она берет каждый словарь и достает из него значение по ключу 'date'.
    sorted_list = sorted(
        data,
        key=lambda item: item.get('date', ''),
        reverse=reverse
    )

    return sorted_list


# Пример для проверки работы (блок кода ниже не выполнится при импорте модуля)
if __name__ == "__main__":
    test_data = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]

    print("--- Проверка фильтрации ---")
    print("По умолчанию (EXECUTED):", filter_by_state(test_data))
    print("Статус CANCELED:", filter_by_state(test_data, 'CANCELED'))

    print("\n--- Проверка сортировки ---")
    print("По убыванию (свежие первые):", sort_by_date(test_data))
    print("По возрастанию (старые первые):", sort_by_date(test_data, reverse=False))
