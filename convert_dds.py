import os
from PIL import Image

# ============ ПУТИ ============

# Папка, где лежат DDS-файлы
SOURCE_DIR = r"C:\Users\adria\Desktop\Карты вот"

# Папка Django, куда кладём PNG
TARGET_DIR = r"C:\Users\adria\PycharmProjects\PythonProjectWOT2025\picker\static\maps"


# ============ МАППИНГ ИМЁН ============

# Здесь мы говорим:
#   КЛЮЧ   = как называется файл .dds (без расширения)
#   ЗНАЧ   = как называется карта в проекте (slug, по-английски)
#
# Пример: eiffel_tower.dds -> paris.png
FILE_TO_SLUG = {
    # Уже были:
    "eiffel_tower": "paris",        # Париж
    "highground_v": "mines",        # Рудники
    "desert": "sand_river",         # Песчаная река

    # Новые, которые ты попросил:
    "cliff": "cliff",               # Утёс
    "dalny_gg": "el_halluf",        # Эль-Халлуф
    "frozen_land": "fishermans_bay",# Залив рыбака / Рыбацкая бухта
    "campania": "westfield",        # Вестфилд
    "lost_city": "lost_city",
    "mannerheim_line": "mannerheim_line",


}



def normalize_name(name: str) -> str:
    """
    Делает из имени файла базовое имя:
    'Malinovka.dds' -> 'malinovka'
    'highground v.DDS' -> 'highground_v'
    """
    name = name.strip().lower()
    name = name.replace(" ", "_")
    name = name.replace("-", "_")
    return name


def get_slug_from_filename(dds_filename: str) -> str:
    """
    По имени файла .dds возвращаем slug карты (как в БД/на сайте).
    """
    base, _ = os.path.splitext(dds_filename)   # 'eiffel_tower.dds' -> 'eiffel_tower'
    base = normalize_name(base)

    # если есть переопределение в словаре – берём его
    if base in FILE_TO_SLUG:
        return FILE_TO_SLUG[base]

    # иначе считаем, что slug такой же, как имя файла
    # (malinovka.dds -> malinovka.png)
    return base


def convert_one(dds_path: str, png_path: str):
    """
    Конвертация одного файла DDS -> PNG.
    """
    with Image.open(dds_path) as img:
        img.save(png_path, "PNG")


def convert_all():
    print("Начинаю конвертацию DDS → PNG...\n")

    if not os.path.isdir(SOURCE_DIR):
        print(f"[ОШИБКА] Папка с DDS не найдена: {SOURCE_DIR}")
        return

    os.makedirs(TARGET_DIR, exist_ok=True)

    files = [f for f in os.listdir(SOURCE_DIR) if f.lower().endswith(".dds")]
    if not files:
        print("[ВНИМАНИЕ] В папке нет .dds-файлов.")
        return

    for filename in files:
        dds_path = os.path.join(SOURCE_DIR, filename)
        slug = get_slug_from_filename(filename)
        png_name = f"{slug}.png"
        png_path = os.path.join(TARGET_DIR, png_name)

        print(f"Обрабатываю: {filename}  ->  {png_name}")

        try:
            convert_one(dds_path, png_path)
        except Exception as e:
            print(f"  [ОШИБКА] Не удалось конвертировать {filename}: {e}")

    print("\nГотово! Все миникарты сохранены в", TARGET_DIR)


if __name__ == "__main__":
    convert_all()
