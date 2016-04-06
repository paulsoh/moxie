from django.contrib import admin

from ideas.models import Idea


@admin.register(Idea)
class IdeaModelAdmin(admin.ModelAdmin):

    list_display = admin.ModelAdmin.list_display + (
        'title',

        'description',
        'price',
        'social_score',
        'sales_goal',
    )
