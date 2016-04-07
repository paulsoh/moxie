from django.db import models
from django.contrib.auth.models import User


class Fund(models.Model):

    idea = models.ForeignKey(
        'Idea',
    )

    funder = models.ForeignKey(
        User,
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
