from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info_string: str) -> str:
    """Принимает строку с типом и номером карты/счета и возвращает её с маской."""
    # Метод rpartition(' ') делит строку по самому ПОСЛЕДНЕМУ пробелу.
    # Это идеально подходит для названий типа "Visa Platinum 7000792289606361"
    name, sep, number = info_string.rpartition(" ")

    if "Счет" in name:
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{name}{sep}{masked_number}"


def get_date(date_string: str) -> str:
    """Принимает строку с датой и возвращает её в формате ДД.ММ.ГГГГ."""
    # Берем первые 10 символов: "2024-03-11"
    date_part = date_string[:10]

    # Разбиваем по дефису на составляющие
    year, month, day = date_part.split("-")

    # Собираем в нужном формате
    return f"{day}.{month}.{year}"