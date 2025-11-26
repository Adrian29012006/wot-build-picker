from django.db import migrations


def create_default_maps(apps, schema_editor):
    Map = apps.get_model("picker", "Map")

    maps_data = [
        # ===== ОТКРЫТЫЕ / ПОЛУОТКРЫТЫЕ КАРТЫ =====
        {
            "slug": "malinovka",
            "wg_id": "malinovka",
            "name_ru": "Малиновка",
            "name_uk": "Малинівка",
            "name_en": "Malinovka",
            "size_m": 1000,
            "layout_type": "open",
            "wg_type": "summer",
        },
        {
            "slug": "prokhorovka",
            "wg_id": "prokhorovka",
            "name_ru": "Прохоровка",
            "name_uk": "Прохорівка",
            "name_en": "Prokhorovka",
            "size_m": 1000,
            "layout_type": "open",
            "wg_type": "summer",
        },
        {
            "slug": "steppes",
            "wg_id": "steppes",
            "name_ru": "Степи",
            "name_uk": "Степи",
            "name_en": "Steppes",
            "size_m": 1000,
            "layout_type": "open",
            "wg_type": "summer",
        },
        {
            "slug": "sand_river",
            "wg_id": "sand_river",
            "name_ru": "Песчаная река",
            "name_uk": "Піщана ріка",
            "name_en": "Sand River",
            "size_m": 1000,
            "layout_type": "open",
            "wg_type": "desert",
        },

        # ===== СМЕШАННЫЕ КАРТЫ =====
        {
            "slug": "mines",
            "wg_id": "mines",
            "name_ru": "Рудники",
            "name_uk": "Рудники",
            "name_en": "Mines",
            "size_m": 800,
            "layout_type": "mixed",
            "wg_type": "summer",
        },
        {
            "slug": "redshire",
            "wg_id": "redshire",
            "name_ru": "Редшир",
            "name_uk": "Редшир",
            "name_en": "Redshire",
            "size_m": 1000,
            "layout_type": "mixed",
            "wg_type": "summer",
        },
        {
            "slug": "cliff",
            "wg_id": "cliff",
            "name_ru": "Утёс",
            "name_uk": "Утес",
            "name_en": "Cliff",
            "size_m": 1000,
            "layout_type": "mixed",
            "wg_type": "summer",
        },
        {
            "slug": "frozen_land",
            "wg_id": "frozen_land",
            "name_ru": "Заполярье",
            "name_uk": "Заполяр’я",
            "name_en": "Arctic Region",
            "size_m": 1000,
            "layout_type": "mixed",
            "wg_type": "winter",
        },

        # ===== ГОРОДСКИЕ КАРТЫ =====
        {
            "slug": "paris",
            "wg_id": "paris",
            "name_ru": "Париж",
            "name_uk": "Париж",
            "name_en": "Paris",
            "size_m": 1000,
            "layout_type": "city",
            "wg_type": "summer",
        },
        {
            "slug": "ensk",
            "wg_id": "ensk",
            "name_ru": "Энск",
            "name_uk": "Енськ",
            "name_en": "Ensk",
            "size_m": 800,
            "layout_type": "city",
            "wg_type": "summer",
        },
        {
            "slug": "ensk_big",
            "wg_id": "ensk_big",
            "name_ru": "Энск (большая)",
            "name_uk": "Енськ (велика)",
            "name_en": "Ensk (large)",
            "size_m": 1000,
            "layout_type": "city",
            "wg_type": "summer",
        },
        {
            "slug": "himmelsdorf",
            "wg_id": "himmelsdorf",
            "name_ru": "Химмельсдорф",
            "name_uk": "Хіммельсдорф",
            "name_en": "Himmelsdorf",
            "size_m": 800,
            "layout_type": "city",
            "wg_type": "summer",
        },
        {
            "slug": "ruinberg",
            "wg_id": "ruinberg",
            "name_ru": "Руинберг",
            "name_uk": "Руйнберг",
            "name_en": "Ruinberg",
            "size_m": 1000,
            "layout_type": "mixed",
            "wg_type": "summer",
        },
        {
            "slug": "fishing_bay",
            "wg_id": "fishing_bay",
            "name_ru": "Рыбацкая бухта",
            "name_uk": "Рибальська бухта",
            "name_en": "Fisherman’s Bay",
            "size_m": 1000,
            "layout_type": "mixed",
            "wg_type": "summer",
        },
        {
            "slug": "westfield",
            "wg_id": "westfield",
            "name_ru": "Вестфилд",
            "name_uk": "Вестфілд",
            "name_en": "Westfield",
            "size_m": 1000,
            "layout_type": "mixed",
            "wg_type": "summer",
        },

        # ===== ПРОЧИЕ КАРТЫ ИЗ ТВОЕГО СПИСКА =====
        {
            "slug": "airfield",
            "wg_id": "airfield",
            "name_ru": "Аэродром",
            "name_uk": "Аеродром",
            "name_en": "Airfield",
            "size_m": 1000,
            "layout_type": "open",
            "wg_type": "desert",
        },
        {
            "slug": "caucasus",
            "wg_id": "caucasus",
            "name_ru": "Перевал",          # ты просил переименовать Северогорск на Перевал
            "name_uk": "Перевал",
            "name_en": "Mountain Pass",
            "size_m": 1000,
            "layout_type": "mixed",
            "wg_type": "summer",
        },
        {
            "slug": "erlenberg",
            "wg_id": "erlenberg",
            "name_ru": "Эрленберг",
            "name_uk": "Ерленберг",
            "name_en": "Erlenberg",
            "size_m": 1000,
            "layout_type": "mixed",
            "wg_type": "winter",
        },
        {
            "slug": "karelia",
            "wg_id": "karelia",
            "name_ru": "Карелия",
            "name_uk": "Карелія",
            "name_en": "Karelia",
            "size_m": 800,
            "layout_type": "mixed",
            "wg_type": "summer",
        },
        {
            "slug": "lakeville",
            "wg_id": "lakeville",
            "name_ru": "Ласвилль",
            "name_uk": "Ласвілль",
            "name_en": "Lakeville",
            "size_m": 800,
            "layout_type": "mixed",
            "wg_type": "summer",
        },
        {
            "slug": "monastery",
            "wg_id": "monastery",
            "name_ru": "Монастырь",
            "name_uk": "Монастир",
            "name_en": "Sacred Valley",
            "size_m": 1000,
            "layout_type": "mixed",
            "wg_type": "summer",
        },
        {
            "slug": "murovanka",
            "wg_id": "murovanka",
            "name_ru": "Мурованка",
            "name_uk": "Мурованка",
            "name_en": "Murovanka",
            "size_m": 1000,
            "layout_type": "mixed",
            "wg_type": "summer",
        },
        {
            "slug": "siegfried_line",
            "wg_id": "siegfried_line",
            "name_ru": "Линия Зигфрида",
            "name_uk": "Лінія Зігфрида",
            "name_en": "Siegfried Line",
            "size_m": 1000,
            "layout_type": "mixed",
            "wg_type": "summer",
        },
        {
            "slug": "turning_point",
            "wg_id": "turning_point",
            "name_ru": "Перевал",
            "name_uk": "Перевал",
            "name_en": "Mountain Pass",
            "size_m": 1000,
            "layout_type": "mixed",
            "wg_type": "summer",
        },
        {
            "slug": "fjord",
            "wg_id": "fjord",
            "name_ru": "Фьорды",          # ты просил сделать Фьорды
            "name_uk": "Фіорди",
            "name_en": "Fjords",
            "size_m": 1000,
            "layout_type": "mixed",
            "wg_type": "summer",
        },

        # ===== ПУСТЫННЫЕ / ПРОЧИЕ =====
        {
            "slug": "el_halluf",
            "wg_id": "el_halluf",
            "name_ru": "Эль-Халлуф",
            "name_uk": "Ель-Халуф",
            "name_en": "El Halluf",
            "size_m": 1000,
            "layout_type": "mixed",
            "wg_type": "desert",
        },
        {
            "slug": "desert",
            "wg_id": "desert",
            "name_ru": "Пустыня",
            "name_uk": "Пустеля",
            "name_en": "Desert",
            "size_m": 1000,
            "layout_type": "open",
            "wg_type": "desert",
        },

        # ===== ТВОИ НОВЫЕ КАРТЫ =====
        {
            "slug": "lost_city",
            "wg_id": "lost_city",
            "name_ru": "Потерянный город",
            "name_uk": "Загублене місто",
            "name_en": "Lost City",
            "size_m": 800,
            "layout_type": "city",
            "wg_type": "summer",
        },
        {
            "slug": "mannerheim_line",
            "wg_id": "mannerheim_line",
            "name_ru": "Линия Маннергейма",
            "name_uk": "Лінія Маннергейма",
            "name_en": "Mannerheim Line",
            "size_m": 1000,
            "layout_type": "mixed",
            "wg_type": "winter",
        },
    ]

    for data in maps_data:
        defaults = data.copy()
        slug = defaults.pop("slug")
        Map.objects.update_or_create(slug=slug, defaults=defaults)


def delete_default_maps(apps, schema_editor):
    Map = apps.get_model("picker", "Map")
    slugs = [
        "malinovka",
        "prokhorovka",
        "steppes",
        "sand_river",
        "mines",
        "redshire",
        "cliff",
        "frozen_land",
        "paris",
        "ensk",
        "ensk_big",
        "himmelsdorf",
        "ruinberg",
        "fishing_bay",
        "westfield",
        "airfield",
        "caucasus",
        "erlenberg",
        "karelia",
        "lakeville",
        "monastery",
        "murovanka",
        "siegfried_line",
        "turning_point",
        "fjord",
        "el_halluf",
        "desert",
        "lost_city",
        "mannerheim_line",
    ]
    Map.objects.filter(slug__in=slugs).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("picker", "0001_initial"),  # если номер другой – поставь последнюю миграцию для picker
    ]

    operations = [
        migrations.RunPython(create_default_maps, delete_default_maps),
    ]
