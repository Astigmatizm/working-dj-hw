from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from PIL import Image
import os


class Record(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class IceCream(models.Model):
    name = models.CharField(max_length=100)
    flavor = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


# class Document(models.Model):
#     title = models.CharField(max_length=100)
#     file = models.FileField(upload_to='documents/')  # Сохраняем файлы в папке "documents"
#     uploaded_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title
#


class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)

    def __str__(self):
        return self.image.name


@receiver(pre_save, sender=ImageModel)
def create_thumbnail(sender, instance, **kwargs):
    if instance.image:
        image_path = instance.image.path  # Путь к оригинальному изображению
        image = Image.open(image_path)

        # Создание миниатюры
        thumbnail_size = (128, 128)
        image.thumbnail(thumbnail_size)

        # Формируем путь для сохранения миниатюры
        thumbnail_dir = os.path.join(os.path.dirname(image_path), 'thumbnails')
        if not os.path.exists(thumbnail_dir):
            os.makedirs(thumbnail_dir)

        thumbnail_path = os.path.join(thumbnail_dir, f"{os.path.basename(image_path)}_thumbnail.jpg")

        # Сохраняем миниатюру в файл
        image.save(thumbnail_path, 'JPEG')

        # Сохраняем путь к миниатюре в поле модели
        instance.thumbnail = os.path.relpath(thumbnail_path, start=os.getcwd())
