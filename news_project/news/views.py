from django.shortcuts import render, get_object_or_404
import requests
from rest_framework import viewsets
from .models import News
from .serializers import NewsSerializer
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .forms import UploadFileForm
from django.contrib.gis.geos import Point
import openpyxl

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

from django.shortcuts import redirect
from .forms import NotablePlaceForm
from .models import NotablePlace

def edit_place(request, pk):
    place = get_object_or_404(NotablePlace, pk=pk)
    if request.method == 'POST':
        form = NotablePlaceForm(request.POST, instance=place)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/admin/news/notableplace/')
    else:
        form = NotablePlaceForm(instance=place)
    return render(request, 'news/notableplace/change_form.html', {
    'form': form,
    'original': place,  # Передаем объект, который редактируется
    'opts': NotablePlace._meta,  # Передаем метаданные модели
})
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            workbook = openpyxl.load_workbook(file)
            sheet = workbook.active

            for row in sheet.iter_rows(min_row=2, values_only=True):  # Пропускаем заголовок
                name, coordinates, rating = row
                latitude, longitude = map(float, coordinates.split(','))
                point = Point(longitude, latitude)
                NotablePlace.objects.create(
                    name=name,
                    coordinates=point,
                    rating=rating,
                )
            return render(request, 'places/upload_success.html')
    else:
        form = UploadFileForm()
    return render(request, 'places/upload.html', {'form': form})