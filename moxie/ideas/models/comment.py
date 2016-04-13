from django.db import models
from django.conf import settings


class Comment(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
    )

    idea = models.ForeignKey(
        'Idea',
    )

    content = models.TextField()

    reaction = models.PositiveIntegerField(
        default=0,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.content
