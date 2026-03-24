#!/bin/bash

# Простой калькулятор BMI

echo "Калькулятор BMI"
echo "================"

# Запрашиваем данные
read -p "Введите вес (кг): " weight
read -p "Введите рост (м): " height

# Считаем BMI (целое число)
bmi=$(echo "$weight / ($height * $height)" | bc | cut -d '.' -f1)

# Выводим результат
echo "================"
echo "Ваш BMI: $bmi"
