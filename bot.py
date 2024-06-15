import logging
from typing import Tuple, Union, List, Optional

from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackContext, MessageHandler, filters, CallbackQueryHandler
import aiohttp
from instances import phrazes, buttons, buttons_taxation, buttons_setup_company
from random import randint
from itertools import zip_longest
from helpers import get_keyboard_from_json, get_random_object, get_inline_keyboard_from_json, find_values_by_titles, get_title_by_payload


TELEGRAM_TOKEN = '7317734081:AAE64GtnGTvz54ZbI60qRQO0xGdmc37tKl8'


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def get_rasa_response(message: str) -> Tuple[Union[list, List[str]], Optional[list]]:
    rasa_url = "http://localhost:5005/webhooks/rest/webhook"
    payload = {
        "sender": "telegram_user",
        "message": message
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(rasa_url, json=payload) as response:
            response_data = await response.json(encoding='utf-8')
            print(f'{response_data=}')
            text = [resp.get("text") for resp in response_data] if response_data else ["Извините, я вас не понял."]
            buttons = [resp.get("buttons") for resp in response_data] if response_data else None
            combined_responses = list(zip_longest(*[text, buttons], fillvalue=None))
            return combined_responses


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=phrazes.get('start'))
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=get_random_object(phrazes.get('start_tails')),
                                   reply_markup=keyboard)


# Функция для обработки сообщений
async def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    rasa_responses = await get_rasa_response(user_message)
    for response, buttons in rasa_responses:
        keyboard = None
        if buttons:
            print(f'------ {buttons=}')
            if find_values_by_titles(buttons, ['Типы компаний', 'Стать налоговым резидентом Кипра']):
                buttons = get_inline_keyboard_from_json(buttons)
                keyboard = InlineKeyboardMarkup(buttons)
            else:
                buttons = get_keyboard_from_json(buttons)
                keyboard = ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)
        print(f'{keyboard=}')
        await update.message.reply_text(response, reply_markup=keyboard)


# Функция для обработки нажатий на кнопки
async def handle_callback_query(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    print(f'{query.message.reply_markup.inline_keyboard=}')
    buttons = query.message.reply_markup.inline_keyboard
    print(f'----- {buttons=}')
    result = get_title_by_payload(buttons, query.data)
    response_text = f"Вы выбрали тему: {result}"
    await query.message.reply_text(response_text)



if __name__ == '__main__':
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    start_handler = CommandHandler('start', start)
    message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    callback_query_handler = CallbackQueryHandler(handle_callback_query)

    application.add_handler(start_handler)
    application.add_handler(message_handler)
    application.add_handler(callback_query_handler)

    application.run_polling()