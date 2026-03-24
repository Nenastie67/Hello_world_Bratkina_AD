echo "=== Исходные данные из файла students.txt ==="
cat students.txt
echo ""

# 1. Находим сумму всех оценок
echo "=== Сумма всех оценок ==="
awk '{sum += $2} END {print "Сумма: " sum " баллов"}' students.txt
echo ""

# 2. Находим среднюю оценку
echo "=== Средняя оценка ==="
awk '{sum += $2; count++} END {print "Средняя: " sum/count " баллов"}' students.txt
echo ""

# 3. Находим максимальную оценку
echo "=== Максимальная оценка ==="
awk 'NR==1 {max=$2; max_student=$1} $2>max {max=$2; max_student=$1} END {print "Максимум: " max_student " - " max " баллов"}' students.txt
echo ""

# Дополнительно: находим минимальную оценку
echo "=== Минимальная оценка (дополнительно) ==="
awk 'NR==1 {min=$2; min_student=$1} $2<min {min=$2; min_student=$1} END {print "Минимум: " min_student " - " min " баллов"}' students.txt
