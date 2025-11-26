import os
import requests

from django.core.management.base import BaseCommand


# Куда складываем миникарты
SAVE_DIR = os.path.join("static", "maps")

# wg_id -> прямой URL на миникарту (160x160) с WG Wiki CDN
# ТЕБЕ НИЧЕГО ИСКАТЬ НЕ НАДО – ссылки уже готовы
MAP_IMAGES = {
    "prokhorovka": "https://wiki.wgcdn.co/images/thumb/c/c2/Prokhorovka.png/160px-Prokhorovka.png",
    "malinovka": "https://wiki.wgcdn.co/images/thumb/b/b9/Malinovka.png/160px-Malinovka.png",
    "himmelsdorf": "https://wiki.wgcdn.co/images/thumb/c/c3/Himmelsdorf.png/160px-Himmelsdorf.png",
    "redshire": "https://wiki.wgcdn.co/images/thumb/8/86/Redshire.png/160px-Redshire.png",
    "fishermans_bay": "https://wiki.wgcdn.co/images/thumb/6/6a/Fisherman%27s_Bay.png/160px-Fisherman%27s_Bay.png",
    "ruinberg": "https://wiki.wgcdn.co/images/thumb/2/28/Ruinberg.png/160px-Ruinberg.png",
    # можно дописывать остальные карты по желанию
}


class Command(BaseCommand):
    help = "Скачивает миникарты WoT в static/maps по wg_id"

    def handle(self, *args, **options):
        os.makedirs(SAVE_DIR, exist_ok=True)
        self.stdout.write(self.style.SUCCESS(
            f"Папка для миникарт: {os.path.abspath(SAVE_DIR)}"
        ))

        for wg_id, url in MAP_IMAGES.items():
            filename = f"{wg_id}.png"
            filepath = os.path.join(SAVE_DIR, filename)

            self.stdout.write(f"Скачиваю {wg_id} из {url} ...")

            try:
                resp = requests.get(url, timeout=15)
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"  ОШИБКА запроса: {e}"))
                continue

            if resp.status_code == 200:
                with open(filepath, "wb") as f:
                    f.write(resp.content)
                self.stdout.write(self.style.SUCCESS(
                    f"  OK: сохранено в {filepath}"
                ))
            else:
                self.stdout.write(self.style.ERROR(
                    f"  HTTP {resp.status_code}: первые 200 символов ответа:\n{resp.text[:200]}"
                ))

        self.stdout.write(self.style.SUCCESS("Загрузка миникарт завершена."))
