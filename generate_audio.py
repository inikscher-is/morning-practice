#!/usr/bin/env python3
"""
Запуск:
  pip install requests python-dotenv
  python generate_audio.py

Erstellen Sie eine .env Datei im gleichen Ordner:
  ELEVEN_API_KEY=ihr_schlüssel_hier
"""
import requests, os, time
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
API_KEY = os.getenv("ELEVEN_API_KEY")

if not API_KEY:
    print("❌ Fehler: ELEVEN_API_KEY nicht gefunden!")
    print("   Erstellen Sie eine .env Datei mit: ELEVEN_API_KEY=ihr_schlüssel")
    exit(1)

def validate_api_key():
    r = requests.get("https://api.elevenlabs.io/v1/voices", headers={"xi-api-key": API_KEY})
    if r.status_code == 401:
        print("❌ API-Key ungültig! Bitte prüfen Sie ELEVEN_API_KEY in der .env Datei.")
        exit(1)
    elif r.status_code != 200:
        print(f"❌ API-Verbindungsfehler: {r.status_code} — {r.text[:120]}")
        exit(1)
    print("✓ API-Key gültig\n")

validate_api_key()

MARINA  = "ymDCYd8puC7gYjxIamPt"
MAXIM   = "HcaxAsrhw4ByUo4CBCBN"
MODEL   = "eleven_multilingual_v2"
OUT_DIR = "audio"

SENTENCES = {
    # ШАГ 1 — Дыхание
    "s1_marina_01": (MARINA, "Шаг первый. Дыхание."),
    "s1_marina_02": (MARINA, "Сядьте удобно."),
    "s1_marina_03": (MARINA, "Закройте глаза."),
    "s1_marina_04": (MARINA, "Сделайте вдох через нос."),
    "s1_marina_05": (MARINA, "Задержите."),
    "s1_marina_06": (MARINA, "Короткий дополнительный вдох."),
    "s1_marina_07": (MARINA, "И медленный... долгий выдох через рот."),
    "s1_marina_08": (MARINA, "Вы переключаетесь из режима стресса в режим открытости."),
    "s1_marina_09": (MARINA, "Повторяйте этот цикл."),
    "s1_maxim_01":  (MAXIM,  "Закройте глаза и сделайте несколько медленных, глубоких вздохов — чтобы расслабить разум и тело. Джо Диспенза."),
    "s1_maxim_02":  (MAXIM,  "Двойной вдох через нос, длинный выдох — и вы переключаетесь с симпатической системы на парасимпатическую. Эндрю Хаберман."),
    "s1_maxim_03":  (MAXIM,  "Я хочу отпустить. Я освобождаю. Я избавляюсь от напряжения. Луиза Хей."),

    # ШАГ 2 — Сердечная когерентность
    "s2_marina_01": (MARINA, "Шаг второй. Сердечная когерентность."),
    "s2_marina_02": (MARINA, "Перенесите всё внимание в центр груди."),
    "s2_marina_03": (MARINA, "Дышите медленно через сердце."),
    "s2_marina_04": (MARINA, "Вспомните один момент настоящей благодарности или любви."),
    "s2_marina_05": (MARINA, "Позвольте этому чувству расшириться и заполнить всю грудную клетку."),
    "s2_marina_06": (MARINA, "Удерживайте его как можно дольше."),
    "s2_maxim_01":  (MAXIM,  "Сердечная когерентность начинается с поддержания возвышенных чувств — благодарности, признательности, вдохновения, сострадания, любви и радости. Джо Диспенза."),
    "s2_maxim_02":  (MAXIM,  "Чувство — ключ. Только чувство способно войти в резонанс с окружающим миром. Грэг Брейден."),
    "s2_maxim_03":  (MAXIM,  "Мир пронизан любовью. Я люблю. И я способна вызвать ответное чувство. Луиза Хей."),

    # ШАГ 3 — Декларация
    "s3_marina_01": (MARINA, "Шаг третий. Декларация новой идентичности."),
    "s3_marina_02": (MARINA, "Вы всё ещё в состоянии сердечной когерентности."),
    "s3_marina_03": (MARINA, "Из этого тепла и открытости произнесите вслух одну сильную декларацию."),
    "s3_marina_04": (MARINA, "Не кем вы хотите стать. А кем вы уже являетесь прямо сейчас."),
    "s3_marina_05": (MARINA, "Например: Я — человек, который действует из ясности и уверенности."),
    "s3_marina_06": (MARINA, "Прочувствуйте каждое слово."),
    "s3_maxim_01":  (MAXIM,  "Создание новой реальности невозможно без создания новой личности. Снова и снова репетируйте будущее в мыслях, пока оно запечатлеется как новые нейронные связи. Джо Диспенза."),
    "s3_maxim_02":  (MAXIM,  "Фокус всегда должен быть на той личности, какой вы хотите стать. Каждое действие — это голос за того человека, которым вы хотите стать. Джеймс Клир."),
    "s3_maxim_03":  (MAXIM,  "Главное в нашей жизни — мысль. А мысль всегда можно изменить. Луиза Хей."),

    # ШАГ 4 — Защита состояния
    "s4_marina_01": (MARINA, "Шаг четвёртый. Защита состояния."),
    "s4_marina_02": (MARINA, "Представьте свой предстоящий день."),
    "s4_marina_03": (MARINA, "Первую встречу. Первый разговор."),
    "s4_marina_04": (MARINA, "Увидьте себя — уже в новом состоянии — в каждом из них."),
    "s4_marina_05": (MARINA, "Установите намерение: при любом отклонении вы возвращаетесь к себе."),
    "s4_marina_06": (MARINA, "Это ваш якорь на весь день."),
    "s4_maxim_01":  (MAXIM,  "Чем более осознанны вы к состояниям тела и ума, тем реже вы будете действовать на автопилоте. Привычная мысль уже не проскользнёт незамеченной. Джо Диспенза."),
    "s4_maxim_02":  (MAXIM,  "Всегда говорите да текущему мгновению. Скажите жизни да — и вы увидите, как она начнёт работать на вас. Экхарт Толле."),
    "s4_maxim_03":  (MAXIM,  "Никогда не пропускайте действие дважды. Если пропустили один день — вернитесь как можно скорее. Джеймс Клир."),

    # ШАГ 5 — Поиск подтверждений
    "s5_marina_01": (MARINA, "Шаг пятый. Поиск подтверждений."),
    "s5_marina_02": (MARINA, "Активируйте режим поиска."),
    "s5_marina_03": (MARINA, "Сегодня вы будете замечать всё, что подтверждает вашу новую идентичность."),
    "s5_marina_04": (MARINA, "Каждое маленькое доказательство — это подпитка."),
    "s5_marina_05": (MARINA, "Мозг начинает видеть то, во что вы верите."),
    "s5_marina_06": (MARINA, "Завершите практику тремя словами благодарности за сегодняшний день."),
    "s5_maxim_01":  (MAXIM,  "Испытывая благодарность, мы сигнализируем, что событие уже произошло. Нужно чувствовать себя так, словно то, чего мы хотим, уже присутствует в нашей жизни. Джо Диспенза."),
    "s5_maxim_02":  (MAXIM,  "Вы в своей жизни видите главным образом то, во что верите. Уэйн Дайер."),
    "s5_maxim_03":  (MAXIM,  "Меняя то, что происходит внутри нас — мысли, чувства и убеждения — мы меняем и окружающий мир. Грэг Брейден."),

    # Финал
    "finish_01":    (MARINA, "Практика завершена."),
    "finish_02":    (MARINA, "Вы сделали шаг к новой версии себя."),
    "finish_03":    (MARINA, "Несите это состояние через весь день."),
}

def generate(file_id, voice_id, text):
    path = os.path.join(OUT_DIR, f"{file_id}.mp3")
    if os.path.exists(path):
        print(f"  ✓ уже есть: {file_id}")
        return True
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {"xi-api-key": API_KEY, "Content-Type": "application/json"}
    body = {
        "text": text,
        "model_id": MODEL,
        "voice_settings": {
            "stability": 0.78,
            "similarity_boost": 0.85,
            "style": 0.15,
            "speed": 0.78
        }
    }
    r = requests.post(url, headers=headers, json=body)
    if r.status_code == 200:
        with open(path, "wb") as f:
            f.write(r.content)
        print(f"  ✓ {file_id}  ({len(r.content)//1024} kb)")
        return True
    else:
        print(f"  ✗ {file_id}: {r.status_code} — {r.text[:120]}")
        return False

if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    total = len(SENTENCES)
    ok = 0
    print(f"Генерируем {total} файлов...\n")
    for i, (fid, (voice, text)) in enumerate(SENTENCES.items()):
        print(f"[{i+1}/{total}]", end=" ")
        if generate(fid, voice, text):
            ok += 1
        time.sleep(0.4)
    print(f"\n{'='*40}")
    print(f"Готово: {ok}/{total} файлов в папке ./{OUT_DIR}/")