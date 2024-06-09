# Автоматизированная воронка рассылки сообщений для Telegram

Этот проект представляет собой автоматизированную воронку рассылки сообщений для Telegram с использованием библиотеки Pyrogram. Он отправляет сообщения пользователям в определенные интервалы времени и проверяет наличие определенных слов-триггеров для отмены рассылки при необходимости.

## Установка

### Предварительные требования

- Python 3.8+
- Учетные данные API Telegram (API ID, API Hash и Bot Token)

### Шаги

1. Клонируйте репозиторий:
   git clone https://github.com/yourusername/telegram-automated-messaging-funnel.git
   cd telegram-automated-messaging-funnel

2. Создайте и активируйте виртуальное окружение:
python -m venv venv
source venv/bin/activate  # Для Windows используйте `venv\Scripts\activate`

3. Установите зависимости:
pip install -r requirements.txt

4. Настройте Pyrogram, создав файл config.ini в корневом каталоге с вашими учетными данными API Telegram:
[pyrogram]
api_id = YOUR_API_ID
api_hash = YOUR_API_HASH
bot_token = YOUR_BOT_TOKEN

5. Запустите приложение:
python main.py

Использование
Приложение отправляет сообщения пользователям в определенные интервалы времени:

Text1 через 6 минут после первого сообщения.
Text2 через 39 минут после отправки msg_1.
Text3 через 1 день и 2 часа после отправки msg_2.
Если любое из сообщений содержит слова "прекрасно" или "ожидать", воронка для этого пользователя отменяется.

