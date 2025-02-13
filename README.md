# Django Web News
Этот проект представляет собой веб-приложение новостей, разработанное с использованием Django. Приложение позволяет просматривать, изменять и удалять новости.
## Установка
Следуйте этим шагам, чтобы установить проект на вашем локальном компьютере:
1. **Клонируйте репозиторий**
   Откройте терминал и выполните следующую команду: 
bash
   git clone https://github.com/Mihail15315/django-web-news.git
2. **Перейдите в каталог проекта**   
bash
   cd django-web-news
3. **Создайте виртуальное окружение (рекомендуется)**  
bash
   python -m venv venv
   source venv/bin/activate  # Для Linux/Mac
   venv\Scripts\activate  # Для Windows
4. **Установите зависимости**
Убедитесь, что у вас установлен pip, затем выполните:
bash
   pip install -r requirements.txt
5. **Настройте базу данных**
   Примените миграции для настройки базы данных:
bash
   python manage.py migrate
6. **Создайте файл .env**
   Создайте файл .env в корне проекта и добавьте необходимые переменные окружения. Пример содержимого: 
   EMAIL_HOST_PASSWORD=your_email_password_here
7. **Запустите сервер**
   После завершения всех настроек вы можете запустить сервер разработки:
bash
   python manage.py runserver
8. **Откройте приложение в браузере**
   Перейдите по адресу (http://127.0.0.1:8000) в вашем браузере, чтобы увидеть приложение.
## Как использовать приложение
- (http://127.0.0.1:8000/news/) **Просмотр новостей в виде API**: Вы можете просматривать список всех доступных новостей, а также добавлять, изменять и удалять, используя drf API.
- (http://127.0.0.1:8000/list/) **Просмотр новостей в виде HTML**: Вы можете просматривать список всех доступных новостей, в удобочитаемом для пользователя виде (HTML,CSS).
- (http://127.0.0.1:8000/admin/) **Админ-панель**: Админ может добавить, изменить и удалить новость или автора новости.
- (http://127.0.0.1:8000/admin/constance/config/) **Рассылка на почту**: Админ может настроить время отправки, почту получателей, заголовок и описание новостей на почту.
## Выполнение периодической задачи на получение Сводки погоды 
- **Перейдите на адрес http://localhost:8000/admin/news/notableplace/**: Убедитесь что у вас есть Примечательные места.
- - **Перейдите на адрес http://localhost:8000/admin/django_celery_beat/periodictask/**: Поменяйте время через которое API будет собирать сводку о погоде по вашим Примечательным местам.
- **Убедитесь что вы запустили Redis**
- **Откройте два терминала по адресу .../django-web-news/news_project**: В первом введите: celery -A news_project worker --loglevel=info а во втором: celery -A news_project beat -l info.
- **Откройте файл .env**: И поменяйте api c сайта https://home.openweathermap.org/api_keys на ваш собственный.
- **Перейдите на адрес http://localhost:8000/admin/news/weatherreport/**: И убедитесь что сводка собрана, также вы можете фильтровать по дате и по местам.
### Страница настройки сбора данных о погоде
![](https://github.com/Mihail15315/django-web-news/blob/weather/periodictask.png)
### Страница сводки данных о погоде
![](https://github.com/Mihail15315/django-web-news/blob/weather/weatherreport.png)
