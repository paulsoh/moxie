from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Fund(models.Model):

    idea = models.ForeignKey(
        'Idea',
    )

    funder = models.ForeignKey(
        settings.AUTH_USER_MODEL,
    )

    funder_name = models.CharField(
        max_length=60,
    )

    funder_address = models.CharField(
        max_length=255,
    )

    funder_cellphone = models.CharField(
        max_length=16,
    )

    quantity = models.PositiveIntegerField(
        default=1,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )
