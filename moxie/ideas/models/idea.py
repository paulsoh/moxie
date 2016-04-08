from django.db import models
from django.db.models import Sum
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User


class Idea(models.Model):

    title = models.CharField(
        max_length=60,
    )

    thumbnail_image = models.ImageField(
        upload_to="thumbnail_images",
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

    fund_user_set = models.ManyToManyField(
        User,
        related_name='fund_idea_set',
        through='Fund',
    )

    def set_custom_slug(self):
        from django.utils.text import slugify
        self.custom_slug = slugify(self.title, allow_unicode=True)

    @property
    def get_current_quantity(self):
        return self.fund_set.aggregate(Sum('quantity')).get('quantity__sum', 0)

    @property
    def get_current_funders(self):
        return self.fund_user_set.count()

    @property
    def get_current_progress(self):
        return int(self.get_current_quantity/self.sales_goal*100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'idea-detail',
            kwargs={
                'pk': self.id,
            }
        )
