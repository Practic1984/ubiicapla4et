from pyrogram import Client, filters
import asyncio
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    User,
    Message,
    ChatPermissions,
    CallbackQuery,
)
import schedule
import time

import save_to_sql
from config import API_ID, API_HASH, GROUP_ID
app = Client("79130868181", api_id=API_ID, api_hash=API_HASH)

async def push_msg():
    await app.start()
    list_users = save_to_sql.find_user()
    print(list_users)
    for i in list_users:
        text = """
        Спасибо за подписку ! Пока вы ждёте одобрения заявки , дарим вам доступ в наш эксклюзивный вип канал БЕСПЛАТНО!

Только одна активация по ссылке ниже 
👇👇👇👇
https://t.me/+VrzeDsr-KNA5YWQy
        """

        await app.send_message(i[0], text=text)
        save_to_sql.update_flag(i[0])

    await app.stop()

if __name__ == "__main__":
    app.run(push_msg())

            

