#!/bin/bash

# Создание файлов
echo "Создание файлов test1.txt - test10.txt"
for i in {1..10}; do
    touch "test$i.txt"
    echo "Создан: test$i.txt"
done

# Удаление файлов в обратном порядке
echo -e "\nУдаление файлов в обратном порядке"
i=10
while [ $i -ge 1 ]; do
    rm "test$i.txt"
    echo "Удален: test$i.txt"
    ((i--))
done
