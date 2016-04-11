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
        if not request.user.is_authenticated():
            return Response('Login required!', status=status.HTTP_400_BAD_REQUEST)

        data = request.data
        idea = Idea.objects.get(
            pk=kwargs.get('pk'),
        )

        fund, is_created = Fund.objects.get_or_create(
            funder=request.user,
            idea=idea,
        )

        if is_created:
            fund.funder = request.user
            fund.idea = idea
            fund.funder_name = data.get('funder_name', 'Null')
            fund.funder_address = data.get('funder_address', 'Null')
            fund.funder_cellphone = data.get('funder_cellphone', 'Null')
            fund.quantity = data.get('quantity', 'Null')

        else:
            fund.quantity += int(data.get('quantity'))

        fund.save()

        serializer = FundIdeaSerializer(fund)
        if FundIdeaSerializer(data=serializer.data):
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
