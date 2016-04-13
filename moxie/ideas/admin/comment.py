from django.contrib import admin

from ideas.models import Comment


@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):

    list_display = admin.ModelAdmin.list_display + (
        'user',
        'content',

        'created_at',
        'updated_at',
    )


class CommentTabularInline(admin.TabularInline):

    model = Comment
