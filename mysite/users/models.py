from django.contrib.auth.models import User
from django.db import models

from cloudinary.models import CloudinaryField

from games.models import Game




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = CloudinaryField('image')
    birthday = models.DateField(null=False)
    country = models.CharField(max_length=10, null=False)
    email = models.EmailField(null=False)
    game = models.ManyToManyField(Game)

    def __str__(self):
        return self.user.username


