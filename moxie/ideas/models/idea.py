from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Idea(models.Model):

    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
    )

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
        allow_unicode=True,
        max_length=255,
        blank=True,
        null=True,
    )

    end_date = models.DateField(
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
        settings.AUTH_USER_MODEL,
        related_name='fund_idea_set',
        through='Fund',
    )

    @property
    def get_current_quantity(self):
        return self.fund_set.aggregate(Sum('quantity')).get('quantity__sum', 0)

    @property
    def get_current_funders(self):
        return self.fund_user_set.count()

    @property
    def get_current_progress(self):
        if self.get_current_quantity is None:
            return 0
        return int(self.get_current_quantity/self.sales_goal*100)

    @property
    def is_past(self):
        from django.utils import timezone
        from datetime import datetime
        t = timezone.localtime(timezone.now())
        _end_date = timezone.make_aware(
                datetime.combine(
                    self.end_date,
                    datetime.max.time()
                ),
                timezone.get_default_timezone(),
        )
        if t > _end_date:
            return True
        return False

    @property
    def get_time_left(self):
        from django.utils import timezone
        from datetime import datetime
        t = timezone.localtime(timezone.now())
        _end_date = timezone.make_aware(
                datetime.combine(
                    self.end_date,
                    datetime.max.time()
                ),
                timezone.get_default_timezone(),
        )

        time_left = _end_date-t

        if time_left//3600 is 0:
            return "{days}d".format(days=time_left.days)
        return "{days}d {hours}h".format(days=time_left.days, hours=time_left.seconds//3600)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'idea-detail',
            kwargs={
                'slug': self.custom_slug,
            }
        )
