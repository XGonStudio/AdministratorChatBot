import os
import telebot
from telegram_bot.commands import *
from dotenv import load_dotenv


load_dotenv()

admin_bot = telebot.TeleBot(os.getenv('TELEGRAM_TOKEN'))
admin_bot.register_message_handler(start, commands=['start'], pass_bot=True)

admin_bot.polling()
