from pyrogram import Client
import asyncio
from database import session
from models import User, MessageLog

app = Client("my_account")

# Функция отправки сообщений
async def send_message(user_id, text):
    async with app:
        await app.send_message(user_id, text)
        log_message(user_id, text)

# Логирование отправленных сообщений
def log_message(user_id, text):
    new_log = MessageLog(user_id=user_id, message_text=text)
    session.add(new_log)
    session.commit()

# Проверка наличия триггеров в тексте
def check_triggers(text):
    triggers = ["прекрасно", "ожидать"]
    for trigger in triggers:
        if trigger in text:
            return True
    return False

# Основная функция для обработки воронки
async def message_funnel():
    while True:
        users = session.query(User).filter(User.status == 'alive').all()
        for user in users:
            logs = session.query(MessageLog).filter(MessageLog.user_id == user.id).all()
            if not logs:
                await send_message(user.id, "Текст1")
                await asyncio.sleep(6 * 60)  # 6 минут
            elif len(logs) == 1 and not check_triggers(logs[0].message_text):
                await send_message(user.id, "Текст2")
                await asyncio.sleep(39 * 60)  # 39 минут
            elif len(logs) == 2 and not check_triggers(logs[1].message_text):
                await send_message(user.id, "Текст3")
                await asyncio.sleep((1 * 24 * 60 * 60) + (2 * 60 * 60))  # 1 день 2 часа
            else:
                user.status = 'finished'
                session.commit()
                continue
            if check_triggers(logs[-1].message_text):
                user.status = 'finished'
                session.commit()
        await asyncio.sleep(60)  # Проверка каждую минуту