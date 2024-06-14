import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackContext, MessageHandler, filters
import aiohttp
from instances import phrazes, buttons
from random import randint

TELEGRAM_TOKEN = '7317734081:AAE64GtnGTvz54ZbI60qRQO0xGdmc37tKl8'


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def get_rasa_response(message: str) -> str:
    rasa_url = "http://localhost:5005/webhooks/rest/webhook"
    payload = {
        "sender": "telegram_user",
        "message": message
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(rasa_url, json=payload) as response:
            response_data = await response.json(encoding='utf-8')
            print(f'{response_data=}')
            result = [resp.get("text") for resp in response_data] if response_data else ["Извините, я вас не понял."]

            print(f'{result=}')

            return result



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=phrazes.get('start'))
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=phrazes.get('start_tails')[randint(0, len(phrazes.get('start_tails'))-1)],
                                   reply_markup=keyboard)


# Функция для обработки сообщений
async def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    rasa_responses = await get_rasa_response(user_message)
    for response in rasa_responses:
        await update.message.reply_text(response)


if __name__ == '__main__':
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()