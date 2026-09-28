from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info_string: str) -> str:
    """Функция принимает данные карты, берёт функцию """
    # Разделяем строку по пробелам на список слов
    # "Visa Platinum 7000792289606361" -> ['Visa', 'Platinum', '7000792289606361']
    items = info_string.split()
    # Забираем последнее слово (это всегда номер)
    number = items[-1]
    # Собираем обратно название, объединяя все элементы, кроме последнего
    # ['Visa', 'Platinum'] -> "Visa Platinum"
    name = " ".join(items[:-1])
    # Маскируем номер
    if "Счет" in name:
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)
    # Соединяем название и замаскированный номер обратно через пробел
    return f"{name} {masked_number}"


def get_date(date_string: str) -> str:
    """Принимает строку с датой и возвращает её в формате ДД.ММ.ГГГГ."""
    # Берем первые 10 символов: "2024-03-11"
    date_part = date_string[:10]

    # Разбиваем по дефису на составляющие
    year, month, day = date_part.split("-")

    # Собираем в нужном формате
    return f"{day}.{month}.{year}."
