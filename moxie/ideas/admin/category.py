from django.contrib import admin

from ideas.models import Category


@admin.register(Category)
class IdeaModelAdmin(admin.ModelAdmin):

    list_display = admin.ModelAdmin.list_display + (
        'name',
        'slug',

        'created_at',
        'updated_at',
    )
