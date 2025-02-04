import os
import django
from django.conf import settings
from celery.schedules import crontab
from celery import Celery
from constance import config
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_project.settings')
django.setup()
app = Celery('news_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'send-daily-news-email': {
        'task': 'news.send_email_task',
        'schedule': crontab(hour=int(config.EMAIL_SEND_TIME.split(':')[0]), 
                            minute=int(config.EMAIL_SEND_TIME.split(':')[1])),
    },
}  