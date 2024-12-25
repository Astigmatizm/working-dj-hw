from django.db import models


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


class Document(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents/')  # Сохраняем файлы в папке "documents"
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title