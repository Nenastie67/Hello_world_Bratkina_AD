import psycopg2

try:
    # Устанавливаем соединение с вашими параметрами
    connection = psycopg2.connect(
        host="localhost",
        port="5432",
        user="student",
        password="student",
        database="taskdb"
    )

    print("Подключение к базе данных прошло успешно!")
    
    # Проверяем информацию о сервере
    cursor = connection.cursor()
    
    # Версия PostgreSQL
    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    print(f"Версия PostgreSQL: {version[0]}")
    
    # Текущая база данных и пользователь
    cursor.execute("SELECT current_database(), current_user;")
    db_info = cursor.fetchone()
    print(f"База данных: {db_info[0]}, Пользователь: {db_info[1]}")
    
    # Закрываем соединение
    cursor.close()
    connection.close()
    print("Соединение закрыто.")

except Exception as error:
    print(f"Ошибка при подключении: {error}")
    print("\nПроверьте:")
    print("1. Запущен ли контейнер: docker ps")
    print("2. Правильные ли учётные данные")
    print("3. Не занят ли порт 5432 другим приложением")