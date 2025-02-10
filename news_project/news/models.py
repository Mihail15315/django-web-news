import os
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django_summernote.fields import SummernoteTextField
import bleach
from django.contrib.gis.db import models
from django.core.files.base import ContentFile
from django.core.validators import MaxValueValidator, MinValueValidator

def clean_html(html):
    return bleach.clean(html, strip=True)
    
class NotablePlace(models.Model):
    name = models.CharField(max_length=255)
    coordinates = models.PointField()  # Используем PointField для хранения координат
    rating = models.PositiveIntegerField(
        validators=[
            MinValueValidator(0),   # Минимальное значение 0
            MaxValueValidator(25)    # Максимальное значение 25
        ]
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Примечательное место"
        verbose_name_plural = "Примечательные места"
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
            img.thumbnail((200, 200))

            # Создаем временный файл для превью
            from io import BytesIO
            temp_file = BytesIO()
            img.save(temp_file, format='JPEG')
            temp_file.seek(0)

            # Сохраняем превью в поле preview_image
            self.preview_image.save(
                os.path.basename(self.main_image.name),  # Имя файла
                ContentFile(temp_file.read()),  # Содержимое файла
                save=False  # Не сохранять модель, чтобы избежать рекурсии
            )
            temp_file.close()

        super().save(update_fields=['preview_image'])

    def __str__(self):
        return self.title