import psycopg2

connection = None
cursor = None

try:
    # Устанавливаем соединение с ВАШИМИ параметрами
    connection = psycopg2.connect(
        host="localhost",
        port="5432",
        user="student",
        password="student",
        database="taskdb"
    )
    cursor = connection.cursor()

    # Выполняем обновление (замените на Вашу таблицу и данные)
    cursor.execute("UPDATE courses SET credits = 5 WHERE course_id = 1;")

    # КРИТИЧЕСКИ ВАЖНО: фиксируем изменения в базе
    connection.commit()
    print("Данные успешно обновлены!")

except Exception as error:
    if connection:
        # Если что-то пошло не так, отменяем всё (откат)
        connection.rollback()
    print(f"Ошибка: {error}")

finally:
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()
        print("Соединение закрыто.")