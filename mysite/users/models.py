from django.contrib.auth.models import User
from django.db import models

from cloudinary.models import CloudinaryField

from games.models import Game




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = CloudinaryField('image')
    game = models.ManyToManyField(Game)

    def __str__(self):
        return self.user.username


