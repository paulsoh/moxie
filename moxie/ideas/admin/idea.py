from django.contrib import admin

from ideas.models import Idea


@admin.register(Idea)
class IdeaModelAdmin(admin.ModelAdmin):

    list_display = admin.ModelAdmin.list_display + (
        'title',

        'description',
        'price',
        '_social_score',
        'sales_goal',
        '_created_at',
        '_updated_at',
    )
