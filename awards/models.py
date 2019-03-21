from django.db import models
from time import timezone
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
import PIL
import datetime as dt
from PIL import Image
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    image = models.ImageField(default='download.png',
                              upload_to='profile_pics/')

    def __str__(self):
        return f'{self.user.username}Profile'

    def save(self):
        super().save()

        img = PIL.Image.open(self.image.path)

        if img.height > 200 or img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def delete_profile(self):
        self.delete()


class Image(models.Model):
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(max_length=500, blank=True)
    link = models.CharField(max_length=50, blank=True)
    pub_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.description

    def save_image(self):
        self.save

    def set_description(self, new_description):
        self.description = new_description
        self.save

    @classmethod
    def search_by_name(cls, search_term):
        project = Image.objects.filter(name_icontains=search_term)
        return project
