from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
# from .models import News
from constance import config
from django.apps import apps
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

        send_mail(subject, body, 'mihailbaranov16072002@gmail.com', recipients)
