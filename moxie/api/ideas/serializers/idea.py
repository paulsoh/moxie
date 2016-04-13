from rest_framework import serializers

from ideas.models import Idea
from django.contrib.auth.models import User


class IdeaSerializer(serializers.ModelSerializer):
    """
    This is for returning the updated idea meta data when ajax post is handled
    """

    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Idea

        get_current_funders = serializers.Field(source='get_current_funders')
        get_current_progress = serializers.Field(source='get_current_progress')
        get_current_quantity = serializers.Field(source='get_current_quantity')

        fields = (
            'title',
            'category',
            'username',
            'thumbnail_image',
            'description',
            'end_date',
            '_social_score',
            'get_current_funders',
            'get_current_progress',
            'get_current_quantity',
        )
