from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ideas.models import Idea, Fund
from api.ideas.serializers import FundIdeaSerializer, IdeaSerializer


class FundIdeaAPIView(APIView):

    def get(self, request, **kwargs):
        idea = Idea.objects.get(pk=kwargs.get('pk'))
        serializer = IdeaSerializer(idea)

        return Response(serializer.data)

    def post(self, request, **kwargs):
        data = request.data

        idea = Idea.objects.get(
            pk=kwargs.get('pk'),
        )

        fund = Fund.objects.create(
            funder=request.user,
            idea=idea,
            funder_name=data.get('funder_name'),
            funder_address=data.get('funder_address'),
            funder_cellphone=data.get('funder_cellphone'),
            quantity=data.get('quantity'),
        )

        serializer = FundIdeaSerializer(fund)
        if FundIdeaSerializer(data=serializer.data):
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
