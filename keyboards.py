from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import link_chat

def start_keyboard():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton(text="Выберете ответ", callback_data='reg_now')
    )
    return markup
