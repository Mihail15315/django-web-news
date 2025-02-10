from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet, news_list, news_detail
from . import views
from .views import edit_place
from .views import upload_file

router = DefaultRouter()
router.register(r'news', NewsViewSet)
urlpatterns = [
    path('upload/', upload_file, name='upload_file'),
    path('', include(router.urls)),
    path('list/', news_list, name='news_list'),  # Добавляем маршрут для списка новостей
    path('<int:news_id>/', news_detail, name='news_detail'),
    path('index/', views.index, name='index'),
    path('places/<int:pk>/edit/', edit_place, name='edit_place'),
]