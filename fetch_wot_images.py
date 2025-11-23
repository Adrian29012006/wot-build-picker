import json
import os
from pathlib import Path

import requests

# ============== НАСТРОЙКИ ==============

# ТВОЙ application_id от Wargaming API
APPLICATION_ID = "74e2d4aabb1012e8491c1ae077f0b700"  # <-- твой app_id (как на скрине)

# Сервер (EU/NA/RU и т.д.) — у тебя, скорее всего, eu
REALM = "eu"

# Путь к tanks_eu.json (подстрой под свой проект)
# Пример: ПРОЕКТ/picker/data/tanks_eu.json
BASE_DIR = Path(__file__).resolve().parent
JSON_PATH = BASE_DIR / "picker" / "data" / "tanks_eu.json"

# Куда сохранять картинки (папка внутри static)
# В итоге картинки будут лежать в: project/static/picker/tanks
STATIC_TANKS_DIR = BASE_DIR / "static" / "picker" / "tanks"

# Какой тип картинки брать с WG API: "big_icon", "contour_icon", "small_icon", "preview", "big"
IMAGE_FIELD = "big_icon"


# ============== ХЕЛПЕРЫ ==============

def ensure_dirs():
    STATIC_TANKS_DIR.mkdir(parents=True, exist_ok=True)


def load_json():
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(data):
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def fetch_vehicle_info(tank_ids):
    """
    tank_ids: список int или str.
    Возвращает dict: {tank_id(str): { ... данные ... }}
    """
    url = f"https://api.worldoftanks.{REALM}/wot/encyclopedia/vehicles/"
    params = {
        "application_id": APPLICATION_ID,
        "tank_id": ",".join(str(tid) for tid in tank_ids),
    }
    resp = requests.get(url, params=params, timeout=15)
    resp.raise_for_status()
    j = resp.json()
    if j.get("status") != "ok":
        raise RuntimeError(f"WG API error: {j}")
    return j.get("data", {})


def download_image(url, dest_path: Path):
    resp = requests.get(url, stream=True, timeout=30)
    resp.raise_for_status()
    with open(dest_path, "wb") as f:
        for chunk in resp.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)


# ============== ОСНОВНАЯ ЛОГИКА ==============

def main():
    if not APPLICATION_ID or APPLICATION_ID == "YOUR_APPLICATION_ID_HERE":
        print("❗ Укажи APPLICATION_ID в файле fetch_wot_images.py")
        return

    ensure_dirs()

    data = load_json()
    if not isinstance(data, list):
        print("Ожидался список танков в JSON.")
        return

    # Собираем все ID танков из JSON
    tank_ids = []
    for t in data:
        tid_raw = t.get("id")
        if tid_raw is None:
            continue
        tank_ids.append(tid_raw)  # тут нам пофиг, строка или int, WG всё равно

    print(f"Найдено танков в JSON: {len(tank_ids)}")

    CHUNK_SIZE = 50
    id_to_image_url = {}

    # Чанками ходим в WG API
    for i in range(0, len(tank_ids), CHUNK_SIZE):
        chunk = tank_ids[i:i + CHUNK_SIZE]
        print(f"Запрашиваю WG API для tank_id {chunk[0]}..{chunk[-1]} (всего {len(chunk)})")

        try:
            info = fetch_vehicle_info(chunk)
        except Exception as e:
            print(f"Ошибка при запросе WG API: {e}")
            continue

        for tid_str, vdata in info.items():
            images = vdata.get("images") or {}
            url = images.get(IMAGE_FIELD)
            if not url:
                continue
            try:
                tid_int = int(tid_str)
            except ValueError:
                # на всякий случай, но у ВГ там числа
                continue
            id_to_image_url[tid_int] = url

    print(f"Нашли картинок в WG API: {len(id_to_image_url)}")

    # Теперь обновляем JSON: приводим id из JSON к int, чтобы совпали ключи
    updated = 0
    for tank in data:
        tid_raw = tank.get("id")
        if tid_raw is None:
            continue

        try:
            tid_int = int(tid_raw)
        except (TypeError, ValueError):
            continue

        img_url = id_to_image_url.get(tid_int)
        if not img_url:
            continue

        filename = f"tank_{tid_int}.png"
        dest = STATIC_TANKS_DIR / filename

        if not dest.exists():
            print(f"Скачиваю {img_url} -> {dest}")
            try:
                download_image(img_url, dest)
            except Exception as e:
                print(f"Ошибка скачивания для tank_id={tid_int}: {e}")
                continue

        # Прописываем путь относительно static/
        tank["image_path"] = f"picker/tanks/{filename}"
        updated += 1

    save_json(data)
    print(f"Готово. Обновлено танков с image_path: {updated}")


if __name__ == "__main__":
    main()
