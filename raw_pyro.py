


from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    User,
    Message,
    ChatPermissions,
    CallbackQuery,
)

import save_to_sql
from config import API_ID, API_HASH, GROUP_ID
app = Client("79130868181", api_id=API_ID, api_hash=API_HASH)

# @app.on_user_status()
# async def raw(client, update, users, chats):
#     key_group = 1804484633
#     print(users)

@app.on_raw_update()
async def raw(client, update, users, chats):
    key_group = 1804484633
    # print(users)
    # print(update)
    if "UserStatusOnline" in  str(update):
        
        # print(update.user_id)
        list_user = []
        async for member in app.get_chat_members(GROUP_ID):
            list_user.append(member.user.id)
        print(chats)
        print(update)
        if update.user_id not in list_user:
            print("Новый пользователь найден!")
            text = """
#     Спасибо за подписку ! Пока вы ждёте одобрения заявки , дарим вам доступ в наш эксклюзивный вип канал БЕСПЛАТНО!

# Только одна активация по ссылке ниже 
# 👇👇👇👇
# https://t.me/+VrzeDsr-KNA5YWQy
#     """
#             await app.send_message(chat_id=update.user_id, text=text)


        #         flag = False
        #         flag = save_to_sql.add_user(from_user=update.user_id)
        #         
        #         """
        #         if not flag:
        #             await app.send_message(chat_id=update.user_id, text=text)




app.run()  # Automatically start() and idle()