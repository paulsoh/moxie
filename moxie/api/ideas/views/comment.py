from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from ideas.models import Comment, Idea
from api.ideas.serializers import CommentSerializer


class CommentIdeaAPIView(APIView):

    def get(self, request, **kwargs):
        idea = Idea.objects.get(custom_slug=kwargs.get('slug'))
        comments = idea.comment_set.all()
        serializer = CommentSerializer(comments, many=True)

        return Response(serializer.data)

    def post(self, request, **kwargs):
        if not request.user.is_authenticated():
            return Response('Login required!', status=status.HTTP_400_BAD_REQUEST)

        idea = get_object_or_404(
            Idea,
            custom_slug=kwargs.get('slug'),
        )

        comment = idea.comment_set.create(
            user=request.user,
            content=request.POST.get('content'),
        )

        serializer = CommentSerializer(comment)
        if CommentSerializer(data=serializer.data):
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
