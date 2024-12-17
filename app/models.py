from django.db import models

class Roditel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Child(models.Model):
    person = models.OneToOneField(Roditel, on_delete=models.CASCADE)
    parent = models.ForeignKey(Roditel, related_name='children', on_delete=models.CASCADE)
    school_name = models.CharField(max_length=200)
    grade = models.PositiveIntegerField()

    def __str__(self):
        return f"Ребёнок {self.person.first_name} {self.person.last_name}, школа: {self.school_name}, класс: {self.grade}"

class IceCream(models.Model):
    flavor = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_gluten_free = models.BooleanField(default=False)
    description = models.TextField()
    available_in_kiosks = models.ManyToManyField('IceCreamKiosk', related_name='available_ice_creams')

    def __str__(self):
        return self.flavor


class IceCreamKiosk(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    ice_creams = models.ManyToManyField(IceCream, related_name='kiosks')

    def __str__(self):
        return self.name
