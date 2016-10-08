from rest_framework import serializers

from ideas.models import Comment
from django.contrib.auth.models import User


class CommentSerializer(serializers.ModelSerializer):

    username = serializers.ReadOnlyField(source='user.username')
    user_profileimage_url = serializers.ReadOnlyField(source='user.profile_image.url')

    class Meta:
        model = Comment

        fields = (
            'id',
            'username',
            'user_profileimage_url',
            'reaction',
            'content',
            'created_at',
        )

        """
        get_current_funders = serializers.Field(source='get_current_funders')
        get_current_progress = serializers.Field(source='get_current_progress')
        get_current_quantity = serializers.Field(source='get_current_quantity')

        fields = (
            '_social_score',
            'get_current_funders',
            'get_current_progress',
            'get_current_quantity',
        )
        """
