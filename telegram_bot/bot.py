import telebot
from django_config import settings


admin_bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)