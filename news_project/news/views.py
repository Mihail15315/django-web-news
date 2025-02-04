from django.shortcuts import render, get_object_or_404
import requests
from rest_framework import viewsets
from .models import News
from .serializers import NewsSerializer
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def index(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        send_mail(
        name,
        message,
        settings.EMAIL_HOST_USER,
        ['mihailbaranov780@gmail.com'],
        fail_silently=False,
        )
        return HttpResponse("Message sent successfully!")

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
def news_list(request):
    response = requests.get('http://127.0.0.1:8000/api/v1/news/')
    news_items = response.json() if response.status_code == 200 else []
    return render(request, 'news/news_list.html', {'news_items': news_items})

def news_detail(request, news_id):
    news_item = get_object_or_404(News, id=news_id)
    return render(request, 'news/news_detail.html', {'news_item': news_item})