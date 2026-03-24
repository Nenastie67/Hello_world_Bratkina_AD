cat > students.txt << 'EOF'
Ivan 78
Maria 92
Oleg 67
Anna 85
EOF

echo "=== Исходный файл students.txt ==="
cat students.txt
echo ""

# 1. Выводим только имена студентов (первая колонка)
echo "=== Только имена студентов (колонка 1) ==="
awk '{print $1}' students.txt
echo ""

# 2. Выводим только оценки студентов (вторая колонка)
echo "=== Только оценки студентов (колонка 2) ==="
awk '{print $2}' students.txt
echo ""

# 3. Выводим номер строки и имя студента
echo "=== Номер строки и имя студента ==="
awk '{print NR, $1}' students.txt
echo ""

# Дополнительно: форматированный вывод с разделителем
echo "=== Форматированный вывод (номер: имя) ==="
awk '{print NR ":" $1}' students.txt
