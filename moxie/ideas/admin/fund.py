from django.contrib import admin


from ideas.models import Fund


@admin.register(Fund)
class IdeaModelAdmin(admin.ModelAdmin):

    list_display = admin.ModelAdmin.list_display + (
        'idea',

        'funder',
        'quantity',
        'created_at',
        'updated_at',
    )
