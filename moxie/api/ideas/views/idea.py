from rest_framework.generics import ListAPIView
from api.ideas.serializers import IdeaSerializer

from ideas.models import Idea


class IdeaListAPIView(ListAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
