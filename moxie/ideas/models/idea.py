from django.db import models
from django.core.urlresolvers import reverse


class Idea(models.Model):

    title = models.CharField(
        max_length=60,
    )

    description = models.TextField()

    price = models.IntegerField()

    sales_goal = models.IntegerField(
        default=20,
    )

    custom_slug = models.SlugField(
        blank=True,
        null=True,
    )

    end_date = models.DateTimeField(
    )

    _social_score = models.IntegerField(
        default=0,
    )

    _created_at = models.DateTimeField(
        auto_now_add=True,
    )

    _updated_at = models.DateTimeField(
        auto_now=True,
    )

    def _get_current_count(self):
        pass

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'idea-detail',
            kwargs={
                'pk': self.id,
            }
        )
