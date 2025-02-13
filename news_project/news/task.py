from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
# from .models import News
from constance import config
from django.apps import apps
import os
email_host_user = os.getenv('EMAIL_HOST_USER')
api = os.getenv('EMAIL_HOST_USER')
API_KEY = os.getenv('API_KEY')  # Замените на ваш ключ
from .models import NotablePlace, WeatherReport
import requests
import random
@shared_task(name='news.send_email_task')
def send_email_task():
    News = apps.get_model('news', 'News')
    # Получаем текущую дату
    today = timezone.now().date()
    
    # Получаем новости, опубликованные сегодня
    news_today = News.objects.filter(publication_date__date=today)

    if news_today.exists():
        recipients = config.EMAIL_RECIPIENTS.split(',')
        subject = config.EMAIL_SUBJECT
        body = config.EMAIL_BODY + '\n\n' + '\n'.join([f"{news.title}: {news.text}" for news in news_today])

        send_mail(subject, body, email_host_user, recipients)
@shared_task
def fetch_weather_reports():
    places = NotablePlace.objects.all()
    # lat = 35.6895  # Пример: широта Токио
    # lon = 139.6917  # Пример: долгота Токио
    for place in places:
        lat, lon = place.coordinates.y, place.coordinates.x
        url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
        # Проверка наличия нужных ключей в ответе
        if 'main' in data and 'wind' in data:
            weather_data = {
                'temperature': data['main']['temp'],  # Температура
                'humidity': data['main']['humidity'],  # Влажность
                'pressure': data['main']['pressure'],  # Давление
                'wind_direction': data['wind']['deg'],  # Направление ветра
                'wind_speed': data['wind']['speed'],  # Скорость ветра
            }

            # # Сохранение данных в базу
            WeatherReport.objects.create(
            place=place,
            temperature=weather_data['temperature'],
            humidity=weather_data['humidity'],
            pressure=weather_data['pressure'],
            wind_direction=weather_data['wind_direction'],
            wind_speed=weather_data['wind_speed'],
            )
        else:
            print("Ошибка: отсутствуют необходимые данные в ответе.")
            print(data)  # Выводим полные данные для отладки
            print(f"Ошибка при запросе к API: {response.status_code}")
            print(response.json())  # Выводим ответ для отладки