"""
Django settings for news_project project.

Generated by 'django-admin startproject' using Django 5.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
from decouple import config
from pathlib import Path
from celery.schedules import crontab
CELERY_BROKER_URL = 'redis://localhost:6379/0'

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
CONSTANCE_CONFIG = {
    'EMAIL_RECIPIENTS': ('mihailbaranov780@gmail.com', 'Comma-separated list of email recipients'),
    'EMAIL_SUBJECT': ('Daily News Update', 'Subject of the email'),
    'EMAIL_BODY': ('Here are the news published today.', 'Body of the email'),
    'EMAIL_SEND_TIME': ('08:00', 'Time to send the email in HH:MM format'),
}

# CELERY_BEAT_SCHEDULE = {
#     'send-daily-news-email': {
#         'task': 'news.tasks.send_daily_news_email',
#         'schedule': crontab(hour=17, minute=17),  # Отправка каждый день в 08:00
#     },
# }

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
SUMMERNOTE_THEME = 'bs4'




# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_ul49fm8s(c@$mm5fm*9^j9t#6qs1#io142knzzu1xzpbqpi+)'

# SECURITY WARNING: don't run with debug turned on in production!


ALLOWED_HOSTS = []


# CONSTANCE_CONFIG = {
#     'EMAIL_RECIPIENTS': ('misha151615@yandex.ru', 'Список адресатов через запятую'),
#     'EMAIL_SUBJECT': ('Новости', 'Тема сообщения'),
#     'EMAIL_BODY': ('Сегодня опубликованы следующие новости...', 'Текст сообщения'),
#     'EMAIL_SEND_TIME': ('10:37', 'Время отправки в формате HH:MM'),
# }

   
# Application definition

INSTALLED_APPS = [
    'constance',
    'constance.backends.database',
    'django.contrib.sites',  # необходим для django-summernote
    'django_summernote',
    'rest_framework',
    'news',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
SITE_ID = 1
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'news_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'news_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DEBUG = True
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 465
EMAIL_HOST_USER = "mihailbaranov16072002@gmail.com"
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_SSL = True
DEBUG = True
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# SERVER_EMAIL = EMAIL_HOST_USER
# EMAIL_ADMIN = EMAIL_HOST_USER
