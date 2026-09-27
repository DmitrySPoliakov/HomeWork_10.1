# Виджет банковских операций

Проект предназначен для фильтрации и сортировки банковских операций клиента.

## Инструкция по установке

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com
   ```
2. Перейдите в папку проекта:
   ```bash
   cd название_репозитория
   ```

## Использование

Модуль `processing` содержит две основные функции:

* `filter_by_state(data, state='EXECUTED')` — фильтрует операции по их статусу.
* `sort_by_date(data, reverse=True)` — сортирует операции по дате (по умолчанию от самых свежих к более старым).

### Пример работы

```python
from src.processing import filter_by_state, sort_by_date

data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}
]

# Фильтрация
executed_data = filter_by_state(data)

# Сортировка
sorted_data = sort_by_date(data)
```