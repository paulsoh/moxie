from django.db import models


class Idea(models.Model):

    title = models.CharField(
        max_length=60,
    )

    description = models.TextField()

    price = models.IntegerField()

    social_score = models.IntegerField(
        default=0,
    )

    sales_goal = models.IntegerField(
        default=20,
    )
