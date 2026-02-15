# 1. ВВОД ДАННЫХ
# Функция input() выводит текст и ждет ввода от пользователя.
nutrient_medium = input("Введите название питательной среды: ")
agar_concentration = input("Введите концентрацию агара (%): ")
sterilization_temperature = input("Введите температуру стерилизации (°C): ")

# 2. РАБОТА С ФАЙЛОМ
# Менеджер контекста 'with' гарантирует закрытие файла.
# "w" — режим записи (write), очищает файл перед работой.
with open("recipe.txt", "w", encoding="utf-8") as card:
    
    # 3. ФОРМИРОВАНИЕ СТРОКИ И ЗАПИСЬ
    # \t — табуляция (отступ), \n — перенос на новую строку.
    card.write(f"{nutrient_medium}\nКонцентрация агара: {agar_concentration}\nТемпература стерилизации:{sterilization_temperature}")
    print(f"{nutrient_medium}\nКонцентрация агара: {agar_concentration}\nТемпература стерилизации:{sterilization_temperature}")
    
    print("Файл 'recipe.txt' успешно сформирован!")