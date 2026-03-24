cat > settings.php << 'EOF'
<?php

return [
    'db_host' => 'localhost',
    'db_name' => 'app_db',
    'db_user' => 'app_user',
    'db_pass' => 'secret',

    // Путь к каталогу данных MySQL
    'db_data_path' => '/var/lib/mysql/data',

    // Дополнительные настройки
    'log_path' => '/var/log/app.log'
];
EOF

echo "Исходное содержимое файла settings.php:"
echo "========================================"
cat settings.php
echo "========================================\n"

# Теперь выполняем замену пути
sed -i 's|/var/lib/mysql/data|/mnt/ssd/mysql|' settings.php

echo "Содержимое файла после замены:"
echo "========================================"
cat settings.php
echo "========================================"
