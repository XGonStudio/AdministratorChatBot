import os
import telebot
from dotenv import load_dotenv
import commands


load_dotenv()


admin_bot = telebot.TeleBot(os.getenv('TELEGRAM_TOKEN'))


def handle_errors(bot, error_message):
    def decorator(func):
        def wrapper(message, *args, **kwargs):
            try:
                return func(message, *args, **kwargs)
            except Exception as e:
                print(type(e).__name__, e)
                if isinstance(message, telebot.types.CallbackQuery):
                    bot.send_message(message.message.chat.id, error_message)
                else:
                    bot.send_message(message.chat.id, error_message)
        return wrapper
    return decorator


@admin_bot.message_handler(commands=['start'])
@handle_errors(admin_bot, 'Sorry, on server side something went wrong')
def get_start(message):
    commands.start(message, admin_bot)


@admin_bot.callback_query_handler(func=lambda call: call.data == 'worker_list')
@handle_errors(admin_bot, 'Sorry, on server side something went wrong')
def get_worker_list(callback_query):
    commands.worker_list(callback_query, admin_bot)


admin_bot.polling()
