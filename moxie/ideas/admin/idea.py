from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from ideas.models import Idea


@admin.register(Idea)
class IdeaModelAdmin(SummernoteModelAdmin):

    list_display = admin.ModelAdmin.list_display + (
        'category',
        'title',

        'description',
        'price',
        '_social_score',
        'sales_goal',
        '_created_at',
        '_updated_at',
    )
