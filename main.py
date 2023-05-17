

from TelegrammBot import TelegramBot


def get_api_credentials():
    # Введіть ваші API ID та API Hash тут
    api_id = '21304077'
    api_hash = 'eee634d8a5f1bf36d0b5117568180a26'
    return api_id, api_hash


if __name__ == '__main__':
    api_id, api_hash = get_api_credentials()
    session_file = 'session.session'
    bot = TelegramBot(api_id, api_hash, session_file)
    bot.create_telegram_bot()
