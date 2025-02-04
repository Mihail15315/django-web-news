from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import News, Author

# admin.site.register(News)
admin.site.register(Author)

@admin.register(News)
class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)  # Указываем, что поле content будет использовать Summernote
    list_display = ('title', 'main_image', 'preview_image', 'publication_date', 'author')
    search_fields = ('title',)
