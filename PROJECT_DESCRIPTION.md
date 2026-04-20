# Утренняя Практика — Projekt-Beschreibung für Claude Code

## Was ist das Projekt?

Eine webbasierte Morgenroutine-App (single HTML-Datei + Audio-Dateien), die den Nutzer per Stimme durch eine 13-minütige Meditationspraxis führt. Die App basiert auf dem 5-Schritt-Protokoll von Joe Dispenza (RAS-Reprogrammierung) und integriert Zitate aus verifizierten Büchern von 9 Autoren.

---

## Dateistruktur

```
morning-practice/
├── index.html           ← die komplette App (HTML + CSS + JS)
├── generate_audio.py    ← Python-Skript zur MP3-Generierung
├── requirements.txt     ← requests, python-dotenv
├── .env                 ← ELEVEN_API_KEY=... (nicht in GitHub!)
├── .gitignore           ← .env, __pycache__/
├── README.md
└── audio/               ← 51 generierte MP3-Dateien
    ├── s1_marina_01.mp3
    ├── s1_maxim_01.mp3
    └── ...
```

---

## Design & Ästhetik

- **Farbschema:** Tief-dunkler Hintergrund (`#0a0c0f`), goldene Akzente (`#c9a96e`, `#f0d898`), helle cremefarbene Texte (`#f0ead8`, `#faf6ee`) — gut lesbar auf dunklem Hintergrund
- **Typografie:** Cormorant Garamond (Fließtext), Cinzel (Überschriften, Labels), IM Fell English (Zitate kursiv)
- **Animationen:** Sternen-Hintergrund, goldene Orb-Animation pro Schritt, Gong-Lichtblitz beim Übergang, Wellenanimation während der Stille
- **Stil:** Luxuriös, meditativ, spirituell — kein generisches AI-Design

---

## Stimmenauswahl

Auf dem Startbildschirm wählt der Nutzer zwischen zwei Stimmen:

| Button | Name | Charakter | ElevenLabs Voice ID |
|--------|------|-----------|---------------------|
| ♀ Марина | weiblich | sanft, warm | `ymDCYd8puC7gYjxIamPt` |
| ♂ Максим | männlich | tief, ruhig | `HcaxAsrhw4ByUo4CBCBN` |

- Der gewählte Button leuchtet golden auf (`.selected` Klasse)
- **Марина** ist vorausgewählt
- Die gewählte Stimme liest **alle** Sätze des gesamten Ablaufs
- Kein API-Key-Eingabefeld für den Nutzer — Voice IDs sind intern im Code
- Stimme wird in generate_audio.py (kostenlos, kein eigener Server) aufgerufen.


---

## Vollständige Audio-Map (Dateiname → Text → Schritt)

Die App spielt die Sätze in dieser exakten Reihenfolge ab. Jeder Schritt hat eine geordnete Liste von Dateinamen:

```javascript
const AUDIO_MAP = {
  step1: [
    "s1_marina_01", // Шаг первый. Дыхание.
    "s1_marina_02", // Сядьте удобно.
    "s1_marina_03", // Закройте глаза.
    "s1_marina_04", // Сделайте вдох через нос.
    "s1_marina_05", // Задержите.
    "s1_marina_06", // Короткий дополнительный вдох.
    "s1_marina_07", // И медленный... долгий выдох через рот.
    "s1_marina_08", // Вы переключаетесь из режима стресса в режим открытости.
    "s1_marina_09", // Повторяйте этот цикл.
    "s1_maxim_01",  // Закройте глаза... Джо Диспенза.
    "s1_maxim_02",  // Двойной вдох... Эндрю Хаберман.
    "s1_maxim_03",  // Я хочу отпустить... Луиза Хей.
  ],
  step2: [
    "s2_marina_01", // Шаг второй. Сердечная когерентность.
    "s2_marina_02", // Перенесите всё внимание в центр груди.
    "s2_marina_03", // Дышите медленно через сердце.
    "s2_marina_04", // Вспомните один момент настоящей благодарности или любви.
    "s2_marina_05", // Позвольте этому чувству расшириться...
    "s2_marina_06", // Удерживайте его как можно дольше.
    "s2_maxim_01",  // Сердечная когерентность... Джо Диспенза.
    "s2_maxim_02",  // Чувство — ключ... Грэг Брейден.
    "s2_maxim_03",  // Мир пронизан любовью... Луиза Хей.
  ],
  step3: [
    "s3_marina_01", // Шаг третий. Декларация новой идентичности.
    "s3_marina_02", // Вы всё ещё в состоянии сердечной когерентности.
    "s3_marina_03", // Из этого тепла и открытости...
    "s3_marina_04", // Не кем вы хотите стать...
    "s3_marina_05", // Например: Я — человек...
    "s3_marina_06", // Прочувствуйте каждое слово.
    "s3_maxim_01",  // Создание новой реальности... Джо Диспенза.
    "s3_maxim_02",  // Фокус всегда должен быть... Джеймс Клир.
    "s3_maxim_03",  // Главное в нашей жизни — мысль... Луиза Хей.
  ],
  step4: [
    "s4_marina_01", // Шаг четвёртый. Защита состояния.
    "s4_marina_02", // Представьте свой предстоящий день.
    "s4_marina_03", // Первую встречу. Первый разговор.
    "s4_marina_04", // Увидьте себя — уже в новом состоянии...
    "s4_marina_05", // Установите намерение...
    "s4_marina_06", // Это ваш якорь на весь день.
    "s4_maxim_01",  // Чем более осознанны вы... Джо Диспенза.
    "s4_maxim_02",  // Всегда говорите да... Экхарт Толле.
    "s4_maxim_03",  // Никогда не пропускайте... Джеймс Клир.
  ],
  step5: [
    "s5_marina_01", // Шаг пятый. Поиск подтверждений.
    "s5_marina_02", // Активируйте режим поиска.
    "s5_marina_03", // Сегодня вы будете замечать всё...
    "s5_marina_04", // Каждое маленькое доказательство...
    "s5_marina_05", // Мозг начинает видеть то, во что вы верите.
    "s5_marina_06", // Завершите практику тремя словами благодарности...
    "s5_maxim_01",  // Испытывая благодарность... Джо Диспенза.
    "s5_maxim_02",  // Вы в своей жизни видите... Уэйн Дайер.
    "s5_maxim_03",  // Меняя то, что происходит внутри нас... Грэг Брейден.
  ],
  finish: [
    "finish_01",    // Практика завершена.
    "finish_02",    // Вы сделали шаг к новой версии себя.
    "finish_03",    // Несите это состояние через весь день.
  ]
};
```

**Wichtig:** Alle Dateien liegen im Ordner `audio/` und haben die Endung `.mp3`.
Abspiel-Logik: `new Audio('audio/' + fileId + '.mp3')`

---

## Audio-Dateien (Zielzustand)

Sobald die MP3-Dateien über `generate_audio.py` generiert wurden, soll die App **lokale Dateien** aus dem `audio/` Ordner abspielen statt die API bei jedem Start aufzurufen:

```javascript
const audio = new Audio(`audio/${fileId}.mp3`);
```

Dateinamen-Schema:
- `s{schritt}_marina_{nr}.mp3` — Anweisungen (Марина-Stimme)
- `s{schritt}_maxim_{nr}.mp3` — Zitate (Максим-Stimme)
- `finish_0{nr}.mp3` — Abschluss

**Wenn lokale Dateien vorhanden:** lokale MP3 abspielen, sonst nichts.


## 5-Schritte-Ablauf

### Genereller Ablauf pro Schritt:
1. **Gong** (synthetisierter Sound + goldener Lichtblitz) — außer beim ersten Schritt
2. **Stimme liest** — Anweisung Satz für Satz, 2 Sekunden Pause zwischen jedem Satz
3. **Stille-Phase** — Overlay mit Countdown-Timer und Wellenanimation
4. Nächster Schritt beginnt

---

### SCHRITT I — Дыхание (Дыхание, 2 Min. + 1 Min. Stille)

**Hintergrund-Musik:** Nutze die Audiofile in /audio  für sigmamusicart_*

**Anweisung (Марина liest):**
- Шаг первый. Дыхание.
- Сядьте удобно.
- Закройте глаза.
- Сделайте вдох через нос.
- Задержите.
- Короткий дополнительный вдох.
- И медленный... долгий выдох через рот.
- Вы переключаетесь из режима стресса в режим открытости.
- Повторяйте этот цикл.

**Zitate (Максим liest) — Format: Zitat zuerst, Autor am Ende:**
- Закройте глаза и сделайте несколько медленных, глубоких вздохов — чтобы расслабить разум и тело. Джо Диспенза.
- Двойной вдох через нос, длинный выдох — и вы переключаетесь с симпатической системы на парасимпатическую. Эндрю Хаберман.
- Я хочу отпустить. Я освобождаю. Я избавляюсь от напряжения. Луиза Хей.

---

### SCHRITT II — Сердечная Когерентность (3 Min. + 1,5 Min. Stille)

**Hintergrund-Musik:** Nutze die Audiofile in /audio  für sigmamusicart_*

**Anweisung (Марина liest):**
- Шаг второй. Сердечная когерентность.
- Перенесите всё внимание в центр груди.
- Дышите медленно через сердце.
- Вспомните один момент настоящей благодарности или любви.
- Позвольте этому чувству расшириться и заполнить всю грудную клетку.
- Удерживайте его как можно дольше.

**Zitate (Максим liest):**
- Сердечная когерентность начинается с поддержания возвышенных чувств — благодарности, признательности, вдохновения, сострадания, любви и радости. Джо Диспенза.
- Чувство — ключ. Только чувство способно войти в резонанс с окружающим миром. Грэг Брейден.
- Мир пронизан любовью. Я люблю. И я способна вызвать ответное чувство. Луиза Хей.

---

### SCHRITT III — Декларация Новой Идентичности (3 Min. + 1,5 Min. Stille)

**Hintergrund-Musik:** Nutze die Audiofile in /audio  für the_mountain_meditation*

**Anweisung (Марина liest):**
- Шаг третий. Декларация новой идентичности.
- Вы всё ещё в состоянии сердечной когерентности.
- Из этого тепла и открытости произнесите вслух одну сильную декларацию.
- Не кем вы хотите стать. А кем вы уже являетесь прямо сейчас.
- Например: Я — человек, который действует из ясности и уверенности.
- Прочувствуйте каждое слово.

**Zitate (Максим liest):**
- Создание новой реальности невозможно без создания новой личности. Снова и снова репетируйте будущее в мыслях, пока оно запечатлеется как новые нейронные связи. Джо Диспенза.
- Фокус всегда должен быть на той личности, какой вы хотите стать. Каждое действие — это голос за того человека, которым вы хотите стать. Джеймс Клир.
- Главное в нашей жизни — мысль. А мысль всегда можно изменить. Луиза Хей.

---

### SCHRITT IV — Защита Состояния (2 Min. + 1 Min. Stille)

**Hintergrund-Musik:** Nutze die Audiofile in /audio  für sigmamusicart_*

**Anweisung (Марина liest):**
- Шаг четвёртый. Защита состояния.
- Представьте свой предстоящий день.
- Первую встречу. Первый разговор.
- Увидьте себя — уже в новом состоянии — в каждом из них.
- Установите намерение: при любом отклонении вы возвращаетесь к себе.
- Это ваш якорь на весь день.

**Zitate (Максим liest):**
- Чем более осознанны вы к состояниям тела и ума, тем реже вы будете действовать на автопилоте. Привычная мысль уже не проскользнёт незамеченной. Джо Диспенза.
- Всегда говорите да текущему мгновению. Скажите жизни да — и вы увидите, как она начнёт работать на вас. Экхарт Толле.
- Никогда не пропускайте действие дважды. Если пропустили один день — вернитесь как можно скорее. Джеймс Клир.

---

### SCHRITT V — Поиск Подтверждений (3 Min. + 1,5 Min. Stille)

**Hintergrund-Musik:** Nutze die Audiofile in /audio  für sigmamusicart_*

**Anweisung (Марина liest):**
- Шаг пятый. Поиск подтверждений.
- Активируйте режим поиска.
- Сегодня вы будете замечать всё, что подтверждает вашу новую идентичность.
- Каждое маленькое доказательство — это подпитка.
- Мозг начинает видеть то, во что вы верите.
- Завершите практику тремя словами благодарности за сегодняшний день.

**Zitate (Максим liest):**
- Испытывая благодарность, мы сигнализируем, что событие уже произошло. Нужно чувствовать себя так, словно то, чего мы хотим, уже присутствует в нашей жизни. Джо Диспенза.
- Вы в своей жизни видите главным образом то, во что верите. Уэйн Дайер.
- Меняя то, что происходит внутри нас — мысли, чувства и убеждения — мы меняем и окружающий мир. Грэг Брейден.

---

### ABSCHLUSS

**Марина liest:**
- Практика завершена.
- Вы сделали шаг к новой версии себя.
- Несите это состояние через весь день.

---

## UI-Elemente

### Startbildschirm
- Titel: Утренняя Практика
- Untertitel: 5 шагов к новому состоянию
- Übersicht der 5 Schritte mit Zeitangaben
- **Stimmenauswahl:** zwei Buttons (Марина / Максим)
- Start-Button: НАЧАТЬ ПРАКТИКУ
- Hinweis: ~ 13 минут

### Während der Praxis
- **5 Fortschrittspunkte** oben (dots, aktiver leuchtet gold)
- **Schritt-Badge:** ШАГ I · 5
- **Überschrift** des aktuellen Schritts
- **Goldene Orb-Animation** (stepspezifisch)
- **Timer** (Countdown in MM:SS)
- **Phase-Label** mit Text + animierten Punkten beim Sprechen
- **Inhaltsbereich** (scrollbar): Anweisung-Box + 3 Zitat-Boxen
- **Buttons:** ПАУЗА / ПРОПУСТИТЬ →

### Stille-Overlay (Fullscreen)
- Großer Countdown-Timer
- Text: Тишина. Оставайтесь в своём состоянии.
- Wellenanimation (7 Balken)
- Button: Продолжить →

### Abschlussbildschirm
- Icon ✦ mit Glow-Animation
- Titel: Практика завершена
- Text: Вы сделали шаг к новой версии себя. Несите это состояние через весь день.
- Button: НАЧАТЬ СНОВА

### Lautstärke-Regler
- Oben rechts, fixiert
- Icon (🔔 / 🔉 / 🔇) + Slider

---

## Audio-Engine

- **Gong:** synthetisiert via Web Audio API (3 Oszillatoren: Bass 110Hz, Mid 220Hz, Shimmer 550Hz)
- **Ambience:** OM-Frequenz 136.1Hz Drone mit LFO während der Stille
- **Gong-Flash:** goldener radialer Gradient Fullscreen-Overlay bei jedem Übergang
- **Sprechgeschwindigkeit:** 0.78 (ElevenLabs speed parameter)
- **Pause zwischen Sätzen:** 2000ms

---

## Technische Hinweise

- Kein Framework — reines HTML/CSS/JS, eine einzige Datei

- Web Audio API für Gong und Ambient-Sound
- Keine externen Abhängigkeiten außer Google Fonts und Puter.js
- Mobile-first, funktioniert auf iPhone/Android im Browser
- API-Key und Voice IDs **niemals** in der HTML-Datei — Voice IDs sind intern, API-Key nur in `.env` für den Python-Skript
