from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):

    alias = models.CharField(
        max_length=24,
        unique=True,
        blank=True,
        null=True,
    )

    profile_image = models.ImageField(
        blank=True,
        null=True,
    )

    phone_regex = RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )

    phonenumber = models.CharField(
        max_length=15,
        validators=[phone_regex],
        blank=True
    )

    def __str__(self):
        return "{name}".format(name=self.username)
