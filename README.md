# TelegramProfileWeather
Данный репозиторий отображает текущую погоду в Екатеринбурге в описании вашего Telegram аккаунта.
### Примеры
![снег](screenshots/image1.png)

![ночь](screenshots/image2.png)
### Установка
Указать в файле [app/config.py](app/config.py) свои токены 

**Обычная**

`pip install -r requirements.txt`

`cd app`

`python main.py`

**Docker**

`docker build -t telegram_profile_weather .`

`docker run TelegramProfileWeather`
