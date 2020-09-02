from django.db import IntegrityError
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from post.models import Post


class PostLikeAPIView(APIView):

    permission_classes = (IsAuthenticated,)

    @staticmethod
    def post(request) -> Response:

        user = request.user
        post_id = request.POST.get('post', False)

        if not post_id:
            return Response(
                {'error': 'post_id required'}, status=status.HTTP_400_BAD_REQUEST
            )

        post = get_object_or_404(Post, id=post_id)
        try:
            if (
                not post.user.private
                or post.user == user
                or post.id
                in Post.objects.filter(
                    user_id__in=user.following.values_list('id', flat=True)
                ).values_list('id', flat=True)
            ):
                post.votes.up(user.id)
            else:
                return Response(
                    {'error': 'Not found.'}, status=status.HTTP_404_NOT_FOUND
                )
        except IntegrityError:
            return Response({'like': 'existed'}, status=status.HTTP_200_OK)
        else:
            return Response({'like': 'created'}, status=status.HTTP_201_CREATED)


class PostUnlikeAPIView(APIView):

    permission_classes = (IsAuthenticated,)

    @staticmethod
    def delete(request, pk) -> Response:
        post = get_object_or_404(Post, id=pk)
        post.votes.delete(request.user.id)
        return Response(status=status.HTTP_204_NO_CONTENT)
