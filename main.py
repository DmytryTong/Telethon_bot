from TelegrammBot import TelegramBot
from dotenv import load_dotenv
import os

# Завантажити змінні оточення з файлу .env
load_dotenv()

# Використовувати змінні оточення
api_key = os.getenv("API_KEY")
db_host = os.getenv("DB_HOST")

def get_api_credentials():
    # Введіть ваші API ID та API Hash тут
    api_id = os.getenv("API_ID")
    api_hash = os.getenv("API_HASH")
    return api_id, api_hash


if __name__ == '__main__':
    api_id, api_hash = get_api_credentials()
    session_file = 'session.session'
    bot = TelegramBot(api_id, api_hash, session_file)
    bot.create_telegram_bot()
