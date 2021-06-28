from django.db import models

# Create your models here.
class AddData(models.Model):
    name = models.CharField(max_length=255, default='')
    place = models.CharField(max_length=255, default='')
    disc = models.CharField(max_length=255, default='')
    image = models.FileField(max_length=255, default='')

    def __str__(self):
        return self.name
