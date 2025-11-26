// picker/static/picker/map_tactics.js

// Формат:
//
// MAP_TACTICS = {
//   slug_карты: {
//     spawns: {
//       a: { spots: [...массив точек для респа 1...] },
//       b: { spots: [...массив точек для респа 2...] }
//     }
//   }
// }
//
// Точка:
// {
//   id: 1,
//   x: 30,   // в процентах
//   y: 70,   // в процентах
//   type: 'ht' | 'mt' | 'lt' | 'td' | 'spg',
//   text: { ru: '...', uk: '...', en: '...' }
// }

const MAP_TACTICS = {
  // ===== АЭРОДРОМ (airfield) =====
  airfield: {
    spawns: {
      // Респ 1 (условно "север")
      a: {
        spots: [
          {
            id: 1,
            x: 30,
            y: 70,
            type: 'ht',
            text: {
              ru: 'Направление НЕ бронированных танков, по типу Leopard 1 и другие (НО при возможности и соответствующем уровне игры нужно играть там же где и тяжелые танки)',
              uk: 'Напрямок НЕ броньованих танків, типу Leopard 1 та інші (АЛЕ при можливості та відповідному рівні гри потрібно грати там же, де і важкі танки)',
              en: 'The direction of non-armoured tanks, such as the Leopard 1 and others (BUT if possible and at the appropriate level of play, you should play in the same place as heavy tanks).'
            }
          },
          {
            id: 2,
            x: 48,
            y: 40,
            type: 'mt',
            text: {
              ru: 'Ключевые позиции для ТТ, бронированных СТ, и штурмовых ПТ-САУ.',
              uk: 'Ключові позиції для ВТ, броньованих СТ і штурмових ПТ-САУ.',
              en: 'Key positions for heavy tanks, armoured medium tanks and assault tank destroyers (T110e3 and others).'
            }
          },


        ]
      },

      // Респ 2 (условно "юг")
      b: {
        spots: [
          {
            id: 1,
            x: 70,
            y: 65,
            type: 'ht',
            text: {
              ru: 'Направление НЕ бронированных танков, по типу Leopard 1 и другие (НО при возможности и соответствующем уровне игры нужно играть там же где и тяжелые танки)',
              uk: 'Напрямок НЕ броньованих танків, типу Leopard 1 та інші (АЛЕ при можливості та відповідному рівні гри потрібно грати там же, де і важкі танки)',
              en: 'The direction of non-armoured tanks, such as the Leopard 1 and others (BUT if possible and at the appropriate level of play, you should play in the same place as heavy tanks).'
            }
          },
          {
            id: 2,
            x: 53,
            y: 41,
            type: 'mt',
            text: {
              ru: 'Ключевые позиции для ТТ, бронированных СТ, и штурмовых ПТ-САУ.',
              uk: 'Ключові позиції для ВТ, броньованих СТ і штурмових ПТ-САУ.',
              en: 'Key positions for heavy tanks, armoured medium tanks and assault tank destroyers (T110e3 and others).'
            }
          },
          {

          },
        ]
      }
    }
  },

  // ===== МАЛИНОВКА (malinovka) =====
  malinovka: {
    spawns: {
      // Респ 1 (холм сверху)
      a: {
        spots: [
          {
            id: 1,
            x: 98,
            y: 5,
            type: 'lt',
            text: {
              ru: 'Самая важная точка на карте, актуально для ВСЕХ классов техники, очень часто кто забирает эту точку, тот и выигрывает бой.',
              uk: 'Найважливіша точка на карті, актуальна для ВСІХ класів танків, дуже часто той, хто забирає цю точку, той і виграє бій.',
              en: 'The most important point on the map, relevant for ALL tank classes. Very often, whoever captures this point wins the battle.'
            }
          },
          {
            id: 2,
            x: 30,
            y: 70,
            type: 'ht',
            text: {
              ru: 'Классический куст для пассивного света респа противника.',
              uk: 'Класичний кущ для пасивного світа респа суперника.',
              en: 'Classic bush for passive light respawn of the enemy.'
            }
          },
          {
            id: 3,
            x: 65,
            y: 55,
            type: 'td',
            text: {
              ru: 'Позиции ПТ-САУ для прострела центральных направлений и подхода к горе.',
              uk: 'Позиції ПТ-САУ для прострілу центральних напрямків та підходу до гори.',
              en: 'TD spots to cover mid approaches and the hill climb.'
            }
          }
        ]
      },

      // Респ 2 (низина, церковь)
      b: {
        spots: [
          {
            id: 1,
            x: 25,
            y: 75,
            type: 'lt',
            text: {
              ru: 'Пассивный свет с этого респа. Позволяет засветить перекатку противника к центру и на горку.',
              uk: 'Пасивний світ з цього респа. Дозволяє підсвітити переїзд противника до центру та на гору.',
              en: 'Passive scout bush from this spawn to spot enemy crossings and hill'
            }
          },
          {
            id: 2,
            x: 40,
            y: 28,
            type: 'mt',
            text: {
              ru: 'Позиции ПТ-САУ для прострела центральных направлений.',
              uk: 'Позиції ПТ-САУ для прострілу центральних напрямків.',
              en: 'TD spots to cover mid approaches.'
            }
          },
          {
            id: 3,
            x: 98,
            y: 7,
            type: 'td',
            text: {
              ru: 'Самая важная точка на карте, актуально для ВСЕХ классов техники, очень часто кто забирает эту точку, тот и выигрывает бой.',
              uk: 'Найважливіша точка на карті, актуальна для ВСІХ класів танків, дуже часто той, хто забирає цю точку, той і виграє бій.',
              en: 'The most important point on the map, relevant for ALL tank classes. Very often, whoever captures this point wins the battle.'
            }
          }
        ]
      }
    }
  }

  // ===== ДАЛЬШЕ МОЖЕШЬ ДОБАВЛЯТЬ ВСЕ ОСТАЛЬНЫЕ КАРТЫ =====
  // Пример структуры:
  //
  // berlin: {
  //   spawns: {
  //     a: { spots: [ ... точки для респа 1 ... ] },
  //     b: { spots: [ ... точки для респа 2 ... ] }
  //   }
  // },
  //
  // lost_city: { ... },
  // mannerheim_line: { ... },
  // westfield: { ... },
  // и т.д.
};

// Цвета для типов техники
const TYPE_COLORS = {
  lt: '#22c55e',  // лёгкие танки
  mt: '#38bdf8',  // средние
  ht: '#f97316',  // тяжёлые
  td: '#a855f7',  // ПТ-САУ
  spg: '#facc15'  // САУ
};

function initMapTactics() {
  const root = document.querySelector('[data-map-interactive="1"]');
  if (!root) return;

  const slug = root.dataset.slug;
  const lang = root.dataset.lang || 'ru';
  const config = MAP_TACTICS[slug];

  if (!config || !config.spawns) {
    // Для этой карты пока нет данных — просто не показываем точки
    return;
  }

  const imageWrapper = root.querySelector('.map-detail-image-inner');
  const tooltip = root.querySelector('.map-tooltip');
  const tooltipText = root.querySelector('.map-tooltip-text');
  const spawnButtons = root.querySelectorAll('[data-spawn-switch]');

  if (!imageWrapper || !tooltip || !tooltipText) return;

  const availableSpawns = Object.keys(config.spawns);
  if (!availableSpawns.length) return;

  // Скрываем лишние кнопки, если данных только для одного респа
  spawnButtons.forEach(btn => {
    const s = btn.getAttribute('data-spawn-switch');
    if (!config.spawns[s]) {
      btn.style.display = 'none';
    }
  });

  let currentSpawn = availableSpawns.includes('a') ? 'a' : availableSpawns[0];

  function setDefaultTooltipText() {
    if (lang === 'uk') {
      tooltipText.textContent = 'Наведи або натисни на маркер, щоб побачити опис позиції.';
    } else if (lang === 'en') {
      tooltipText.textContent = 'Hover or tap a marker to see position description.';
    } else {
      tooltipText.textContent = 'Наведи або натисни на маркер, чтобы увидеть описание позиции.';
    }
  }

  function clearSpots() {
    imageWrapper.querySelectorAll('.map-spot').forEach(el => el.remove());
  }

  function renderSpots() {
    clearSpots();

    const spawnCfg = config.spawns[currentSpawn];
    if (!spawnCfg || !spawnCfg.spots) return;

    spawnCfg.spots.forEach((spot) => {
      const dot = document.createElement('button');
      dot.type = 'button';
      dot.className = 'map-spot';
      dot.style.left = spot.x + '%';
      dot.style.top = spot.y + '%';

      const color = TYPE_COLORS[spot.type] || '#e5e7eb';
      dot.style.setProperty('--spot-color', color);

      dot.innerHTML = `<span class="map-spot-label">${spot.id}</span>`;

      const showTooltip = () => {
        tooltipText.textContent = spot.text[lang] || spot.text.ru;
        tooltip.style.opacity = '1';
        tooltip.style.transform = 'translateY(0)';
      };

      dot.addEventListener('mouseenter', showTooltip);
      dot.addEventListener('click', showTooltip); // для мобилок

      imageWrapper.appendChild(dot);
    });
  }

  function setActiveSpawn(newSpawn) {
    if (!config.spawns[newSpawn]) return;
    currentSpawn = newSpawn;

    spawnButtons.forEach(btn => {
      const s = btn.getAttribute('data-spawn-switch');
      btn.classList.toggle('is-active', s === currentSpawn);
    });

    setDefaultTooltipText();
    renderSpots();
  }

  // Навешиваем обработчики на кнопки респов
  spawnButtons.forEach(btn => {
    const s = btn.getAttribute('data-spawn-switch');
    btn.addEventListener('click', () => setActiveSpawn(s));
  });

  // Инициализация
  setDefaultTooltipText();
  setActiveSpawn(currentSpawn);
}

document.addEventListener('DOMContentLoaded', initMapTactics);
