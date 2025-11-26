from pathlib import Path

import requests
from django.conf import settings
from django.core.management.base import BaseCommand

# Сюда впиши ссылки на миникарты.
# КЛЮЧИ = wg_id (или slug) карты, ЗНАЧЕНИЕ = ссылка на картинку
MAP_IMAGES = {
    "prokhorovka": "URL_КАРТИНКИ_ПРОКОРОВКИ",
    "malinovka": "URL_КАРТИНКИ_МАЛИНОВКИ",
    "redshire": "URL_КАРТИНКИ_REDSHIRE",
    "ruinberg": "URL_КАРТИНКИ_RUINBERG",
    "himmelsdorf": "URL_КАРТИНКИ_HIMMELSDORF",
    "fishermans_bay": "URL_КАРТИНКИ_FISHERMANS_BAY",
    # добавишь остальные по желанию
}


class Command(BaseCommand):
    help = "Скачивает миникарты и кладёт их в picker/static/maps"

    def handle(self, *args, **options):
        # Папка назначения: picker/static/maps
        output_dir: Path = settings.BASE_DIR / "picker" / "static" / "maps"
        output_dir.mkdir(parents=True, exist_ok=True)

        self.stdout.write(self.style.SUCCESS(f"Папка для карт: {output_dir}"))

        downloaded = 0
        for wg_id, url in MAP_IMAGES.items():
            filename = output_dir / f"{wg_id}.png"

            try:
                self.stdout.write(f"Скачиваю {wg_id} из {url}...")
                resp = requests.get(url, timeout=15)
                resp.raise_for_status()

                with open(filename, "wb") as f:
                    f.write(resp.content)

                downloaded += 1
                self.stdout.write(self.style.SUCCESS(f"  ✔ {wg_id}.png сохранён"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"  ✖ Ошибка для {wg_id}: {e}"))

        self.stdout.write(self.style.SUCCESS(f"Готово! Скачано файлов: {downloaded}"))
