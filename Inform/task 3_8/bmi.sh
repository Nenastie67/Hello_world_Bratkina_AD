#!/bin/bash

read -p "Введите вес (кг): " weight
read -p "Введите рост (м): " height


bmi=$(echo "$weight / ($height * $height)" 

echo "Ваш Индекс массы тела: $bmi"


