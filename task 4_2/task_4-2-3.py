N = int(input("Введите количество чисел N: ") )

A1 = float(input("Введите число 1: "))

max_value = A1
i = 2

while i <= N:
    Ai = float(input(f"Введите число {i}: "))
    if Ai > max_value:
        max_value = Ai
    i = i + 1

print(f"Максимальное число: {max_value}")