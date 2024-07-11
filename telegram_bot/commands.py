from telebot import types
from .bot import admin_bot
from ..main import info


@admin_bot.message_handler(commands='start')
def start(message):
    photo = open(f'static/media/photos/{info.MAIN_PHOTO_NAME}', 'rb')
    start_txt = f'Welcome to {info.NAME_OF_BUSINESS}\n{info.MAIN_DESCRIPTION}'
    keyboard = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton(text='To main website', url=info.MAIN_WEBPAGE_URL)
    b2 = types.InlineKeyboardButton(text='Get all workers', callback_data='get_worker_list')
    keyboard.add(b1, b2)

    admin_bot.send_photo(message.chat.id, photo=photo, caption=start_txt, reply_markup=keyboard)


# TODO func must return in chat messages with photo and description of every worker with 2 buttons: 1. to full worker
#  info, 2. to page with event form
@admin_bot.callback_query_handlers(func=lambda call: call.data == 'get_worker_list')
def get_worker_list(call):
    pass
