from django.db import models


class Category(models.Model):

    name = models.CharField(
        max_length=20,
    )

    slug = models.SlugField(
        allow_unicode=True,
        max_length=255,
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'category',
            kwargs={
                'slug': self.slug,
            }
        )
