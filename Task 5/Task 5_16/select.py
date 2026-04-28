import psycopg2

try:
    # Устанавливаем соединение
    connection = psycopg2.connect(
        host="localhost",
        port="5432",
        user="student",
        password="student",
        database="taskdb"
    )

    # Создаём курсор
    cursor = connection.cursor()

    # 1. Выполняем запрос
    cursor.execute("SELECT first_name, last_name FROM students;")

    # 2. Извлекаем все строки
    students = cursor.fetchall()

    for student in students:
        print(f"Студент: {student[0]} {student[1]}")

    # Не забываем закрыть курсор
    cursor.close()

except Exception as error:
    print(f"Ошибка: {error}")

finally:
    # Закрываем соединение
    if 'connection' in locals() and connection:
        connection.close()
        print("Соединение закрыто.")