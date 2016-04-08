from django.db.models.signals import pre_save
from django.dispatch import receiver

from ideas.models import Idea


@receiver(pre_save, sender=Idea)
def pre_save_idea(sender, instance, *args, **kwargs):
    """
    Create/save custom_slug automatically if not specified
    """
    if not instance.custom_slug:
        from django.utils.text import slugify
        instance.custom_slug = slugify(instance.title, allow_unicode=True)
