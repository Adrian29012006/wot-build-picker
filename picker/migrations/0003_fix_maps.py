from django.db import migrations


def fix_maps(apps, schema_editor):
    Map = apps.get_model("picker", "Map")

    # 1) ДВА ВЕСТФИЛДА – удаляем лишний campania
    Map.objects.filter(slug="campania").delete()

    # 2) МЮНХЕН – удалить
    Map.objects.filter(slug="munchen").delete()

    # 3) Удалить Рудники (mines) и переименовать Холмы (hills) на Рудники
    Map.objects.filter(slug="mines").delete()

    try:
        hills = Map.objects.get(slug="hills")
        hills.name_ru = "Рудники"
        hills.name_uk = "Рудники"
        hills.name_en = "Mines"
        hills.save()
    except Map.DoesNotExist:
        pass

    # 4) Рыбацкая бухта с зимней заставкой – удалить зимние варианты
    Map.objects.filter(name_ru="Рыбацкая бухта", wg_type="winter").delete()

    # 5) Северогорск -> Перевал (slug=caucasus)
    try:
        caucasus = Map.objects.get(slug="caucasus")
        caucasus.name_ru = "Перевал"
        caucasus.name_uk = "Перевал"
        caucasus.name_en = "Mountain Pass"
        caucasus.save()
    except Map.DoesNotExist:
        pass

    # 6) Фьорд -> Фьорды (slug=fjord)
    try:
        fjord = Map.objects.get(slug="fjord")
        fjord.name_ru = "Фьорды"
        fjord.name_uk = "Фіорди"
        fjord.name_en = "Fjords"
        fjord.save()
    except Map.DoesNotExist:
        pass

    # 7) Эль-Халлуф – базу не трогаем, картинку надо будет поменять руками
    # (static/maps/el_halluf.png заменить на правильную миникарту)


class Migration(migrations.Migration):

    dependencies = [
        ("picker", "0002_create_default_maps"),  # если у тебя номер другой – поставь последнюю миграцию picker
    ]

    operations = [
        migrations.RunPython(fix_maps, migrations.RunPython.noop),
    ]
