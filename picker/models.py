from django.db import models


class Map(models.Model):
    WG_TYPES = (
        ('summer', 'Летняя'),
        ('winter', 'Зимняя'),
        ('desert', 'Пустынная'),
    )

    LAYOUT_TYPES = (
        ('open', 'Открытая'),
        ('city', 'Городская'),
        ('mixed', 'Смешанная'),
    )

    # ID карты в API World of Tanks (arenas)
    wg_id = models.CharField(max_length=100, unique=True)

    # slug для URL (prokhorovka, himmelsdorf и т.д.)
    slug = models.SlugField(unique=True)

    # Названия карты на 3 языках
    name_ru = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100, blank=True, null=True)
    name_uk = models.CharField(max_length=100, blank=True, null=True)

    # Размер карты (например 800, 1000)
    size_m = models.IntegerField(blank=True, null=True)

    # Тип карты: open / city / mixed
    layout_type = models.CharField(
        max_length=20,
        choices=LAYOUT_TYPES,
        blank=True,
        null=True,
    )

    # Сезон: summer / winter / desert
    wg_type = models.CharField(
        max_length=20,
        choices=WG_TYPES,
        blank=True,
        null=True,
    )

    def get_name(self, lang: str) -> str:
        if lang == 'ru':
            return self.name_ru
        elif lang == 'en':
            return self.name_en or self.name_ru
        elif lang == 'uk':
            return self.name_uk or self.name_ru
        return self.name_ru

    def __str__(self):
        return self.name_ru
