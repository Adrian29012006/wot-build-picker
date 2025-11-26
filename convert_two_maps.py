import os
from PIL import Image

# Папка, где лежат два DDS (твоя папка "Карты вот")
SOURCE_DIR = r"C:\Users\adria\Desktop\Карты вот"

# Папка Django, куда кладём готовые PNG
TARGET_DIR = r"C:\Users\adria\PycharmProjects\PythonProjectWOT2025\picker\static\maps"

# Соответствие: имя DDS-файла -> имя PNG/slug
NAME_MAP = {
    "lost_city.dds": "lost_city",
    "mannerheim_line.dds": "mannerheim_line",
}


def convert_two_maps():
    print("Начинаю конвертацию двух карт из DDS в PNG...\n")

    if not os.path.isdir(SOURCE_DIR):
        print(f"❌ Папка с исходниками не найдена: {SOURCE_DIR}")
        return

    if not os.path.isdir(TARGET_DIR):
        print(f"❌ Папка назначения не найдена: {TARGET_DIR}")
        return

    for filename in os.listdir(SOURCE_DIR):
        lower = filename.lower()
        if lower not in NAME_MAP:
            # пропускаем всё лишнее, если вдруг появится
            continue

        src_path = os.path.join(SOURCE_DIR, filename)
        png_name = NAME_MAP[lower] + ".png"
        dst_path = os.path.join(TARGET_DIR, png_name)

        print(f"Обрабатываю {filename}  ->  {png_name}")

        try:
            with Image.open(src_path) as img:
                img = img.convert("RGB")  # на всякий случай
                img.save(dst_path, "PNG")
        except Exception as e:
            print(f"  ❌ Ошибка при конвертации {filename}: {e}")
        else:
            print(f"  ✅ Успешно сохранено: {dst_path}")

    print("\nГотово! Проверь папку static/maps.")


if __name__ == "__main__":
    convert_two_maps()
