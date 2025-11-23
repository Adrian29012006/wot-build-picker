import json
from pathlib import Path
import requests

# ❗ СЮДА ВСТАВЬ СВОЙ MOBILE application_id
# пример: "3e614a24bf6ab45bd7844d1bec28b6f1"
APPLICATION_ID = "3e614a24bf6ab45bd7844d1bec28b6f1"

API_URL = "https://api.worldoftanks.eu/wot/encyclopedia/vehicles/"

# соответствие типов из WG → наши классы
TYPE_TO_CLASS = {
    "heavyTank": "HT",
    "mediumTank": "MT",
    "lightTank": "LT",
    "AT-SPG": "TD",
    # "SPG": "ARTY"  # арту НЕ берём
}


def fetch_all_vehicles():
    """Запрос всех танков у WG API (EU сервер)"""
    params = {
        "application_id": APPLICATION_ID,
        "language": "en",
        "fields": "tank_id,name,nation,type,tier,is_premium",
        "limit": 10000,
    }

    print("Запрос списка танков у WG API...")
    resp = requests.get(API_URL, params=params, timeout=15)
    resp.raise_for_status()

    data = resp.json()
    # если API вернул ошибку — сразу вывалимся с понятным текстом
    if data.get("status") != "ok":
        raise RuntimeError(f"WG API error: {data}")

    # data["data"] — это СЛОВАРЬ {tank_id: {...}}
    vehicles_dict = data["data"]
    print(f"Получено записей: {len(vehicles_dict)}")

    # берём только значения (сами танки), чтобы дальше были dict, а не строки
    return list(vehicles_dict.values())


def normalize_tank(v: dict):
    """Преобразуем один танк из формата WG → наш формат"""

    # пропускаем арту
    if v["type"] == "SPG":
        return None

    tank_class = TYPE_TO_CLASS.get(v["type"])
    if not tank_class:
        return None

    return {
        "id": str(v["tank_id"]),
        "tier": v["tier"],
        "nation": v["nation"],
        "class": tank_class,
        "names": {
            # пока используем одно и то же имя на всех языках
            "uk": v["name"],
            "ru": v["name"],
            "en": v["name"],
        },
    }


def main():
    vehicles = fetch_all_vehicles()
    result = []

    print("Обработка танков...")

    for v in vehicles:
        tank = normalize_tank(v)
        if tank:
            result.append(tank)

    print(f"Итого танков (без арты): {len(result)}")

    # путь к JSON-файлу picker/data/tanks_eu.json
    json_path = Path(__file__).resolve().parent / "picker" / "data" / "tanks_eu.json"
    json_path.parent.mkdir(parents=True, exist_ok=True)

    # запись файла
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print("Готово!")
    print("Файл сохранён сюда:")
    print(json_path)


if __name__ == "__main__":
    main()

