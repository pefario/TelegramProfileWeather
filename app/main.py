from pyowm import OWM
from pytz import timezone
from datetime import datetime
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
import asyncio
from config import *

owm = OWM(weather_token)
mgr = owm.weather_manager()

telegram_client = TelegramClient('TelegramProfileWeather', telegram_id, telegram_hash)
telegram_client.start()

emojis = {
    'clouds': '☁️',
    'clear': '☀️',
    'snow': '❄️',
    'rain': '🌧'
}


async def update_description():
    """Добавляем информацию о погоде в описание пользователя"""
    while True:
        observation = mgr.weather_at_place('Ekaterinburg')
        weather = observation.weather
        description = f'Сейчас в Екатеринбурге {weather.temperature("celsius")["temp"]} '

        current_time = datetime.now(timezone('Asia/Yekaterinburg'))
        if current_time.hour <= 6 or current_time.hour >= 22:
            description += '🌙'
        else:
            description += emojis.get(weather.status.lower(), '🌆')

        await telegram_client(UpdateProfileRequest(about=description))
        await asyncio.sleep(3600)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(update_description())
