from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet, news_list, news_detail
from . import views

router = DefaultRouter()
router.register(r'news', NewsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('list/', news_list, name='news_list'),  # Добавляем маршрут для списка новостей
    path('<int:news_id>/', news_detail, name='news_detail'),
    path('index/', views.index, name='index'),
]