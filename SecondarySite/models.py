from django.db import models

class Announcement(models.Model):
    title = models.CharField(max_length=50)
    appearance = models.TextField(null=True, blank=True)
    breed = models.TextField(null=True, blank=True)
    status = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)