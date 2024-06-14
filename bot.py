import logging
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests

# Вставьте ваш токен сюда
TELEGRAM_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# Логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Функция для команды /start
def start(update: Update, _: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )

# Функция для обработки сообщений
def handle_message(update: Update, _: CallbackContext) -> None:
    user_message = update.message.text
    rasa_response = get_rasa_response(user_message)
    update.message.reply_text(rasa_response)

# Функция для получения ответа от Rasa
def get_rasa_response(message: str) -> str:
    rasa_url = "http://localhost:5005/webhooks/rest/webhook"
    payload = {
        "sender": "telegram_user",
        "message": message
    }
    response = requests.post(rasa_url, json=payload)
    response_data = response.json()
    if response_data:
        return response_data[0].get("text", "Sorry, I didn't understand that.")
    return "Sorry, I didn't understand that."

def main() -> None:
    # Создаем Updater и передаем ему токен бота.
    updater = Updater(TELEGRAM_TOKEN)

    # Получаем диспетчер для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Регистрируем обработчики команд
    dispatcher.add_handler(CommandHandler("start", start))

    # Регистрируем обработчики сообщений
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
