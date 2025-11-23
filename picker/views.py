from django.shortcuts import render
from pathlib import Path
import json

# ===== ЯЗЫКИ =====

LANGS = ["uk", "ru", "en"]
DEFAULT_LANG = "uk"

UI_TEXT = {
    "en": {
        "title": "WoT Build Picker",
        "subtitle": "Pick a tank and get a ready build: equipment, consumables, crew skills and how to play.",
        "label_tank": "Tank",
        "label_lang": "Language",
        "label_nation": "Nation",
        "label_class": "Class",
        "label_tier": "Tier",
        "button_show": "Show build",
        "footer": "Early prototype. Next: more custom builds.",
        "role_label": "Role",
        "equipment": "Equipment",
        "consumables": "Consumables",
        "crew_skills": "Crew skills (order)",
        "how_to_play": "How to play",
        "support": "Support the author with a coffee:",
        "ability_label": "Special ability",
    },
    "ru": {
        "title": "WoT Build Picker",
        "subtitle": "Выбери танк и получи готовую сборку: оборудование, расходники, перки и стиль игры.",
        "label_tank": "Танк",
        "label_lang": "Язык",
        "label_nation": "Нация",
        "label_class": "Класс",
        "label_tier": "Уровень",
        "button_show": "Показать сборку",
        "footer": "Ранний прототип. Дальше — больше кастомных билдов.",
        "role_label": "Роль",
        "equipment": "Оборудование",
        "consumables": "Расходники",
        "crew_skills": "Перки экипажа (порядок прокачки)",
        "how_to_play": "Как играть",
        "support": "Поддержать автора чашкой кофе:",
        "ability_label": "Особое умение",
    },
    "uk": {
        "title": "WoT Build Picker",
        "subtitle": "Обери танк і отримаєш готову збірку: обладнання, спорядження, вміння екіпажу та стиль гри.",
        "label_tank": "Танк",
        "label_lang": "Мова",
        "label_nation": "Нація",
        "label_class": "Клас",
        "label_tier": "Рівень",
        "button_show": "Показати збірку",
        "footer": "Ранній прототип. Далі — більше кастомних збірок.",
        "role_label": "Роль",
        "equipment": "Обладнання",
        "consumables": "Спорядження",
        "crew_skills": "Вміння екіпажу (порядок прокачки)",
        "how_to_play": "Як грати",
        "support": "Підтримати автора чашкою кави:",
        "ability_label": "Особлива здатність",
    },
}

# ===== НАЦИИ (с флагами) =====

NATIONS = {
    "all": {
        "labels": {
            "en": "All nations",
            "ru": "Все нации",
            "uk": "Усі нації",
        },
        "flag": None,
    },
    "ussr": {
        "labels": {
            "en": "U.S.S.R.",
            "ru": "СССР",
            "uk": "СРСР",
        },
        "flag": "picker/flags/ussr.png",
    },
    "germany": {
        "labels": {
            "en": "Germany",
            "ru": "Германия",
            "uk": "Німеччина",
        },
        "flag": "picker/flags/germany.png",
    },
    "usa": {
        "labels": {
            "en": "U.S.A.",
            "ru": "США",
            "uk": "США",
        },
        "flag": "picker/flags/usa.png",
    },
    "france": {
        "labels": {
            "en": "France",
            "ru": "Франция",
            "uk": "Франція",
        },
        "flag": "picker/flags/france.png",
    },
    "uk": {
        "labels": {
            "en": "U.K.",
            "ru": "Великобритания",
            "uk": "Велика Британія",
        },
        "flag": "picker/flags/uk.png",
    },
    "china": {
        "labels": {
            "en": "China",
            "ru": "Китай",
            "uk": "Китай",
        },
        "flag": "picker/flags/china.png",
    },
    "japan": {
        "labels": {
            "en": "Japan",
            "ru": "Япония",
            "uk": "Японія",
        },
        "flag": "picker/flags/japan.png",
    },
    "czech": {
        "labels": {
            "en": "Czechoslovakia",
            "ru": "Чехословакия",
            "uk": "Чехословаччина",
        },
        "flag": "picker/flags/czech.png",
    },
    "italy": {
        "labels": {
            "en": "Italy",
            "ru": "Италия",
            "uk": "Італія",
        },
        "flag": "picker/flags/italy.png",
    },
    "sweden": {
        "labels": {
            "en": "Sweden",
            "ru": "Швеция",
            "uk": "Швеція",
        },
        "flag": "picker/flags/sweden.png",
    },
    "poland": {
        "labels": {
            "en": "Poland",
            "ru": "Польша",
            "uk": "Польща",
        },
        "flag": "picker/flags/poland.png",
    },
}

# ===== КЛАССЫ =====

CLASSES = {
    "all": {
        "labels": {
            "en": "All classes",
            "ru": "Все классы",
            "uk": "Усі класи",
        }
    },
    "HT": {
        "labels": {
            "en": "Heavy tank",
            "ru": "Тяжёлый танк",
            "uk": "Важкий танк",
        }
    },
    "MT": {
        "labels": {
            "en": "Medium tank",
            "ru": "Средний танк",
            "uk": "Середній танк",
        }
    },
    "LT": {
        "labels": {
            "en": "Light tank",
            "ru": "Лёгкий танк",
            "uk": "Легкий танк",
        }
    },
    "TD": {
        "labels": {
            "en": "Tank destroyer",
            "ru": "ПТ-САУ",
            "uk": "ПТ-САУ",
        }
    },
}

# ===== ПЕРКИ =====

SKILL_NAMES = {
    "repair": {
        "en": "Repair",
        "ru": "Ремонт",
        "uk": "Ремонт",
    },
    "firefighting": {
        "en": "Firefighting",
        "ru": "Пожаротушение",
        "uk": "Пожежогасіння",
    },
    "eagle_eye": {
        "en": "Situational Awareness",
        "ru": "Орлиный глаз",
        "uk": "Орлине око",
    },
    "bia": {
        "en": "Brothers in Arms",
        "ru": "Боевое братство",
        "uk": "Бойове братство",
    },
    "smooth_ride": {
        "en": "Smooth Ride / driver",
        "ru": "Плавный ход (мехвод / аналог)",
        "uk": "Плавний хід (мехвод / аналог)",
    },
    "safe_stowage": {
        "en": "Safe Stowage / ammo rack",
        "ru": "Бесконтактная боеукладка",
        "uk": "Безконтактна боеукладка",
    },
    "camouflage": {
        "en": "Camouflage",
        "ru": "Маскировка",
        "uk": "Маскування",
    },
    "sound_detection": {
        "en": "Sound Detection",
        "ru": "Звуковая разведка",
        "uk": "Звукова розвідка",
    },
}


def generate_crew_skills(lang: str, nation: str, tank_class: str):
    """
    Логика перков:
      • 1-й: Ремонт
      • у ЛТ: после ремонта Орлиный глаз
      • у СССР: после ремонта Пожаротушение
      • 3-й: Боевое братство
      • дальше: Плавный ход → Бесконтактная б/к → Маскировка
      • у всех тяжёлых: добавляем Звуковую разведку
    """
    codes = []

    codes.append("repair")

    if tank_class == "LT":
        codes.append("eagle_eye")
    elif nation == "ussr":
        codes.append("firefighting")

    codes.append("bia")
    codes.extend(["smooth_ride", "safe_stowage", "camouflage"])

    if tank_class == "HT":
        codes.append("sound_detection")

    result = []
    for i, code in enumerate(codes, start=1):
        name = SKILL_NAMES.get(code, {}).get(lang) or SKILL_NAMES.get(code, {}).get("en") or code
        result.append(f"{i}. {name}")
    return result


# ===== ЗАГРУЗКА JSON =====

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data"
TANKS_FILE = DATA_PATH / "tanks_eu.json"
BUILDS_CONFIG_FILE = DATA_PATH / "builds_config.json"

try:
    with open(TANKS_FILE, "r", encoding="utf-8") as f:
        TANK_SPECS = json.load(f)
except FileNotFoundError:
    TANK_SPECS = []

try:
    with open(BUILDS_CONFIG_FILE, "r", encoding="utf-8") as f:
        BUILDS_CONFIG = json.load(f)
except FileNotFoundError:
    BUILDS_CONFIG = {
        "default_by_class": {},
        "build_templates": {},
        "overrides_by_id": {},
    }

DEFAULT_BY_CLASS = BUILDS_CONFIG.get("default_by_class", {})
BUILD_TEMPLATES = BUILDS_CONFIG.get("build_templates", {})
OVERRIDES_BY_ID = BUILDS_CONFIG.get("overrides_by_id", {})

# ===== ОСОБЫЕ УМЕНИЯ 11 УРОВНЯ (мультиязычно) =====

ABILITY_TEXT = {
    "Taschenratte": {
        "ru": "Вспомогательные орудия (Нажимая клавишу активации, вы можете стрелять по цели из вспомогательного орудия. У него собственный цикл перезарядки, не зависящий от основного орудия).",
        "uk": "Допоміжні гармати (Натискаючи клавішу активації, ви можете стріляти по цілі з допоміжної гармати. Вона має власний цикл перезаряджання, незалежний від основного знаряддя).",
        "en": "Auxiliary guns (Press the ability key to fire at a target with the auxiliary gun. It has its own reload cycle independent from the main gun).",
    },
    "КР-1": {
        "ru": "Таранная компоновка (Основанная на опыте ранних моделей, эта машина скомпонована специально для мощных атак за счёт корпуса. Усиленная конструкция позволяет ей наносить больше урона тараном технике противника, что даёт преимущество в бою на ближней дистанции).",
        "uk": "Таранна компоновка (На основі досвіду попередніх машин цей танк спеціально спроєктований для потужних ударів корпусом. Посилена конструкція дає змогу завдавати більше шкоди тараном і мати перевагу в ближньому бою).",
        "en": "Ramming layout (Based on earlier designs, this vehicle is built for powerful ramming attacks. The reinforced hull lets it deal more ramming damage, giving an advantage in close combat).",
    },
    "KR-1": {  # дубль для латиницы
        "ru": "Таранная компоновка (Основанная на опыте ранних моделей, эта машина скомпонована специально для мощных атак за счёт корпуса. Усиленная конструкция позволяет ей наносить больше урона тараном технике противника, что даёт преимущество в бою на ближней дистанции).",
        "uk": "Таранна компоновка (На основі досвіду попередніх машин цей танк спеціально спроєктований для потужних ударів корпусом. Посилена конструкція дає змогу завдавати більше шкоди тараном і мати перевагу в ближньому бою).",
        "en": "Ramming layout (Based on earlier designs, this vehicle is built for powerful ramming attacks. The reinforced hull lets it deal more ramming damage, giving an advantage in close combat).",
    },
    "T803": {
        "ru": "Полуавтоматическая боеукладка (При каждом попадании по противнику вы получаете уровень эффективности перезарядки, временно ускоряющий перезарядку вашего орудия. Уровни набираются с каждым попаданием, а при уничтожении машины противника вы получите дополнительные уровни).",
        "uk": "Напівавтоматична боеукладка (За кожне влучання ви отримуєте рівень ефективності перезаряджання, який тимчасово пришвидшує перезарядку гармати. Рівні накопичуються, а за знищення машини противника даються додаткові рівні).",
        "en": "Semi-automatic ammo rack (Each hit on an enemy gives a reload efficiency level that temporarily speeds up your reload. Levels stack with every hit, and destroying an enemy grants extra levels).",
    },
    "AMX 67 Imbattable": {
        "ru": "Кассетная система заряжания (Система автоматически начинает заряжать новую кассету, когда в текущей остаётся один снаряд, что позволяет всегда быть готовым к атаке. Вы можете использовать последний снаряд, но это добавит несколько секунд к оставшемуся времени перезарядки).",
        "uk": "Касетна система заряджання (Система автоматично починає заряджати нову касету, коли в поточній лишається один снаряд, що дозволяє завжди бути готовим до атаки. Ви можете вистрілити останнім снарядом, але це збільшить час перезаряджання).",
        "en": "Cassette loading system (The system automatically starts loading a new cassette when only one shell remains, so you are always ready to attack. You can fire the last shell, but this will add a few seconds to the reload time).",
    },
    "FV4025 Contriver": {
        "ru": "Залповый режим (Позволяет нанести двойной урон, а также улучшает стабилизацию за счёт ухудшения показателей мобильности, разброса, скорости вращения башни и времени сведения. Лучше всего использовать в ближнем бою).",
        "uk": "Залповий режим (Дозволяє завдати подвоєної шкоди та покращує стабілізацію, але погіршує мобільність, розкид, швидкість повороту башти й час зведення. Найкраще підходить для бою на близькій дистанції).",
        "en": "Salvo mode (Lets you deal double damage and improves stabilization at the cost of mobility, dispersion, turret traverse speed and aiming time. Most effective in close-range fights).",
    },
    "BZ-79": {
        "ru": "Жидкотопливный ускоритель (Активируйте жидкотопливный ускоритель в любое время, чтобы получить бонус к скорости, когда это нужно больше всего. Ускорители нагреваются и им нужно остывать перед повторным использованием. В противном случае они перегреются и временно отключатся).",
        "uk": "Рідкопаливний прискорювач (Активуйте прискорювач у потрібний момент, щоб отримати бонус до швидкості. Після використання він нагрівається і має охолонути перед повторним запуском, інакше може перегрітися та тимчасово вимкнутися).",
        "en": "Liquid-fuel booster (Activate it when you need extra speed. The boosters heat up and must cool down before reuse; otherwise they overheat and shut down for a while).",
    },
    "Black Rock": {
        "ru": "Режим очереди (После двух попаданий с пробитием техники противника активируется режим очереди. Будет заряжена кассета, позволяющая совершить два быстрых выстрела подряд и нанести больше урона).",
        "uk": "Режим черги (Після двох влучань із пробиттям по техніці противника активується режим черги. Заряджається касета, що дозволяє зробити два швидкі постріли поспіль і завдати більше шкоди).",
        "en": "Burst queue mode (After two penetrating hits, a special queue mode activates. A cassette is loaded that lets you fire two quick shots in a row to deal extra damage).",
    },
    "Объект 432У": {
        "ru": "Термобаллистическая перегрузка (При заряженном орудии вы можете начать нагревать ваш следующий снаряд. Чем выше уровень нагрева, тем больше будет бонус к разовому урону).",
        "uk": "Термобалістичне перевантаження (Коли гармата заряджена, ви можете почати нагрівати наступний снаряд. Чим вищий рівень нагріву, тим більший бонус до разового урону).",
        "en": "Thermoballistic overload (With a loaded gun you can start heating the next shell. The higher the heat level, the bigger the bonus to single-shot damage).",
    },
    "Object 432U": {  # дубль для латиницы
        "ru": "Термобаллистическая перегрузка (При заряженном орудии вы можете начать нагревать ваш следующий снаряд. Чем выше уровень нагрева, тем больше будет бонус к разовому урону).",
        "uk": "Термобалістичне перевантаження (Коли гармата заряджена, ви можете почати нагрівати наступний снаряд. Чим вищий рівень нагріву, тим більший бонус до разового урону).",
        "en": "Thermoballistic overload (With a loaded gun you can start heating the next shell. The higher the heat level, the bigger the bonus to single-shot damage).",
    },
    "Leopard 120 Verbessert": {
        "ru": "Аналоговый баллистический вычислитель (Оставаясь неподвижным или двигаясь медленно, вы накапливаете уровни точности, повышающие точность следующего выстрела. На максимальном уровне достигаются почти идеальные характеристики орудия с минимальным разбросом даже при движении или повороте корпуса/башни).",
        "uk": "Аналоговий балістичний обчислювач (Якщо стояти на місці або рухатися повільно, накопичуються рівні точності, що підвищують точність наступного пострілу. На максимальному рівні гармата стає майже ідеально точною навіть у русі чи при повороті корпусу/башти).",
        "en": "Analog ballistic computer (Staying still or moving slowly builds accuracy levels that improve your next shot. At maximum level the gun becomes almost perfectly accurate even while moving or turning the hull/turret).",
    },
    "CS-67 Szakal": {
        "ru": "Тактическая силовая установка (В зависимости от активного режима и уровня заряда машина может применить одну из двух способностей: Ионно-разрядный дожигатель — увеличивает мощность двигателя и максимальную скорость; Параллаксный электромеханический прицел — уменьшает разброс и время перезарядки).",
        "uk": "Тактична силова установка (Залежно від активного режиму та рівня заряду машина використовує одну з двох здібностей: іонно-розрядний дожигатель збільшує потужність двигуна й максимальну швидкість; паралаксний електромеханічний приціл зменшує розкид і час перезаряджання).",
        "en": "Tactical power unit (Depending on the active mode and charge level the tank uses one of two abilities: the ion-discharge booster increases engine power and top speed; the parallax electromechanical sight reduces dispersion and reload time).",
    },
    "AS-XX 40t": {
        "ru": "Модуль внешней подачи боеприпасов (Этот модуль помогает вам продолжать бой, позволяя прервать перезарядку в любое время, если у вас заряжен хотя бы один снаряд. Нажмите назначенную клавишу, чтобы прервать перезарядку, выстрелите после небольшой задержки и продолжите перезарядку вручную или позвольте ей начаться автоматически, когда снаряды закончатся).",
        "uk": "Модуль зовнішньої подачі боєприпасів (Дає змогу перервати перезаряджання в будь-який момент, якщо заряджений хоча б один снаряд. Натисніть призначену клавішу, щоб зупинити перезарядку, зробіть постріл після невеликої затримки та продовжте перезаряджання вручну або дозвольте йому початися автоматично, коли снаряди закінчаться).",
        "en": "External ammo feed module (Lets you interrupt reloading at any time if at least one shell is loaded. Press the assigned key to stop the reload, fire after a short delay, then continue reloading manually or automatically when the clip is empty).",
    },
    "XM69 Hacker": {
        "ru": "Пневматический гиростабилизатор (Пневматический гиростабилизатор обеспечивает максимальную стабилизацию в движении, при повороте корпуса и башни, что позволяет стрелять точнее, а также быстрее отвечать на внезапные угрозы и эффективнее использовать укрытия).",
        "uk": "Пневматичний гіростабілізатор (Забезпечує максимальну стабілізацію в русі та при повороті корпусу й башти, що дозволяє точніше стріляти, швидше реагувати на раптові загрози та ефективніше використовувати укриття).",
        "en": "Pneumatic gyrostabilizer (Provides very strong stabilization when moving and turning the hull or turret, letting you fire more accurately, react faster to sudden threats and use cover more effectively).",
    },
    "Hirschkäfer": {
        "ru": "Система термоконтроля боезаряда (Стойте неподвижно или двигайтесь медленно, чтобы преднагрев увеличил урон и уменьшил разброс для вашего следующего выстрела. При максимальном уровне преднагрева пробитие брони противника, у которого меньше прочности, чем ваш средний урон, вызовет фатальный взрыв боекомплекта).",
        "uk": "Система термоконтролю боєзаряду (Стоячи на місці або рухаючись повільно, ви нагріваєте боєзаряд, що збільшує шкоду й зменшує розкид для наступного пострілу. На максимальному рівні нагріву пробиття цілі з низькою кількістю міцності може спричинити детонацію боєкомплекту).",
        "en": "Ammo thermal-control system (Standing still or moving slowly preheats the charge, increasing damage and reducing dispersion for your next shot. At maximum heat, penetrating a low-HP target can cause an ammo rack explosion).",
    },
    "Strv 107-12": {
        "ru": "Укреплённый режим (В этом режиме ваша машина превращается в укреплённую орудийную платформу с уменьшенным разбросом и ускоренной перезарядкой. Однако за повышенную огневую мощь приходится платить существенным снижением динамики и скорости поворота).",
        "uk": "Укріплений режим (У цьому режимі машина перетворюється на укріплену вогневу платформу з меншим розкидом і швидшою перезарядкою, але з помітно гіршою динамікою та повороткістю).",
        "en": "Fortified mode (The vehicle becomes a fortified gun platform with lower dispersion and faster reload, but its mobility and traverse speed are heavily reduced).",
    },
    "AT-FV230 Breaker": {
        "ru": "Прямая передача (В этом режиме существенно возрастают мощность двигателя и скорость. Чем дольше вы двигаетесь вперёд, тем лучше ускорение. Это позволяет вам быстро преодолевать большие расстояния).",
        "uk": "Прямий привід (У цьому режимі значно зростає потужність двигуна й швидкість. Чим довше ви рухаєтесь уперед, тим краще прискорення. Це дає змогу швидко долати великі відстані).",
        "en": "Direct drive (This mode greatly increases engine power and speed. The longer you drive forward, the better the acceleration, allowing you to cover large distances quickly).",
    },
    "leKpz Borkenkäfer": {
        "ru": "Лазерный целеуказатель (При вашем следующем выстреле будет применён эффект, зависящий от того, обнаружен ли противник. Попадание по обнаруженной машине отметит её — она будет дольше оставаться видимой, а также получать больше урона. Попадание по необнаруженной машине обозначит её местоположение особой отметкой).",
        "uk": "Лазерний цілевказівник (На наступний постріл накладається ефект, що залежить від того, чи була техніка виявлена. Влучання по виявленій машині позначає її — вона довше лишається видимою та отримує більше шкоди. Влучання по невиявленій машині позначає її місцеперебування спеціальною міткою).",
        "en": "Laser designator (Your next shot applies an effect depending on whether the target was spotted. Hitting a spotted vehicle marks it so it stays visible longer and takes more damage; hitting an unspotted target marks its position with a special indicator).",
    },
}

def _normalize_name(s: str) -> str:
    return "".join(ch.lower() for ch in s if ch.isalnum())

ABILITY_TEXT_NORM = {
    _normalize_name(key): val for key, val in ABILITY_TEXT.items()
}

# ===== ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ =====

def get_lang(request):
    lang = request.GET.get("lang") or request.POST.get("lang")
    if lang not in LANGS:
        lang = DEFAULT_LANG
    return lang


def get_role_code_for_tank(spec):
    """
    Определяем код роли:
      1) overrides_by_id из JSON
      2) особые правила (итальянские ПТ, немецкие штурмовые ПТ, барабанные французы, Somua SM, 11 уровень и т.д.)
      3) дефолт по классу
    """
    tank_class = spec.get("class")
    nation = spec.get("nation")
    default_role = DEFAULT_BY_CLASS.get(tank_class)

    names = spec.get("names", {}) or {}
    name_en = names.get("en") or next(iter(names.values()), None)

    # 1) явные overrides из JSON
    if name_en and name_en in OVERRIDES_BY_ID:
        return OVERRIDES_BY_ID[name_en]

    # 2) особые правила

    # Все итальянские ПТ-САУ = штурмовые ПТ
    if tank_class == "TD" and nation == "italy":
        return "td_assault"

    # Немецкие штурмовые ПТ-САУ по списку
    german_assault_td = {
        "Jagdpanzer E 100",
        "Jagdtiger",
        "Jagdtiger FL",
        "8,8 cm Pak 43 Jagdtiger",
        "Ferdinand",
        "Ferdinand FL",
        "Jagdpanther II",
        "Jagdtiger Prototype",
        "Jagdpanther",
        "Jagdpanzer IV",
    }
    if tank_class == "TD" and nation == "germany" and name_en in german_assault_td:
        return "td_assault"

    # Французские барабанные СТ (логика как у барабанных ТТ, но активнее используют скорость)
    french_autoloader_mts = {
        "Miel",
        "Lorraine 40 t",
        "Bat.-Châtillon Bourrasque",
        "Char Murat",
        "Char Futur 4",
        "Bat.-Châtillon 25 t AP",
        "Bat.-Châtillon 25 t",
    }
    if tank_class == "MT" and nation == "france" and name_en in french_autoloader_mts:
        # используем штурмовой СТ — агрессивная игра, акцент на скорости
        return "mt_assault"

    # Somua SM — барабанный тяж поддержки
    if name_en == "Somua SM":
        return "heavy_autoloader_support"

    # AT-FV230 Breaker — штурмовая ПТ-САУ
    if name_en == "AT-FV230 Breaker":
        return "td_assault"

    # AMX 67 Imbattable — барабанный тяж поддержки
    if name_en == "AMX 67 Imbattable":
        return "heavy_autoloader_support"

    # AS-XX 40 t — барабанный штурмовой СТ
    if name_en == "AS-XX 40t" or name_en == "AS-XX 40 t":
        return "mt_assault"

    # CS-67 Szakal — быстрый СТ (универсальный по роли, скорость в описании билда)
    if name_en == "CS-67 Szakal":
        return "mt_universal"

    # 3) дефолт по классу
    return default_role


def get_build_for_tank(spec, lang):
    """
    Возвращает:
    - build: словарь с equipment / consumables / crew_skills / notes
    - role_title: название роли (локализованное)
    """
    role_code = get_role_code_for_tank(spec)
    if not role_code:
        return None, None

    template = BUILD_TEMPLATES.get(role_code)
    if not template:
        return None, None

    role_title = template["role"].get(lang) or template["role"].get("en")

    equipment = template["equipment"].get(lang) or template["equipment"].get("en") or []
    consumables = template["consumables"].get(lang) or template["consumables"].get("en") or []
    notes = template["notes"].get(lang) or template["notes"].get("en") or ""

    crew_skills = generate_crew_skills(
        lang=lang,
        nation=spec.get("nation", ""),
        tank_class=spec.get("class", ""),
    )

    build = {
        "equipment": equipment,
        "consumables": consumables,
        "crew_skills": crew_skills,
        "notes": notes,
    }
    return build, role_title


# ===== VIEW =====

def index(request):
    lang = get_lang(request)
    ui = UI_TEXT[lang]

    selected_nation = request.GET.get("nation") or request.POST.get("nation") or "all"
    selected_class = request.GET.get("tank_class") or request.POST.get("tank_class") or "all"
    selected_tier = request.GET.get("tier") or request.POST.get("tier") or "all"
    selected_tank_id = request.GET.get("tank_id") or request.POST.get("tank_id")

    # --- список всех танков (уровни 6–10 и 11) ---
    tanks_all = []
    for spec in TANK_SPECS:
        tier = spec.get("tier")
        if tier is None or tier < 6:
            continue

        tank_id = spec.get("id")
        nation = spec.get("nation")
        tank_class = spec.get("class")

        names = spec.get("names", {}) or {}
        name_local = names.get(lang) or names.get("en") or next(iter(names.values()), "")

        _, role_title = get_build_for_tank(spec, lang)

        tanks_all.append({
            "id": tank_id,
            "nation": nation,
            "tank_class": tank_class,
            "tier": tier,
            "name": name_local,
            "role": role_title or "",
            "image_path": spec.get("image_path"),
            "spec": spec,
        })

    tiers_available = sorted({t["tier"] for t in tanks_all})

    # --- фильтрация ---
    tanks_filtered = []
    for t in tanks_all:
        if selected_nation != "all" and t["nation"] != selected_nation:
            continue
        if selected_class != "all" and t["tank_class"] != selected_class:
            continue
        if selected_tier != "all" and str(t["tier"]) != str(selected_tier):
            continue
        tanks_filtered.append(t)

    tanks_filtered.sort(key=lambda x: (x["tier"], x["nation"], x["name"]))

    # --- выбранный танк ---
    selected_tank = None
    build = None

    if selected_tank_id:
        for t in tanks_all:
            if str(t["id"]) == str(selected_tank_id):
                selected_tank = t
                break

    if selected_tank:
        build, role_title = get_build_for_tank(selected_tank["spec"], lang)
        if role_title:
            selected_tank["role"] = role_title

        names = selected_tank["spec"].get("names", {}) or {}

        ability_data = None

        # 1) пробуем точное совпадение по ru/en/uk
        for code in ("ru", "en", "uk"):
            nm = names.get(code)
            if nm and nm in ABILITY_TEXT:
                ability_data = ABILITY_TEXT[nm]
                break

        # 2) если не нашли — пробуем по нормализованному имени (любого языка)
        if not ability_data:
            for nm in names.values():
                if not nm:
                    continue
                key_norm = _normalize_name(nm)
                if key_norm in ABILITY_TEXT_NORM:
                    ability_data = ABILITY_TEXT_NORM[key_norm]
                    break

        if ability_data:
            selected_tank["ability_text"] = (
                ability_data.get(lang)
                or ability_data.get("ru")
                or ability_data.get("en")
            )
    else:
        selected_tank = None

    # --- список наций для селекта ---
    nation_list = []
    nation_list.append({
        "code": "all",
        "label": NATIONS["all"]["labels"][lang],
        "flag": None,
    })
    for code, data in NATIONS.items():
        if code == "all":
            continue
        nation_list.append({
            "code": code,
            "label": data["labels"][lang],
            "flag": data["flag"],
        })

    # --- список классов ---
    class_list = [
        {"code": "all", "label": CLASSES["all"]["labels"][lang]},
        {"code": "HT", "label": CLASSES["HT"]["labels"][lang]},
        {"code": "MT", "label": CLASSES["MT"]["labels"][lang]},
        {"code": "LT", "label": CLASSES["LT"]["labels"][lang]},
        {"code": "TD", "label": CLASSES["TD"]["labels"][lang]},
    ]

    context = {
        "ui": ui,
        "lang": lang,
        "langs": LANGS,
        "nation_list": nation_list,
        "class_list": class_list,
        "tiers": tiers_available,
        "selected_nation": selected_nation,
        "selected_class": selected_class,
        "selected_tier": selected_tier,
        "tanks": tanks_filtered,
        "selected_tank_id": selected_tank_id,
        "selected_tank": selected_tank,
        "build": build,
    }

    return render(request, "picker/index.html", context)
