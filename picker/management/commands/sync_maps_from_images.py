from django.core.management.base import BaseCommand
from django.conf import settings
from picker.models import Map
import os

class Command(BaseCommand):
    help = "Создаёт недостающие карты на основе файлов в static/maps"

    def handle(self, *args, **options):
        # Папка с миникартами
        maps_dir = os.path.join(settings.BASE_DIR, "picker", "static", "maps")

        if not os.path.isdir(maps_dir):
            self.stderr.write(f"Папка с картами не найдена: {maps_dir}")
            return

        created = 0
        skipped = 0

        for file_name in os.listdir(maps_dir):
            if not file_name.lower().endswith(".png"):
                continue

            wg_id = os.path.splitext(file_name)[0]  # имя файла без .png

            # Уже есть такая карта в БД?
            if Map.objects.filter(wg_id=wg_id).exists():
                skipped += 1
                continue

            # Создаём новую карту с базовыми значениями
            Map.objects.create(
                wg_id=wg_id,
                name_ru=wg_id,          # потом поправишь в админке
                slug=wg_id,             # чтобы работала страница деталей
                size_m=1000,            # временно, можно править
                wg_type="random",       # тоже потом поменяем
                layout_type="Смешанная"
            )
            created += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Готово! Создано новых карт: {created}, пропущено (уже были): {skipped}"
            )
        )
