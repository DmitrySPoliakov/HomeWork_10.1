from src.widget import get_date, mask_account_card

# Проверка маскирования
print(mask_account_card("Visa Platinum 7000792289606361"))
# Выведет: Visa Platinum 7000 79** **** 6361

print(mask_account_card("Счет 73654108430135874305"))
# Выведет: Счет **4305

print(mask_account_card("Maestro 1596837868705199"))
# Выведет: Maestro 1596 83** **** 1999

# Проверка даты
print(get_date("2024-03-11T02:26:18.671407"))
# Выведет: 11.03.2024
