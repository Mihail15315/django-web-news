import os
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django_summernote.fields import SummernoteTextField
import bleach

def clean_html(html):
    return bleach.clean(html, strip=True)


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=255)
    main_image = models.ImageField(upload_to='news_images/')
    preview_image = models.ImageField(upload_to='news_images/preview/', blank=True)
    text = SummernoteTextField(null=True)
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.text = clean_html(self.text)
        super().save(*args, **kwargs)

        # Генерация превью-изображения
        if not self.preview_image:
            img = Image.open(self.main_image.path)
            print(self.main_image.path)
            img.thumbnail((200, 200))
            preview_path = self.main_image.path.replace('news_images\\', 'news_images\\preview\\')
            print(preview_path)
            img.save(preview_path)
            self.preview_image = preview_path
        self.text = clean_html(self.text)
        super().save(update_fields=['preview_image'])

    def __str__(self):
        return self.title