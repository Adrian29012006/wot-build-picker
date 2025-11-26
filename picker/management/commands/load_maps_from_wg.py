import requests
from django.core.management.base import BaseCommand
from django.utils.text import slugify

from picker.models import Map


# Статический список карт WoT (данные для ВГ, но без привязки к серверу)
STATIC_MAPS = [
    # open / летние
    {"wg_id": "prokhorovka", "name_ru": "Прокоровка", "size_m": 1000, "layout_type": "open", "wg_type": "summer"},
    {"wg_id": "malinovka", "name_ru": "Малиновка", "size_m": 1000, "layout_type": "open", "wg_type": "summer"},
    {"wg_id": "steppes", "name_ru": "Степи", "size_m": 1000, "layout_type": "open", "wg_type": "summer"},
    {"wg_id": "karelia", "name_ru": "Карелия", "size_m": 1000, "layout_type": "open", "wg_type": "summer"},
    {"wg_id": "sand_river", "name_ru": "Песчаная река", "size_m": 1000, "layout_type": "open", "wg_type": "desert"},
    {"wg_id": "el_halluf", "name_ru": "Эль-Халлуф", "size_m": 1000, "layout_type": "open", "wg_type": "desert"},

    # mixed
    {"wg_id": "fishermans_bay", "name_ru": "Залив рыбака", "size_m": 1000, "layout_type": "mixed", "wg_type": "summer"},
    {"wg_id": "westfield", "name_ru": "Вестфилд", "size_m": 1000, "layout_type": "mixed", "wg_type": "summer"},
    {"wg_id": "redshire", "name_ru": "Редшир", "size_m": 1000, "layout_type": "mixed", "wg_type": "summer"},
    {"wg_id": "murovanka", "name_ru": "Мурованка", "size_m": 1000, "layout_type": "mixed", "wg_type": "summer"},
    {"wg_id": "abbey", "name_ru": "Утёс", "size_m": 1000, "layout_type": "mixed", "wg_type": "summer"},
    {"wg_id": "cliff", "name_ru": "Утёс (Cliff)", "size_m": 1000, "layout_type": "mixed", "wg_type": "summer"},
    {"wg_id": "ruinberg", "name_ru": "Руинберг", "size_m": 800, "layout_type": "mixed", "wg_type": "summer"},
    {"wg_id": "arctic_region", "name_ru": "Арктик", "size_m": 1000, "layout_type": "mixed", "wg_type": "winter"},

    # city
    {"wg_id": "himmelsdorf", "name_ru": "Химмельсдорф", "size_m": 800, "layout_type": "city", "wg_type": "summer"},
    {"wg_id": "ensk", "name_ru": "Энск", "size_m": 800, "layout_type": "city", "wg_type": "summer"},
    {"wg_id": "paris", "name_ru": "Париж", "size_m": 1000, "layout_type": "city", "wg_type": "summer"},
    {"wg_id": "kharkov", "name_ru": "Харьков", "size_m": 1000, "layout_type": "city", "wg_type": "summer"},
    {"wg_id": "mines", "name_ru": "Рудники", "size_m": 800, "layout_type": "mixed", "wg_type": "summer"},
]


class Command(BaseCommand):
    help = "Пробует загрузить карты из WG API, если пусто — создаёт карты из STATIC_MAPS"

    def add_arguments(self, parser):
        parser.add_argument(
            '--app-id',
            type=str,
            help='WG API application_id',
            required=True,
        )
        parser.add_argument(
            '--region',
            type=str,
            default='eu',
            help='Регион WG API: eu, na, asia',
        )

    def handle(self, *args, **options):
        app_id = options['app_id']
        region = options['region']

        # 1. Пробуем взять карты из WG
        arenas = self._try_fetch_from_wg(app_id, region)

        if arenas:
            self.stdout.write(self.style.SUCCESS(
                f'WG API вернул {len(arenas)} карт, создаю их...'
            ))
            self._create_from_wg_data(arenas)
        else:
            # 2. Если WG ничего не вернул — используем STATIC_MAPS
            self.stdout.write(self.style.WARNING(
                'WG API не вернул карты (data пустой). '
                'Создаю карты из статического списка.'
            ))
            self._create_from_static()

    # ---------- ВСПОМОГАТЕЛЬНЫЕ МЕТОДЫ ----------

    def _try_fetch_from_wg(self, app_id: str, region: str):
        """Запрос к WG API. Если что-то пошло не так — возвращаем None."""
        base_url = f'https://api.worldoftanks.{region}/wot/encyclopedia/arenas/'
        params = {
            'application_id': app_id,
            'language': 'ru',
        }

        self.stdout.write(self.style.WARNING(f'Запрос к WG API: {base_url}'))

        try:
            response = requests.get(base_url, params=params, timeout=10)
        except requests.RequestException as e:
            self.stdout.write(self.style.ERROR(f'Ошибка запроса к WG API: {e}'))
            return None

        if response.status_code != 200:
            self.stdout.write(self.style.ERROR(
                f'HTTP ошибка {response.status_code}: {response.text[:200]}'
            ))
            return None

        data = response.json()
        if data.get('status') != 'ok':
            self.stdout.write(self.style.ERROR(f"WG API error: {data}"))
            return None

        arenas = data.get('data', {})
        self.stdout.write(self.style.SUCCESS(
            f'WG API ответил, карт в data: {len(arenas)}'
        ))
        return arenas or None

    def _create_from_wg_data(self, arenas: dict):
        """Создание/обновление карт по данным WG (если они вообще есть)."""
        created_count = 0
        updated_count = 0

        for wg_id, arena in arenas.items():
            name_ru = arena.get('name_i18n') or arena.get('name') or wg_id

            # slug = wg_id, чтобы всегда был латиницей и уникальный
            slug = wg_id

            # размер карты
            size_m = None
            size_data = arena.get('size')
            if isinstance(size_data, (list, tuple)) and len(size_data) >= 1:
                try:
                    size_m = int(size_data[0])
                except (ValueError, TypeError):
                    size_m = None

            # тип местности
            environment = arena.get('environment')
            if environment == 'summer':
                wg_type = 'summer'
            elif environment == 'winter':
                wg_type = 'winter'
            elif environment == 'desert':
                wg_type = 'desert'
            else:
                wg_type = None

            minimap_url = arena.get('icon') or arena.get('minimap') or None

            obj, created = Map.objects.update_or_create(
                wg_id=wg_id,
                defaults={
                    'name_ru': name_ru,
                    'slug': slug,
                    'size_m': size_m,
                    'wg_type': wg_type,
                    'layout_type': None,
                    'minimap_image': minimap_url,
                },
            )

            if created:
                created_count += 1
            else:
                updated_count += 1

        self.stdout.write(self.style.SUCCESS(
            f'ГОТОВО (WG): создано {created_count}, обновлено {updated_count}'
        ))

    def _create_from_static(self):
        """Создание/обновление карт из нашего списка STATIC_MAPS."""
        created_count = 0
        updated_count = 0

        for m in STATIC_MAPS:
            name_ru = m["name_ru"]
            wg_id = m["wg_id"]
            size_m = m.get("size_m")
            layout_type = m.get("layout_type")
            wg_type = m.get("wg_type")

            # slug всегда = wg_id
            slug = wg_id

            obj, created = Map.objects.update_or_create(
                wg_id=wg_id,
                defaults={
                    "name_ru": name_ru,
                    "slug": slug,
                    "size_m": size_m,
                    "wg_type": wg_type,
                    "layout_type": layout_type,
                    "minimap_image": None,
                },
            )

            if created:
                created_count += 1
            else:
                updated_count += 1

        self.stdout.write(self.style.SUCCESS(
            f"ГОТОВО (STATIC): создано {created_count}, обновлено {updated_count}"
        ))

