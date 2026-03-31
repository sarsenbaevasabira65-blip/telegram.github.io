# 🤖 AI Creative Services Bot — Баптау нұсқаулығы
`BOT_TOKEN = "8754227384:AAFlaA-7Bq6wVR8wVAOZqUwY86bCjJuJG4k"`
`ADMIN_ID = 1313252587`
KASPI_NUMBER = "+7 7474513371"  
KASPI_NAME   = "Сабира С"

## 4. Бағаларды өзгерту
`SERVICES` сөздігінде әр қызмет үшін:
- `price_kz` / `price_ru` — баға
- `time_kz` / `time_ru` — орындалу уақыты
- `desc_kz` / `desc_ru` — сипаттама

## 5. Орнату және іске қосу

```bash
# Python орнатылған болуы керек (3.10+)

# Кітапханаларды орнату
pip install -r requirements.txt

# Ботты іске қосу
python bot.py
```

## 6. Серверде іске қосу (24/7)
VPS сервер немесе Railway.app / Render.com сайтында безплатно іске қосуға болады.

### Railway.app (тегін):
1. https://railway.app тіркелу
2. GitHub-қа файлдарды жүктеу
3. New Project → Deploy from GitHub
4. Environment Variable: `BOT_TOKEN` қосу

## Ботты функционалы:
- ✅ Қазақ / орыс тілдері
- ✅ 6 қызмет: фото, видео, анимация, шақыру, дауыс, ән
- ✅ Баға + уақыт ақпараты
- ✅ Kaspi төлем нұсқаулығы
- ✅ Скриншотты adminге жіберу
- ✅ Менеджерге хабарласу
