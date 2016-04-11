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

    @property
    def get_current_sales(self):
        sum = 0
        for idea in self.idea_set.all():
            if not idea.is_past:
                sum += idea.price*idea.get_current_quantity
        return sum

    @property
    def get_total_sales(self):
        sum = 0
        for idea in self.idea_set.all():
            if not idea.is_past:
                sum += idea.price*idea.get_current_quantity
        return sum

    @property
    def get_sales_goal(self):
        sum = 0
        for idea in self.idea_set.all():
            if not idea.is_past:
                sum += idea.price*idea.sales_goal
        return sum

    @property
    def get_current_ideas_count(self):
        sum = 0
        for idea in self.idea_set.all():
            if not idea.is_past:
                sum += 1
        return sum

    @property
    def get_finished_ideas_count(self):
        sum = 0
        for idea in self.idea_set.all():
            if idea.is_past:
                sum += 1
        return sum

    def __str__(self):
        return "{name}".format(name=self.username)
