import psycopg2

# 1. Создаём переменные для соединения и курсора
connection = None
cursor = None

try:
    # 2. Устанавливаем соединение
    connection = psycopg2.connect(
        host="localhost",
        port="5432",
        user="student",
        password="student",
        database="taskdb"
    )
    print("✅ Соединение установлено!")

    # 3. Открываем курсор
    cursor = connection.cursor()
    print("✅ Курсор создан!")

    # 4. Выполняем SQL-запрос (получаем список всех таблиц в базе)
    cursor.execute("""
        SELECT table_name 
        FROM information_schema.tables 
        WHERE table_schema = 'public'
        ORDER BY table_name;
    """)

    # 5. Извлекаем и выводим результат
    tables = cursor.fetchall()
    
    print("\n" + "=" * 40)
    print("СПИСОК ТАБЛИЦ В БАЗЕ ДАННЫХ taskdb:")
    print("=" * 40)
    
    if tables:
        for table in tables:
            print(f"📁 {table[0]}")
    else:
        print("Таблицы не найдены.")

    print("=" * 40)

except Exception as error:
    print(f"❌ Ошибка: {error}")

finally:
    # 6. Закрываем курсор
    if cursor is not None:
        cursor.close()
        print("\n✅ Курсор закрыт!")

    # 7. Закрываем соединение
    if connection is not None:
        connection.close()
        print("✅ Соединение закрыто!")