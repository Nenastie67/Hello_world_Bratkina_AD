#!/bin/bash

# Скрипт для подсчета нуклеотидов в FASTA файлах

# Вывод заголовка таблицы
printf "%-20s %-8s %-8s %-8s %-8s\n" "Файл" "A" "T" "G" "C"
printf "%s\n" "----------------------------------------------------------------"

# Перебираем все FASTA файлы в текущей папке
for file in *.fasta; do
    # Проверяем, существует ли файл (на случай, если нет .fasta файлов)
    [ -e "$file" ] || continue
    
    # Пропускаем пустые файлы (размер 0 байт)
    if [ ! -s "$file" ]; then
        continue
    fi
    
    # Извлекаем последовательность (удаляем заголовки и объединяем строки)
    sequence=$(grep -v "^>" "$file" | tr -d '\n' | tr -d ' ')
    
    # Подсчет нуклеотидов (регистронезависимый)
    a_count=$(echo "$sequence" | grep -o "[Aa]" | wc -l)
    t_count=$(echo "$sequence" | grep -o "[Tt]" | wc -l)
    g_count=$(echo "$sequence" | grep -o "[Gg]" | wc -l)
    c_count=$(echo "$sequence" | grep -o "[Cc]" | wc -l)
    
    # Вывод результатов
    printf "%-20s %-8d %-8d %-8d %-8d\n" "$file" "$a_count" "$t_count" "$g_count" "$c_count"
done

echo "----------------------------------------------------------------"
