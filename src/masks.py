def get_mask_card_number(card_number):
    """Маскирует номер карты в формат XXXX XX** **** XXXX"""

    card_str = str(card_number)

    # Вырезаем нужные части:
    first_block = card_str[0:4]    # Первые 4 цифры
    second_block = card_str[4:6]   # 5-я и 6-я цифры
    last_block = card_str[12:16]   # Последние 4 цифры

    # Собираем всё в одну строку с пробелами и звёздочками
    result = first_block + " " + second_block + "** **** " + last_block
    return result


def get_mask_account(account_number):
    """Маскирует номер счета в формат **XXXX"""
    # Превращаем в строку
    account_str = str(account_number)

    # Вырезаем последние 4 цифры с конца строки
    last_four = account_str[-4:]

    # Склеиваем две звёздочки и эти цифры
    result = "**" + last_four
    return result