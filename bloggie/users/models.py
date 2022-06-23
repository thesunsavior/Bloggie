from email.policy import default
from urllib import request
from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self) -> str:
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class FB_User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField()
    phoneNumber = models.TextField()
    info = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # self.user = request.user


class GG_User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField()
    occupation = models.TextField()
    info = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # self.user = request.user
