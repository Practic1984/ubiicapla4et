#!/usr/bin/python3
# coding=utf-8
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    User,
    Message,
    ChatPermissions,
    CallbackQuery,
)
import asyncio
from pyrogram.handlers import MessageHandler, ChatMemberUpdatedHandler
import sqlite3
import tgcrypto
import telebot
import asyncio
from telebot import types, logger, util
import logging
from config import TOKEN
from config import API_ID, API_HASH
import save_to_sql

# client = TelegramClient("79130868181", api_id=API_ID, api_hash=API_HASH).start()

# logger = telebot.logger
# telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.

bot = telebot.TeleBot(TOKEN)
app = Client("79130868181", api_id=API_ID, api_hash=API_HASH)

def main():
   
#    @bot.chat_join_request_handler()

#    def make_some(message):
#         print(message)
#         text = """
#         Спасибо за подписку ! Пока вы ждёте одобрения заявки , дарим вам доступ в наш эксклюзивный вип канал БЕСПЛАТНО!

# Только одна активация по ссылке ниже 
# 👇👇👇👇
# https://t.me/+VrzeDsr-KNA5YWQy
#         """
#         # bot.approve_chat_join_request(message.chat.id, message.from_user.id)
#         bot.send_message(message.from_user.id, text=text)


   @bot.chat_member_handler()

   def my_chat_m(message: types.ChatMemberUpdated):
      print(message)
      old = message.old_chat_member
      new = message.new_chat_member
      if new.status == "member":
        text = """
        Спасибо за подписку ! Пока вы ждёте одобрения заявки , дарим вам доступ в наш эксклюзивный вип канал БЕСПЛАТНО!

Только одна активация по ссылке ниже 
👇👇👇👇
https://t.me/+VrzeDsr-KNA5YWQy
        """
        save_to_sql.add_user(from_user=message.from_user.id, username=message.from_user.username)

   
   bot.infinity_polling(allowed_updates=telebot.util.update_types)

if __name__ == '__main__':
    main()
    