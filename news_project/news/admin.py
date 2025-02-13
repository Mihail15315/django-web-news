from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import News, Author
from django.contrib.gis import forms
from .models import NotablePlace, WeatherReport
from mapwidgets.widgets import GoogleMapPointFieldWidget
from leaflet.admin import LeafletGeoAdmin 
# admin.site.register(News)
from django.contrib.gis.db import models  # Импортируйте GIS модели
admin.site.register(Author)

@admin.register(News)
class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)  # Указываем, что поле content будет использовать Summernote
    list_display = ('title', 'main_image', 'preview_image', 'publication_date', 'author')
    search_fields = ('title',)
class NotablePlaceAdmin(LeafletGeoAdmin):
    list_display = ('name', 'coordinates', 'rating')
    search_fields = ('name',)
    list_filter = ('rating',)
@admin.register(WeatherReport)
class WeatherReportAdmin(admin.ModelAdmin):
    list_display = ('place', 'temperature', 'humidity', 'pressure', 'wind_direction', 'wind_speed', 'timestamp')
    list_filter = ('place', 'timestamp')
    search_fields = ('place__name',)
    readonly_fields = ('place', 'temperature', 'humidity', 'pressure', 'wind_direction', 'wind_speed', 'timestamp')
admin.site.register(NotablePlace, NotablePlaceAdmin)