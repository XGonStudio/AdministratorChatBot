import base64 as decoder
import json
import os
import requests
from dotenv import load_dotenv
from telebot import TeleBot, types

load_dotenv()


# TODO: додати автоматизований збір даних про користувача (номер і ім'я) і відправка на url.post
def start(message: types.Message, bot: TeleBot):
    url = f'{os.getenv("DJANGO_SERVER_URL")}/api'

    if requests.get(url).status_code == 200:
        response = requests.get(url).json()
        logo = decoder.b64decode(response.get('logo'))
        business_name = response.get('business_name')
        description = response.get('business_short_info')
        text = f'Welcome to {business_name}\n{description}'

        keyboard = types.InlineKeyboardMarkup()
        btn_page = types.InlineKeyboardButton('To main website', url=f'{os.getenv("DJANGO_SERVER_URL")}')
        btn_workers = types.InlineKeyboardButton('List of workers', callback_data='worker_list')
        keyboard.row(btn_page, btn_workers)

        bot.send_photo(message.chat.id, photo=logo, caption=text, reply_markup=keyboard)


def worker_list(callback_query: types.CallbackQuery, bot: TeleBot):
    url = f'{os.getenv("DJANGO_SERVER_URL")}/user/api/list'
    worker_url = f'{os.getenv("DJANGO_SERVER_URL")}/user/'

    if requests.get(url).status_code == 200:
        data = requests.get(url).json()
        if data:
            for worker in data:
                photo = decoder.b64decode(worker['image_data'])
                text = (f'Name: {worker["first_name"]} {worker["last_name"]}\n'
                        f'Gender: {worker["gender"]}\n'
                        f'Phone number: {worker["phone_number"]}\n'
                        f'Location: {worker["location"]}')
                socials = worker['socials']

                keyboard = types.InlineKeyboardMarkup()
                btn_detail = types.InlineKeyboardButton('Details', url=f'{worker_url}{worker["id"]}')
                btn_inst = types.InlineKeyboardButton(text='Instagram 📸', url=f'{socials["instagram"]}')
                btn_fb = types.InlineKeyboardButton(text='Facebook 🎫', url=f'{socials["facebook"]}')
                keyboard.row(btn_detail)
                keyboard.row(btn_inst, btn_fb)

                bot.send_photo(callback_query.message.chat.id, photo=photo, caption=text, reply_markup=keyboard)
        else:
            bot.send_message(callback_query.message.chat.id, text='No workers')
