import os
from pathlib import Path

from telebot import TeleBot, types
from server_app.main import info


def path_to_photo(filename):
    return Path(__file__).resolve().parent.parent/'server_app'/'static'/'media'/'photos'/filename


def start(message: types.Message, bot: TeleBot):
    photo = open(f'{path_to_photo(info.MAIN_PHOTO_NAME)}', 'rb')
    start_txt = f'Welcome to {info.NAME_OF_BUSINESS}\n{info.MAIN_DESCRIPTION}'

    keyboard = types.InlineKeyboardMarkup()
    btn_page = types.InlineKeyboardButton('To main website', url=info.MAIN_WEBPAGE_URL)
    keyboard.row(btn_page)

    bot.send_photo(message.chat.id, photo=photo, caption=start_txt, reply_markup=keyboard)


# TODO func must return in chat messages with photo and description of every worker with 2 buttons: 1. to full worker
#  info, 2. to page with event form
def get_worker_list(call):
    pass
