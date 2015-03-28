from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="")


class Campground(models.Model):

    user = models.ForeignKey(User, related_name='campgrounds')
    campground_name = models.CharField(max_length=100,)
    campground_email = models.CharField(max_length=100)
    campground_phone = models.CharField(validators=[phone_regex], max_length=100)
    campground_address = models.CharField(max_length=100)
    campground_zip = models.CharField(max_length=256)
    campground_description = models.TextField()
    campground_latitude = models.CharField(max_length=256)
    campground_longitude = models.CharField(max_length=256)
    timestamp = models.DateTimeField(auto_now=True)