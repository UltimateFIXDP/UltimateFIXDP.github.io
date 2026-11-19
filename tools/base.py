#!/usr/bin/env python3
# Builds the UltimateFIXDP site (index.html, i18n.js) from one table of texts in both languages.
import json, sys, html, os

OUT = sys.argv[1]
SITE = 'https://littlebitua.github.io/UltimateFIXDP/'
REPO = 'https://github.com/LittleBitUA/UltimateFIXDP'

T = {}  # key -> (en, uk); values may contain HTML
def t(key, en, uk): T[key] = (en, uk); return key

ICON = {
 'shield': '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/>',
 'bolt': '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
 'eye': '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
 'puzzle': '<path d="M9 3h6v3a2 2 0 1 0 4 0V3h2v6h-3a2 2 0 1 0 0 4h3v8h-6v-3a2 2 0 1 0-4 0v3H3v-6h3a2 2 0 1 0 0-4H3V3z"/>',
 'pad': '<rect x="2" y="7" width="20" height="10" rx="5"/><path d="M7 10v4M5 12h4M15 11h.01M18 13h.01"/>',
 'map': '<path d="M9 4L3 6v14l6-2 6 2 6-2V4l-6 2z"/><path d="M9 4v14M15 6v14"/>',
 'book': '<path d="M4 4h7a3 3 0 0 1 3 3v13a2 2 0 0 0-2-2H4z"/><path d="M20 4h-4a3 3 0 0 0-3 3"/>',
 'camera': '<rect x="3" y="7" width="18" height="13" rx="2"/><circle cx="12" cy="13.5" r="3.5"/><path d="M8 7l1.5-3h5L16 7"/>',
 'save': '<path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z"/><path d="M17 21v-8H7v8M7 3v5h8"/>',
 'globe': '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
 'tv': '<rect x="3" y="5" width="18" height="12" rx="2"/><path d="M8 21h8M12 17v4"/>',
 'gauge': '<path d="M4 18a8 8 0 1 1 16 0"/><path d="M12 18l4-6"/>',
}
def icon(name):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" '
            'stroke-linejoin="round">' + ICON[name] + '</svg>')

FEATURES = [
 ('shield', t('f.stab.t', 'Stability', 'Стабільність'),
  t('f.stab.d', 'The crash after cutscenes, the zero-frame freeze, the Alt+Tab hang and the endless hang on a broken angle are fixed. A crash handler and a freeze watchdog write a dump if anything still goes wrong.',
    'Виправлено виліт після катсцен, зависання на нульовому кадрі, після Alt+Tab і вічне зависання на «зламаному» куті. Обробник вильотів і сторож зависань пишуть дамп, якщо щось усе ж трапиться.')),
 ('bolt', t('f.fps.t', '45 → 180 FPS', '45 → 180 FPS'),
  t('f.fps.d', 'On some PCs the game sat at ~45 FPS with an idle GPU. Fixed. Physics, the car, doors, animations and every timer of the game run right at 120–180 FPS.',
    'На деяких ПК гра трималась на ~45 FPS при вільній відеокарті. Виправлено. Фізика, машина, двері, анімації й усі таймери гри йдуть правильно на 120–180 FPS.')),
 ('eye', t('f.gfx.t', 'Graphics', 'Графіка'),
  t('f.gfx.d', 'Your monitor\'s resolution, supersampling up to 3×, HBAO, SMAA, sharpening, wet reflections, 16× anisotropy, sharper shadows, longer draw distance, and <strong>no more flickering far textures</strong>.',
    'Роздільність монітора, суперсемплінг до 3×, HBAO, SMAA, різкість, мокрі відбиття, анізотропія 16×, чіткіші тіні, більша дальність і <strong>далекі текстури більше не блимають</strong>.')),
 ('tv', t('f.x360.t', 'Xbox 360 look', 'Вигляд Xbox 360'),
  t('f.x360.d', 'The console\'s colour grading and TV gamma, compared with our own Xbox 360 recompilation, on top of the PC picture.',
    'Кольорокорекція й гамма телевізора консолі, звірені з нашою рекомпіляцією версії для Xbox 360, поверх картинки PC.')),
 ('puzzle', t('f.mods.t', 'Mod manager', 'Менеджер модів'),
  t('f.mods.d', 'Drop a folder into <code>UltimateFix\\mods\\</code>: a translation from the SWERY Localization Tool, a texture pack, or any game file by its name (<code>fontwide.xpc</code>, <code>mes_all.mes</code>). Order and on/off in F10.',
    'Покладіть теку в <code>UltimateFix\\mods\\</code>: переклад із SWERY Localization Tool, текстурний пак або будь-який файл гри за іменем (<code>fontwide.xpc</code>, <code>mes_all.mes</code>). Порядок і вмикання в F10.')),
 ('pad', t('f.pad.t', 'DualSense and Xbox pads', 'DualSense і Xbox-пади'),
  t('f.pad.d', 'USB and Bluetooth without Steam Input, adaptive triggers per weapon, rumble that the PC port never sent, aim on L2 and fire on R2, the Xbox 360 quick turn, button icons that follow the device.',
    'USB і Bluetooth без Steam Input, адаптивні триґери під кожну зброю, вібрація, яку PC-порт ніколи не надсилав, приціл на L2 і постріл на R2, швидкий розворот Xbox 360, іконки під пристрій.')),
 ('map', t('f.map.t', 'Map and waypoints', 'Мапа й мітки'),
  t('f.map.d', 'The full pause map with all 64 tiles, north up. F7 sets a waypoint that becomes the game\'s own objective, with its beacon and minimap arrows.',
    'Повна мапа паузи з усіма 64 плитками, північ угорі. F7 ставить мітку, яка стає рідною ціллю гри: з маяком і стрілками на мінімапі.')),
 ('book', t('f.story.t', 'Story and residents', 'Сюжет і жителі'),
  t('f.story.d', 'Where the story stands, side quests and where to go next by name. The live timetable of every resident of Greenvale.',
    'Де ви в сюжеті, побічні завдання й куди йти далі — назвою місця. Живий розклад кожного жителя Грінвейла.')),
 ('camera', t('f.photo.t', 'Photo mode', 'Фоторежим'),
  t('f.photo.d', 'Free camera, frozen time, 13 filters with grain, sepia, aberration and letterbox, your own presets, costumes, poses, PNG screenshots.',
    'Вільна камера, зупинка часу, 13 фільтрів із зерном, сепією, аберацією й кінорамкою, власні пресети, костюми, пози, знімки PNG.')),
 ('save', t('f.save.t', 'Safe saves', 'Надійні збереження'),
  t('f.save.d', 'Atomic writes, a damaged <code>dp.sav</code> restored by itself, 60 backups named by episode, chapter and play time.',
    'Атомарний запис, пошкоджений <code>dp.sav</code> відновлюється сам, 60 резервних копій із підписом: епізод, розділ, час гри.')),
 ('gauge', t('f.tools.t', 'Tools', 'Інструменти'),
  t('f.tools.d', 'Frame statistics, a built-in profiler that found the 45 FPS bug, cheats (money, time, weather, ammo), mouse sensitivity and inversion.',
    'Статистика кадру, вбудований профайлер, що знайшов баг 45 FPS, читкоди (гроші, час, погода, набої), чутливість і інверсія миші.')),
 ('globe', t('f.lang.t', 'Two languages', 'Дві мови'),
  t('f.lang.d', 'Ukrainian and English, switched in the menu. One DLL, no installer: press F10 in game and everything is there.',
    'Українська та англійська, перемикаються в меню. Одна DLL, без інсталятора: натисніть F10 у грі, і все там.')),
]

ENGINE = [
 (t('e.time.t', 'The "only a reboot helps" slowdown', 'Гальмування, яке лікувалось лише перезавантаженням'),
  t('e.time.d', 'The game counted time from the Windows uptime in single-precision floats: after days without a reboot the frame time lost precision. The mod hands it a counter that starts with the game.',
    'Гра рахувала час від часу роботи Windows у float одинарної точності: після кількох днів без перезавантаження час кадру втрачав точність. Мод дає їй лічильник, що стартує разом із грою.')),
 (t('e.fps.t', 'The 45 FPS mystery', 'Загадка 45 FPS'),
  t('e.fps.d', 'Every frame the game asked Windows about a WinMM gamepad, even with none connected, and on some systems that call takes milliseconds.',
    'Щокадру гра питала Windows про ґеймпад WinMM, навіть коли його немає, а на деяких системах цей виклик триває мілісекунди.')),
 (t('e.depth.t', 'Flicker in the distance', 'Блимання вдалині'),
  t('e.depth.d', 'The play camera\'s near plane sat at 1.0, so the 24-bit depth buffer had almost no precision far away. At 20.0 far roads, roofs and decals stop fighting.',
    'Ближня площина камери стояла на 1.0, тож 24-бітному буферу глибини вдалині майже не лишалось точності. На 20.0 далекі дороги, дахи й написи більше не «перебивають» одне одного.')),
 (t('e.ticks.t', 'Above 120 FPS', 'Понад 120 FPS'),
  t('e.ticks.d', 'About 80 timers turned the frame time into whole ticks: above 120 FPS they stood still or ran double. They now share whole steps.',
    'Близько 80 таймерів перетворювали час кадру на цілі такти: понад 120 FPS вони стояли або бігли вдвічі. Тепер вони ділять цілі кроки.')),
 (t('e.house.t', 'Day and night in buildings', 'День і ніч у будівлях'),
  t('e.house.d', 'The port read the building list with a wrong byte-order key: 64 of 81 entries were misread and interiors got the wrong light.',
    'Порт читав список будівель з неправильним порядком байтів: 64 з 81 записів читались хибно, і в приміщеннях було не те світло.')),
 (t('e.crash.t', 'The crash after cutscenes', 'Виліт після катсцен'),
  t('e.crash.d', 'An NPC sent to waypoint -1 read the navigation table out of bounds. Guarded at the lookup, together with a divide-by-zero freeze and a NaN hang.',
    'NPC, якого відправили до точки -1, читав таблицю навігації поза межами. Тепер там перевірка, як і для зависання на діленні на нуль і на NaN.')),
]

CREDITS = [
 ('ZachFix', 'h714je', 'https://github.com/h714je/ZachFix', t('c.zach', 'Research of the port, many ideas', 'Дослідження порту, багато ідей')),
 ('DPfix', 'Peter «Durante» Thoman', 'https://github.com/PeterTh/dpfix', t('c.dpfix', 'Resolution, shadows, texture replacement', 'Роздільність, тіні, підміна текстур')),
 ('DPStabilityFix', 'Cesario67', 'https://github.com/Cesario67/DeadlyPremonitionFix', t('c.stab', 'Saves, timing, DualSense layout', 'Збереження, час, розкладка DualSense')),
 ('CrashFix · MapFix · FreeCam', 'Behelit09', 'https://github.com/Behelit09', t('c.beh', 'Navigation crash, the full map, free camera', 'Виліт навігації, повна мапа, вільна камера')),
 ('DPRecomp', '«Little Bit»', 'https://github.com/LittleBitUA/DPRecomp', t('c.recomp', 'Our Xbox 360 recompilation: the reference the PC port is compared with', 'Наша рекомпіляція версії для Xbox 360: еталон, з яким порівнюємо PC-порт')),
 ('Kenney Input Prompts', 'Kenney', 'https://kenney.nl/assets/input-prompts', t('c.kenney', 'Gamepad button icons (CC0)', 'Іконки кнопок ґеймпада (CC0)')),
 ('DXVK', 'Philip «doitsujin» Rebohle', 'https://github.com/doitsujin/dxvk', t('c.dxvk', 'Optional Vulkan renderer, under its own license', 'Необов\'язковий Vulkan-рендерер, під власною ліцензією')),
]

SHOTS = [('menu-graphics.jpg', t('s.gfx', 'Screen and graphics', 'Екран і графіка')),
         ('menu-controls.jpg', t('s.ctl', 'Controls', 'Керування')),
         ('menu-world.jpg', t('s.world', 'Game and world', 'Гра і світ')),
         ('menu-fixes.jpg', t('s.fix', 'Fixes', 'Виправлення'))]

for k, en, uk in [
 ('nav.features', 'Features', 'Можливості'), ('nav.engine', 'Engine', 'Рушій'), ('nav.shots', 'Screenshots', 'Скріншоти'),
 ('nav.install', 'Install', 'Установка'), ('nav.about', 'About', 'Про проєкт'),
 ('hero.whatsnew', '✦ New in 0.7.0: a mod manager, no more flickering far textures, HBAO, SMAA, the Xbox 360 look, physics up to 180 FPS →',
  '✦ Нове в 0.7.0: менеджер модів, далекі текстури більше не блимають, HBAO, SMAA, вигляд Xbox 360, фізика до 180 FPS →'),
 ('hero.badge', 'FAN-MADE FIX · MIT · OPEN SOURCE', 'ФАНАТСЬКИЙ ФІКС · MIT · ВІДКРИТИЙ КОД'),
 ('hero.sub', 'THE ALL-IN-ONE FIX', 'УНІВЕРСАЛЬНИЙ ФІКС'),
 ('hero.tagline', 'One DLL in the game folder instead of DPfix, a stability fix, a map fix and a crash fix. Press F10 in game and everything is there.',
  'Одна DLL у теці гри замість DPfix, фіксу стабільності, фіксу мапи й фіксу вильотів. Натисніть F10 у грі, і все там.'),
 ('hero.download', 'DOWNLOAD', 'ЗАВАНТАЖИТИ'), ('hero.viewRepo', 'View on GitHub', 'Відкрити на GitHub'),
 ('hero.steam', 'Steam 1.01b', 'Steam 1.01b'), ('hero.one', 'One DLL · F10', 'Одна DLL · F10'), ('hero.langs', 'UA + EN', 'UA + EN'),
 ('hero.downloads', 'downloads', 'завантажень'),
 ('features.eyebrow', 'EVERYTHING IT DOES', 'ЩО ВІН РОБИТЬ'),
 ('features.title', 'Greenvale, the way it should have shipped', 'Грінвейл таким, яким він мав вийти'),
 ('engine.eyebrow', 'REVERSE ENGINEERING', 'REVERSE ENGINEERING'),
 ('engine.title', 'Fixed at the root', 'Виправлено в корені'),
 ('engine.lead', 'Every fix comes from taking the game\'s code apart and comparing the PC port with the Xbox 360 original.',
  'Кожне виправлення — результат розбору коду гри й порівняння PC-порту з оригіналом для Xbox 360.'),
 ('shots.eyebrow', 'IN GAME', 'У ГРІ'), ('shots.title', 'One menu for everything', 'Одне меню для всього'),
 ('credits.eyebrow', 'STANDING ON THE SHOULDERS', 'НА ЧИЇХ ПЛЕЧАХ СТОЇМО'), ('credits.title', 'Thanks to', 'Дякуємо'),
 ('credits.lead', 'The code is our own (MIT). The ideas, facts and addresses came from earlier community work.',
  'Код наш власний (MIT). Ідеї, факти й адреси взято з попередніх робіт спільноти.'),
 ('credits.testers', '🧪 Testers: <strong>Gold flin</strong> and <strong>Tree Fan</strong>. Thank you for playing the unfinished builds.',
  '🧪 Тестувальники: <strong>Gold flin</strong> і <strong>Tree Fan</strong>. Дякуємо, що грали в недороблені збірки.'),
 ('install.eyebrow', 'GET STARTED', 'ПОЧНІТЬ ГРАТИ'), ('install.title', 'Install in a minute', 'Установка за хвилину'),
 ('install.s1.t', 'Download', 'Завантажте'),
 ('install.s1.d', 'Take the latest <code>UltimateFIXDP-*.zip</code> from Releases and back up <code>savedata\\dp.sav</code>.',
  'Візьміть останній <code>UltimateFIXDP-*.zip</code> із Releases і зробіть копію <code>savedata\\dp.sav</code>.'),
 ('install.s2.t', 'Copy', 'Скопіюйте'),
 ('install.s2.d', 'Put <code>X3DAudio1_7.dll</code> and the <code>UltimateFix</code> folder next to <code>DP.exe</code>.',
  'Покладіть <code>X3DAudio1_7.dll</code> і теку <code>UltimateFix</code> поруч із <code>DP.exe</code>.'),
 ('install.s3.t', 'Play', 'Грайте'),
 ('install.s3.d', 'Start the game as usual and press <strong>F10</strong>. To remove the mod, delete the DLL.',
  'Запустіть гру як завжди й натисніть <strong>F10</strong>. Щоб прибрати мод, видаліть DLL.'),
 ('install.note', 'Steam version 1.01b. Do not combine with DPfix, ZachFix or DPStabilityFix: UltimateFIXDP replaces them. For a DualSense turn Steam Input off for the game.',
  'Steam-версія 1.01b. Не поєднуйте з DPfix, ZachFix і DPStabilityFix: UltimateFIXDP їх замінює. Для DualSense вимкніть Steam Input для гри.'),
 ('about.eyebrow', 'WHO MADE THIS', 'ХТО ЦЕ ЗРОБИВ'), ('about.title', 'About', 'Про проєкт'),
 ('about.line1', 'UltimateFIXDP is made by <strong>Dmytro Bidlov</strong> for the <span class="hl-ua">Ukrainian 🇺🇦 fan community</span> of <em>Deadly Premonition</em>. It is the successor of DP1 Launcher.',
  'UltimateFIXDP створив <strong>Dmytro Bidlov</strong> для <span class="hl-ua">української 🇺🇦 спільноти фанатів</span> <em>Deadly Premonition</em>. Це наступник DP1 Launcher.'),
 ('about.line2', 'It is free, open source and not affiliated with Access Games, Rising Star Games or Toybox Inc. The project ships no game files.',
  'Він безкоштовний, відкритий і не афілійований з Access Games, Rising Star Games чи Toybox Inc. Проєкт не містить файлів гри.'),
 ('about.thanks', 'Thanks to Swery (Hidetaka Suehiro) for an immortal, absurd and heart-warming game.',
  'Спасибі Swery (Hidetaka Suehiro) за безсмертну, абсурдну і щемливу гру.'),
 ('footer.line', 'Created by <strong>Dmytro Bidlov</strong> with love from <a href="https://t.me/LittleBitUA" target="_blank" rel="noopener">«Little Bit»</a> 🇺🇦',
  'Створено <strong>Dmytro Bidlov</strong> з любов\'ю від <a href="https://t.me/LittleBitUA" target="_blank" rel="noopener">«Little Bit»</a> 🇺🇦'),
 ('footer.disclaimer', 'Not affiliated with Access Games / Rising Star Games / Toybox Inc. All rights to the game belong to their respective owners.',
  'Не афілійовано з Access Games / Rising Star Games / Toybox Inc. Усі права на гру належать правовласникам.'),
 ('ui.scrollTop', 'Scroll to top', 'Нагору'),
]: T[k] = (en, uk)

def txt(key, tag='span', attrs='', html_=True):
    en = T[key][0]
    a = f' data-i18n-html="{key}"' if html_ else f' data-i18n="{key}"'
    return f'<{tag}{attrs}{a}>{en}</{tag}>'

GH = ('<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M12 .3a12 12 0 0 0-3.8 23.4c.6.1.8-.3.8-.6v-2c-3.3.7-4-1.6-4-1.6-.5-1.4-1.3-1.8-1.3-1.8-1.1-.7.1-.7.1-.7 1.2.1 1.8 1.2 1.8 1.2 1 1.8 2.8 1.3 3.5 1 .1-.8.4-1.3.7-1.6-2.7-.3-5.5-1.3-5.5-6 0-1.3.5-2.3 1.2-3.2-.1-.3-.5-1.5.1-3.2 0 0 1-.3 3.3 1.2a11.5 11.5 0 0 1 6 0c2.3-1.5 3.3-1.2 3.3-1.2.6 1.7.2 2.9.1 3.2.8.9 1.2 2 1.2 3.2 0 4.6-2.8 5.7-5.5 6 .4.4.8 1.1.8 2.2v3.3c0 .3.2.7.8.6A12 12 0 0 0 12 .3z"/></svg>')
TG = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M21.94 4.31a1 1 0 0 0-1.37-1.05L2.62 10.34a1 1 0 0 0 .06 1.86l4.27 1.32 1.62 5.14a1 1 0 0 0 1.74.37l2.18-2.62 4.13 3.04a1 1 0 0 0 1.58-.65zM9.4 14.4l-.5 4.04 3.5-3.5z"/></svg>'
YT = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M23.5 7.1a3 3 0 0 0-2.1-2.1C19.5 4.5 12 4.5 12 4.5s-7.5 0-9.4.5A3 3 0 0 0 .5 7.1C0 9 0 12 0 12s0 3 .5 4.9a3 3 0 0 0 2.1 2.1c1.9.5 9.4.5 9.4.5s7.5 0 9.4-.5a3 3 0 0 0 2.1-2.1C24 15 24 12 24 12s0-3-.5-4.9zM9.5 15.5v-7l6.3 3.5-6.3 3.5z"/></svg>'
ST = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2C6.6 2 2.2 6.1 2 11.3l5.3 2.2a3 3 0 0 1 1.7-.5h.2l2.4-3.4v-.1a4 4 0 1 1 4 4h-.1l-3.4 2.4v.2a3 3 0 0 1-5.7 1.3l-3.8-1.6C3.9 19.5 7.6 22 12 22c5.5 0 10-4.5 10-10S17.5 2 12 2z"/></svg>'

features = '\n'.join(
    f'''      <article class="glass-card feature">
        <div class="feature-icon">{icon(ic)}</div>
        {txt(tk, 'h3')}
        {txt(dk, 'p')}
      </article>''' for ic, tk, dk in FEATURES)
engine = '\n'.join(
    f'''      <article class="glass-card feature engine">
        {txt(tk, 'h3')}
        {txt(dk, 'p')}
      </article>''' for tk, dk in ENGINE)
credits = '\n'.join(
    f'''      <a class="glass-card credit" href="{url}" target="_blank" rel="noopener">
        <h3>{html.escape(name)}</h3>
        <p class="credit-by">{html.escape(by)}</p>
        {txt(dk, 'p')}
      </a>''' for name, by, url, dk in CREDITS)
shots = '\n'.join(
    f'''      <figure class="shot glass-card">
        <a href="screenshots/{f}" target="_blank" rel="noopener"><img src="screenshots/{f}" alt="{T[k][0]}" loading="lazy"></a>
        {txt(k, 'figcaption')}
      </figure>''' for f, k in SHOTS)

