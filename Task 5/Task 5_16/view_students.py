import psycopg2

connection = None
cursor = None

try:
    connection = psycopg2.connect(
        host="localhost",
        port="5432",
        user="student",
        password="student",
        database="taskdb"
    )
    cursor = connection.cursor()

    # Ваш запрос на выборку данных
    cursor.execute("SELECT * FROM courses;")
    students = cursor.fetchall()

    print("=" * 40)
    print("ДАННЫЕ ТАБЛИЦЫ students:")
    print("=" * 40)
    
    for student in students:
        print(student)  # Выведет всю строку целиком

except Exception as error:
    print(f"Ошибка: {error}")

finally:
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()
        print("\nСоединение закрыто.")