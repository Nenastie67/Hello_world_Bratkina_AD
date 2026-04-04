array = [7, 3, 8, 1, 4, 6, 2, 5]

print("Исходный массив:", array)
print("=" * 60)

n = len(array)

for i in range(n):
    print(f"\nПроход {i + 1}:")
    for j in range(n - i - 1):
        print(f"  Сравниваем array[{j}] = {array[j]} и array[{j + 1}] = {array[j + 1]}", end=" ")
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
            print("→ Меняем местами →", array)
        else:
            print("→ Оставляем без изменений →", array)
    
    print(f"  Результат прохода {i + 1}: {array}")

print("=" * 60)
print("Отсортированный массив:", array)