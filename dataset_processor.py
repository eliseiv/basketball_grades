import os
from PIL import Image

# Указываем папки
# Папка с исходными фото
input_folder = "C:\\Users\\DellXPS\\Downloads\\Python\\Новая папка\\basketball_grades\\psa11"
# Куда сохраняем сжатые фото
output_folder = "C:\\Users\\DellXPS\\Downloads\\Python\\Новая папка\\basketball_grades\\psa111"
max_size_kb = 20  # Максимальный размер файла в KB

# Создаём выходную папку, если её нет
os.makedirs(output_folder, exist_ok=True)

# Обрабатываем файлы
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):  # Поддерживаемые форматы
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Проверяем размер файла
        file_size_kb = os.path.getsize(input_path) / 1024  # Перевод в KB

        if file_size_kb > max_size_kb:
            with Image.open(input_path) as img:
                quality = 95  # Начальное качество
                while file_size_kb > max_size_kb and quality > 5:
                    img.save(output_path, quality=quality, optimize=True)
                    file_size_kb = os.path.getsize(output_path) / 1024
                    quality -= 5  # Понижаем качество на 5%

        else:
            # Если размер нормальный, просто копируем изображение
            with Image.open(input_path) as img:
                img.save(output_path)

print("Сжатие изображений завершено!")
