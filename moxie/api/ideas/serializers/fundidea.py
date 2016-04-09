from rest_framework import serializers

from ideas.models import Idea, Fund
from django.contrib.auth.models import User


class FundIdeaSerializer(serializers.ModelSerializer):

    # username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Fund

    def save(self):
        return super(FundIdeaSerializer, self).save()
