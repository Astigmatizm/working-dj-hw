from django.db import models
from django.core.exceptions import ValidationError

class Roditel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_id_and_name(self):
        return f"ID: {self.id}, Имя: {self.first_name} {self.last_name}"

class Child(models.Model):
    person = models.OneToOneField(Roditel, on_delete=models.CASCADE)
    parent = models.ForeignKey(Roditel, related_name='children', on_delete=models.CASCADE)
    school_name = models.CharField(max_length=200)
    grade = models.PositiveIntegerField()

    def __str__(self):
        return f"Ребёнок {self.person.first_name} {self.person.last_name}, школа: {self.school_name}, класс: {self.grade}"

    def get_id_and_school_grade(self):
        return f'ID: {self.id}, Школа: {self.school_name}, Класс: {self.grade}'

class IceCream(models.Model):
    flavor = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_gluten_free = models.BooleanField(default=False)
    description = models.TextField()
    available_in_kiosks = models.ManyToManyField('IceCreamKiosk', related_name='available_ice_creams')

    def __str__(self):
        return self.flavor
    def get_id_and_flavor(self):
        return f"ID: {self.id}, Вкус: {self.flavor}"
    def get_total_price_in_kiosks(self):
        total_price = 0
        for kiosk in self.available_in_kiosks.all():
            total_price += self.price
        return total_price
    def positive_number_validator(value):
        if value < 0:
            raise ValidationError(f"Значение должно быть положительным или равно 0, но получено: {value}")


class IceCreamKiosk(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    ice_creams = models.ManyToManyField(IceCream, related_name='kiosks')

    def __str__(self):
        return self.name

# models.py
class Announcement(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
