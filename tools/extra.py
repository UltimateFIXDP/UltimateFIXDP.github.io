# Extra sections of the site (run inside build.py after base.py: uses t(), T, txt()).

STATS = [('180', t('st.fps', 'FPS with the car at normal speed', 'FPS, а машина їде нормально')),
         ('1', t('st.dll', 'DLL instead of five mods', "DLL замість п'яти модів")),
         ('64', t('st.map', 'tiles on the pause map', 'плитки на мапі паузи')),
         ('60', t('st.saves', 'named save backups', 'підписані копії збережень')),
         ('13', t('st.filters', 'photo mode filters', 'фільтрів фоторежиму')),
         ('0', t('st.files', 'game files changed on disk', 'змінених файлів гри на диску'))]

BEFORE = [
 (t('b1.a', 'About 45 FPS on many PCs, an idle GPU', 'Близько 45 FPS на багатьох ПК при вільній відеокарті'),
  t('b1.b', 'Up to 180 FPS, physics and timers at normal speed', 'До 180 FPS, фізика й таймери з нормальною швидкістю')),
 (t('b2.a', 'Picture rendered at 1280×720 and stretched', 'Картинка в 1280×720, розтягнута на екран'),
  t('b2.b', "Your monitor's resolution, up to 3× supersampling", 'Роздільність монітора, суперсемплінг до 3×')),
 (t('b3.a', 'Crashes after cutscenes, freezes, Alt+Tab hangs', 'Вильоти після катсцен, зависання, Alt+Tab'),
  t('b3.b', 'Guarded in the code, a dump if anything slips through', 'Перевірки в коді, дамп, якщо щось проскочить')),
 (t('b4.a', 'Far roads and roofs flicker', 'Далекі дороги й дахи блимають'),
  t('b4.b', 'Steady to the horizon', 'Стабільні до самого обрію')),
 (t('b5.a', 'Rumble calculated, never sent to the pad', 'Вібрація рахується, але не доходить до ґеймпада'),
  t('b5.b', 'Rumble and DualSense adaptive triggers per weapon', 'Вібрація й адаптивні триґери DualSense під кожну зброю')),
 (t('b6.a', 'A 3×3 window of the map that turns with you', 'Вікно мапи 3×3, що крутиться разом із вами'),
  t('b6.b', 'All 64 tiles, zoom, north up, your own waypoint', 'Усі 64 плитки, масштаб, північ угорі, власна мітка')),
 (t('b7.a', 'One save file, emptied before every write', 'Один файл збережень, що очищається перед кожним записом'),
  t('b7.b', 'Atomic writes and 60 named backups', 'Атомарний запис і 60 підписаних копій')),
 (t('b8.a', 'Difficulty stuck on Easy', 'Складність назавжди легка'),
  t('b8.b', 'Normal by default, your choice', 'Звичайна за замовчуванням, вибір за вами')),
]

NEWS = [
 (t('n1.t', 'Mod manager', 'Менеджер модів'),
  t('n1.d', 'Folders in <code>UltimateFix\\mods\\</code>, on/off and order in F10. Translations, texture packs, any game file by its name.',
    'Теки в <code>UltimateFix\\mods\\</code>, вмикання й порядок у F10. Переклади, текстурні паки, будь-який файл гри за іменем.')),
 (t('n2.t', 'Far textures fixed', 'Далекі текстури'),
  t('n2.d', 'Depth precision, mipmaps for textures without them, steadier far shadows.',
    'Точність глибини, міпмапи для текстур без них, стабільніші далекі тіні.')),
 (t('n3.t', 'HBAO · SMAA · Xbox 360 look', 'HBAO · SMAA · вигляд Xbox 360'),
  t('n3.d', "Horizon-based occlusion with a depth-aware blur, SMAA 1x, the console's grading and gamma.",
    'Затінення по горизонту з розмиттям за глибиною, SMAA 1x, кольорокорекція й гамма консолі.')),
 (t('n4.t', 'High FPS physics', 'Фізика на високому FPS'),
  t('n4.d', 'The car and about 80 timers of the game run right at 120–180 FPS. FPS unlocked by default.',
    'Машина й близько 80 таймерів гри працюють правильно на 120–180 FPS. FPS типово розблоковано.')),
 (t('n5.t', 'Story and residents', 'Сюжет і жителі'),
  t('n5.d', "Episode, chapter, side quests, the next destination by name; every resident's timetable.",
    'Епізод, розділ, побічні завдання, наступне місце назвою; розклад кожного жителя.')),
 (t('n6.t', 'Camera and mouse', 'Камера й миша'),
  t('n6.d', 'Field of view in play, the Xbox 360 quick turn, mouse speed 25–400 % and inversion per axis.',
    'Кут огляду в грі, швидкий розворот Xbox 360, швидкість миші 25–400 % та інверсія по осях.')),
 (t('n7.t', 'Photo mode presets', 'Пресети фоторежиму'),
  t('n7.d', '13 filters, grain, sepia, aberration, letterbox and four presets of your own.',
    '13 фільтрів, зерно, сепія, аберація, кінорамка й чотири власні пресети.')),
 (t('n8.t', 'Stability and saves', 'Стабільність і збереження'),
  t('n8.d', 'No endless hang on a NaN angle, audio kept in memory, 60 backups named by episode and chapter.',
    "Немає вічного зависання на NaN, звук тримається в пам'яті, 60 копій із підписом епізоду й розділу.")),
]

KEYS = [('F10', t('k.f10', 'Settings menu', 'Меню налаштувань')),
        ('F7', t('k.f7', 'Waypoint on the map or in the world', 'Мітка на мапі або у світі')),
        ('Shift+F7', t('k.sf7', 'Remove the waypoint', 'Прибрати мітку')),
        ('Ctrl+F7', t('k.cf7', "Waypoint to the game's objective", 'Мітка на ціль гри')),
        ('Shift+S', t('k.ss', 'Quick turn', 'Швидкий розворот')),
        ('F6', t('k.f6', 'Photo mode', 'Фоторежим')),
        ('F5', t('k.f5', 'Free camera', 'Вільна камера')),
        ('F11', t('k.f11', 'Screenshot (PNG, without the menu)', 'Знімок екрана (PNG, без меню)'))]

FAQ = [
 (t('q1', 'Is it safe for my saves?', 'Чи безпечно для збережень?'),
  t('a1', 'Yes. The mod writes <code>dp.sav</code> through a temporary file and keeps 60 backups in <code>UltimateFix\\savebackups</code>, each named by episode, chapter and play time. A damaged save is restored from the newest good copy by itself. Still, back up your save before the first start.',
    'Так. Мод пише <code>dp.sav</code> через тимчасовий файл і тримає 60 копій у <code>UltimateFix\\savebackups</code>, кожна з підписом епізоду, розділу й часу гри. Пошкоджений сейв відновлюється з найновішої доброї копії сам. Але перед першим запуском усе одно зробіть копію.')),
 (t('q2', 'Which version of the game?', 'Яка версія гри потрібна?'),
  t('a2', "The Steam version 1.01b of <em>The Director's Cut</em>. Every patch checks the game's bytes first: on another build it switches itself off and says so in <code>ufx.log</code>.",
    'Steam-версія 1.01b <em>The Director\'s Cut</em>. Кожна правка спершу звіряє байти гри: на іншій збірці вона вимикається сама й пише про це в <code>ufx.log</code>.')),
 (t('q3', 'Can I keep DPfix, ZachFix or DP1 Launcher?', 'Чи можна лишити DPfix, ZachFix або DP1 Launcher?'),
  t('a3', 'No, UltimateFIXDP replaces them. Remove DPfix (<code>d3d9.dll</code>, <code>DPfix.ini</code>) and the other fixes first.',
    'Ні, UltimateFIXDP їх замінює. Спершу приберіть DPfix (<code>d3d9.dll</code>, <code>DPfix.ini</code>) та інші фікси.')),
 (t('q4', 'How do I install a translation?', 'Як поставити переклад?'),
  t('a4', 'Make a folder in <code>UltimateFix\\mods\\</code> and put the game files there (<code>fontwide.xpc</code>, <code>mes_all.mes</code>), or the <code>text\\</code> folder of the SWERY Localization Tool. Switch it on in F10 → Mods and restart the game.',
    'Створіть теку в <code>UltimateFix\\mods\\</code> і покладіть туди файли гри (<code>fontwide.xpc</code>, <code>mes_all.mes</code>) або теку <code>text\\</code> із SWERY Localization Tool. Увімкніть мод у F10 → Моди й перезапустіть гру.')),
 (t('q5', 'The DualSense does not work', 'DualSense не працює'),
  t('a5', 'Turn Steam Input off for the game (Properties → Controller). Then the mod reads the DualSense directly over USB or Bluetooth.',
    'Вимкніть Steam Input для гри (Властивості → Контролер). Тоді мод читає DualSense напряму через USB або Bluetooth.')),
 (t('q6', 'Something broke. What do I send?', 'Щось зламалось. Що надіслати?'),
  t('a6', '<code>UltimateFix\\ufx.log</code> and any <code>crash_*.dmp</code> / <code>hang_*.dmp</code>, through GitHub Issues or Telegram. Every feature can be switched off in F10; <code>[Debug] SafeMode=1</code> starts with fewer hooks.',
    '<code>UltimateFix\\ufx.log</code> і файли <code>crash_*.dmp</code> / <code>hang_*.dmp</code>, якщо є, через GitHub Issues або Telegram. Будь-яку функцію можна вимкнути в F10; <code>[Debug] SafeMode=1</code> запускає мод із меншою кількістю хуків.')),
 (t('q7', 'How do I remove it?', 'Як видалити?'),
  t('a7', 'Delete <code>X3DAudio1_7.dll</code> from the game folder. Nothing else of the game is changed; to undo the 4 GB flag, put <code>DP.exe.bak</code> back as <code>DP.exe</code> or let Steam verify the files.',
    'Видаліть <code>X3DAudio1_7.dll</code> із теки гри. Більше нічого в грі не змінено; щоб прибрати прапор 4 ГБ, поверніть <code>DP.exe.bak</code> як <code>DP.exe</code> або перевірте файли в Steam.')),
]

for k, en, uk in [
 ('nav.new', "What's new", 'Нове'), ('nav.mods', 'Mods', 'Моди'), ('nav.faq', 'FAQ', 'Питання'),
 ('before.eyebrow', 'BEFORE AND AFTER', 'ДО І ПІСЛЯ'), ('before.title', 'The PC port, fixed', 'PC-порт, виправлений'),
 ('before.a', 'Stock PC port', 'Звичайний PC-порт'), ('before.b', 'With UltimateFIXDP', 'З UltimateFIXDP'),
 ('new.eyebrow', 'VERSION 0.7.0', 'ВЕРСІЯ 0.7.0'), ('new.title', "What's new", 'Що нового'),
 ('new.all', 'All changes on GitHub →', 'Усі зміни на GitHub →'),
 ('new.known', '<strong>Known issues:</strong> a light strip along some wall corners with HBAO, doubled depth-of-field edges at render scale 300 %, the X on the pause map drifts while the map pans.',
  "<strong>Відомі проблеми:</strong> світла смужка вздовж деяких кутів з HBAO, подвоєні краї глибини різкості на масштабі рендеру 300 %, X на мапі паузи з'їжджає під час прокручування."),
 ('mods.eyebrow', 'MOD MANAGER', 'МЕНЕДЖЕР МОДІВ'), ('mods.title', 'Drop a folder, press F10', 'Покладіть теку, натисніть F10'),
 ('mods.lead', "Every folder in <code>UltimateFix\\mods\\</code> is a mod. The one higher in the list wins. Nothing is written to the game's files: everything is replaced in memory.",
  "Кожна тека в <code>UltimateFix\\mods\\</code> — це мод. Той, що вище в списку, перекриває нижчі. У файли гри нічого не пишеться: усе підміняється в пам'яті."),
 ('mods.c1.t', 'Game files by name', 'Файли гри за іменем'),
 ('mods.c1.d', "Any file of the game's archives right in the mod folder: by its name when it is unique, or by its path (<code>UPDATA\\…</code>). A <code>.dds</code> with an XPC's name replaces the picture inside it.",
  'Будь-який файл з архівів гри просто в теці мода: за іменем, якщо воно унікальне, або за шляхом (<code>UPDATA\\…</code>). <code>.dds</code> з іменем XPC замінює картинку всередині нього.'),
 ('mods.c2.t', 'Translations', 'Переклади'),
 ('mods.c2.d', "<code>text\\mes_all.json</code> and <code>glyphmap.json</code> of the SWERY Localization Tool are laid over the game's text, record by record.",
  '<code>text\\mes_all.json</code> і <code>glyphmap.json</code> із SWERY Localization Tool накладаються на текст гри, запис за записом.'),
 ('mods.c3.t', 'Textures', 'Текстури'),
 ('mods.c3.d', '<code>textures\\&lt;hash&gt;.dds</code> or <code>.png</code>, compatible with the packs for DPfix. <code>[Debug] DumpTextures=1</code> dumps every texture named by its hash.',
  '<code>textures\\&lt;хеш&gt;.dds</code> або <code>.png</code>, сумісно з паками для DPfix. <code>[Debug] DumpTextures=1</code> скидає всі текстури з назвою-хешем.'),
 ('keys.eyebrow', 'CONTROLS', 'КЛАВІШІ'), ('keys.title', 'Keys worth knowing', 'Клавіші, які варто знати'),
 ('faq.eyebrow', 'QUESTIONS', 'ПИТАННЯ'), ('faq.title', 'Before you ask', 'Часті питання'),
 ('cta.title', 'Greenvale is waiting', 'Ґрінвейл чекає'),
 ('cta.text', 'Free, open source, one file. Agent York would approve.', 'Безкоштовно, відкритий код, один файл. Агент Йорк схвалив би.'),
 ('cta.issue', 'Report a problem', 'Повідомити про проблему'),
]:
    T[k] = (en, uk)


def kbd(combo):
    parts = combo.split('+')
    out = []
    for i, x in enumerate(parts):
        out.append('<kbd>' + html.escape(x) + '</kbd>')
        if i < len(parts) - 1:
            out.append('<span class="plus">+</span>')
    return ''.join(out)


stats = '\n'.join('      <div class="stat reveal"><span class="stat-num">%s</span>%s</div>' % (n, txt(k, 'span', ' class="stat-label"', False)) for n, k in STATS)
before = '\n'.join('      <div class="ba-row reveal"><div class="ba-cell ba-old">%s</div><div class="ba-arrow">→</div><div class="ba-cell ba-new">%s</div></div>'
                   % (txt(a, 'span', '', False), txt(b, 'span', '', False)) for a, b in BEFORE)
news = '\n'.join('      <article class="glass-card news reveal">%s%s</article>' % (txt(tk, 'h3', '', False), txt(dk, 'p')) for tk, dk in NEWS)
keys = '\n'.join('      <div class="key-row"><span class="keys">%s</span>%s</div>' % (kbd(k), txt(dk, 'span', ' class="key-what"', False)) for k, dk in KEYS)
faq = '\n'.join('      <details class="glass-card faq reveal"><summary>%s</summary>%s</details>' % (txt(qk, 'span', '', False), txt(ak, 'p')) for qk, ak in FAQ)
tree = ('<pre class="tree"><span class="t-dim">Deadly Premonition The Director\'s Cut\\</span>\n'
        '├─ DP.exe\n'
        '├─ X3DAudio1_7.dll        <span class="t-red">← UltimateFIXDP</span>\n'
        '└─ UltimateFix\\\n'
        '   └─ mods\\\n'
        '      ├─ UA\\\n'
        '      │  ├─ fontwide.xpc\n'
        '      │  └─ mes_all.mes\n'
        '      └─ HD Textures\\\n'
        '         ├─ mod.ini\n'
        '         └─ textures\\\n'
        '            └─ 1a2b3c4d.dds</pre>')


# ---- texts of the calm design (2026-11-19) ----
for k, en, uk in [
 ('hero.pill', "Version 0.7.12 · residents in the photo mode, play as Emily, a spawner", "Версія 0.7.12 · жителі у фоторежимі, гра за Емілі, спавнер"),
 ('hero.title', 'Deadly Premonition,<br>the way it should have been', 'Deadly Premonition,<br>якою вона мала бути'),
 ('hero.lead', "One file in the game folder instead of five mods. Stability, up to 180 FPS, your monitor's resolution and a full settings menu on F10.",
  "Один файл у теці гри замість п'яти модів. Стабільність, до 180 FPS, роздільність вашого монітора й повне меню налаштувань на F10."),
 ('hero.dl', 'Download for Windows', 'Завантажити для Windows'),
 ('hero.code', 'Code on GitHub', 'Код на GitHub'),
 ('hero.meta', 'Steam 1.01b · free, MIT · UA + EN', 'Steam 1.01b · безкоштовно, MIT · UA + EN'),
 ('nav.download', 'Download', 'Завантажити'),
 ('nav.compare', 'Before and after', 'До і після'),
 ('s2.fps', 'and the car and timers run right', 'а машина й таймери йдуть нормально'),
 ('s2.dll', 'instead of DPfix and four other fixes', 'замість DPfix і чотирьох інших фіксів'),
 ('s2.saves', 'named save backups', 'підписаних резервних копій сейвів'),
 ('s2.files', 'game files changed on disk', 'змінених файлів гри на диску'),
 ('f2.title', 'Everything the PC version was missing', 'Усе, чого бракувало PC-версії'),
 ('f2.lead', 'Every fix comes from taking the game\'s code apart and comparing it with the Xbox 360 original.',
  'Кожне виправлення — з розбору коду гри й порівняння з оригіналом для Xbox 360.'),
 ('e2.title', 'Fixed at the root', 'Виправлено в корені'),
 ('n2.title', "What's new in 0.7.0", 'Що нового в 0.7.0'),
 ('c2.title', 'Before and after', 'До і після'),
 ('c2.lead', 'What changes in the PC port once UltimateFIXDP is in the game folder.', "Що змінюється в PC-порті, щойно в теці гри з'являється UltimateFIXDP."),
 ('m2.title', 'Mods without instructions', 'Моди без інструкцій'),
 ('m2.lead', "Put a folder into <code>UltimateFix\\mods\\</code> and switch it on in F10 → Mods. The game's files stay as they are: everything is replaced in memory.",
  "Покладіть теку в <code>UltimateFix\\mods\\</code> і ввімкніть її в F10 → Моди. Файли гри не змінюються: усе підміняється в пам'яті."),
 ('sh2.title', 'One menu for everything', 'Одне меню для всього'),
 ('i2.title', 'Install in a minute', 'Установка за хвилину'),
 ('k2.title', 'Keys', 'Клавіші'),
 ('q2.title', 'Questions', 'Питання'),
 ('cr2.title', 'Thanks to', 'Дякуємо'),
 ('cta2.title', 'Greenvale is waiting', 'Ґрінвейл чекає'),
 ('cta2.text', 'Free, open source, one file.', 'Безкоштовно, відкритий код, один файл.'),
]:
    T[k] = (en, uk)

STATS2 = [('180 FPS', 's2.fps'), ('1 DLL', 's2.dll'), ('60', 's2.saves'), ('0', 's2.files')]
stats2 = '\n'.join('      <div class="stat2 reveal"><div class="stat2-num">%s</div>%s</div>' % (n, txt(k, 'div', ' class="stat2-label"', False)) for n, k in STATS2)
compare = '\n'.join('      <div class="cmp-row"><span class="cmp-old">%s</span><span class="cmp-new">%s</span></div>'
                    % (txt(a, 'span', '', False), txt(b, 'span', '', False)) for a, b in BEFORE)
news2 = '\n'.join('      <li class="news2 reveal">%s%s</li>' % (txt(tk, 'h3', '', False), txt(dk, 'p')) for tk, dk in NEWS)


# ---- live F10 menu in the hero and the bento of features (2026-11-19) ----
MENU = [
 (('Screen and graphics', 'Екран і графіка'), ('Most items work at once, without restarting the game.', 'Більшість пунктів діє одразу, без перезапуску гри.'),
  [(('Borderless window', 'Вікно без рамки'), 1), (("Your monitor's resolution", 'Роздільність монітора'), 1), (('HBAO ambient occlusion', 'Затінення HBAO'), 1),
   (('SMAA anti-aliasing', 'Згладжування SMAA'), 1), (('Xbox 360 look', 'Вигляд Xbox 360'), 0)]),
 (('Input', 'Ввід'), ('The DualSense works without Steam Input, over USB or Bluetooth.', 'DualSense працює без Steam Input, через USB або Bluetooth.'),
  [(('DualSense directly', 'DualSense напряму'), 1), (('Adaptive triggers', 'Адаптивні триґери'), 1), (('Aim on L2, fire on R2', 'Приціл на L2, постріл на R2'), 1),
   (('Quick turn', 'Швидкий розворот'), 1), (('Invert the mouse', 'Інвертувати мишу'), 0)]),
 (('Game and world', 'Гра і світ'), ("The waypoint becomes the game's own objective: a beacon and minimap arrows.", 'Мітка стає рідною ціллю гри: маяк і стрілки на мінімапі.'),
  [(('Full pause map', 'Повна мапа паузи'), 1), (('Waypoint on F7', 'Мітка на F7'), 1), (('High FPS physics', 'Фізика на високому FPS'), 1),
   (('Longer draw distance', 'Більша дальність промальовки'), 1), (('Pause while the menu is open', 'Пауза, коли відкрите меню'), 0)]),
 (('Photo mode', 'Фоторежим'), ('13 filters and four presets of your own.', '13 фільтрів і чотири власні пресети.'),
  [(('Free camera', 'Вільна камера'), 0), (('Freeze time', 'Зупинити час'), 0), (('Hide the interface', 'Сховати інтерфейс'), 0),
   (('Film grain', 'Зерно плівки'), 0), (('Letterbox', 'Кінорамка'), 0)]),
 (('Fixes', 'Виправлення'), ("Every patch checks the game's bytes first.", 'Кожна правка спершу звіряє байти гри.'),
  [(('Crash guards', 'Захист від вильотів'), 1), (('Hang watchdog', 'Захист від зависань'), 1), (('Save backups', 'Резервні копії сейвів'), 1),
   (('60 limit on 61–139 Hz', 'Ліміт 60 на 61–139 Гц'), 1), (('Safe mode', 'Безпечний режим'), 0)]),
 (('Mods', 'Моди'), ('A mod higher in the list wins over the ones below.', 'Мод вище в списку перекриває ті, що нижче.'),
  [(('UA · translation', 'UA · переклад'), 1), (('HD Textures', 'HD Textures'), 1), (('My font', 'Мій шрифт'), 0)]),
]
menu_tabs, menu_panels = [], []
for i, (name, hint, items) in enumerate(MENU):
    T['menu.t%d' % i] = name
    T['menu.h%d' % i] = hint
    menu_tabs.append('<button type="button" role="tab" class="fx-tab%s" data-tab="%d" aria-selected="%s" data-i18n="menu.t%d">%s</button>'
                     % (' active' if i == 0 else '', i, 'true' if i == 0 else 'false', i, name[0]))
    rows = []
    for j, (label, on) in enumerate(items):
        T['menu.i%d_%d' % (i, j)] = label
        rows.append('<button type="button" class="fx-item" aria-pressed="%s"><span data-i18n="menu.i%d_%d">%s</span><span class="fx-switch" aria-hidden="true"></span></button>'
                    % ('true' if on else 'false', i, j, label[0]))
    menu_panels.append('<div class="fx-panel" role="tabpanel" data-panel="%d"%s><div class="fx-title" data-i18n="menu.t%d">%s</div>%s<div class="fx-hint" data-i18n="menu.h%d">%s</div></div>'
                       % (i, '' if i == 0 else ' hidden', i, name[0], ''.join(rows), i, hint[0]))
menu_tabs = '\n          '.join(menu_tabs)
menu_panels = '\n        '.join(menu_panels)

for k, en, uk in [
 ('menu.hint', 'Try it: click a section on the left and the switches on the right.', 'Спробуйте: клацніть розділ ліворуч і перемикачі праворуч.'),
 ('menu.close', 'F10 · close', 'F10 · закрити'),
 ('bt.perf', 'Performance', 'Продуктивність'),
 ('bt.perf.d', 'Found with the built-in profiler: every frame the game asked Windows about a gamepad. Physics and timers now run right at any refresh rate.',
  'Знайдено вбудованим профайлером: гра щокадру питала Windows про ґеймпад. Фізика й таймери тепер працюють правильно на будь-якій частоті.'),
 ('bt.stab', 'Stability', 'Стабільність'), ('bt.stab.d', 'No crash after cutscenes, no hang after Alt+Tab.', 'Без вильотів після катсцен і зависань після Alt+Tab.'),
 ('bt.saves', '60 save backups', '60 копій сейвів'), ('bt.saves.d', 'Each named by episode, chapter and play time.', 'Кожна підписана епізодом, розділом і часом гри.'),
 ('bt.gfx', 'Graphics', 'Графіка'), ('bt.gfx.d', "Your monitor's resolution, HBAO, SMAA, the Xbox 360 look, no flickering far away.", 'Роздільність монітора, HBAO, SMAA, вигляд Xbox 360, без блимання вдалині.'),
 ('bt.mods', 'Mod manager', 'Менеджер модів'), ('bt.mods.t', 'A translation is just a folder', 'Переклад — це просто тека'),
 ('bt.mods.d', 'Put the game files into UltimateFix\\mods\\UA\\ and switch the mod on in F10.', 'Покладіть файли гри в UltimateFix\\mods\\UA\\ і ввімкніть мод у F10.'),
 ('bt.pad', 'DualSense', 'DualSense'), ('bt.pad.d', 'Adaptive triggers for every weapon, without Steam Input.', 'Адаптивні триґери під кожну зброю, без Steam Input.'),
 ('more.title', 'And also', 'А ще'),
]:
    T[k] = (en, uk)
