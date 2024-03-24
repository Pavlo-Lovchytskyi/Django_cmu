from django.db import models
from cloudinary.models import CloudinaryField


class Genre(models.Model):
    name = models.CharField(max_length=20, null=False, unique=True)

    def __str__(self):
        return self.name

class Game(models.Model):
    genre = models.ManyToManyField(Genre)
    name = models.CharField(max_length=25, null=False, unique=True)
    title = CloudinaryField('image')
    price = models.PositiveIntegerField(null=True)
    date_of_release = models.DateField(null=True)

    def __str__(self):
        return self.name
