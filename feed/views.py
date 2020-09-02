from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.core.handlers.wsgi import WSGIRequest

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser

from post.models import Post
from feed.models import FollowRequest
from post.serializers import PostSerializer
from feed.serializers import FollowRequestSerializer


User = get_user_model()


class FeedAPIView(ListAPIView):

    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self) -> QuerySet:
        user = self.request.user
        followers = user.following
        follower_ids = list(followers.values_list('id', flat=True)) + [user.id]
        return Post.objects.filter(user__in=follower_ids).order_by('-timestamp')


class UnfollowUserAPIView(APIView):

    permission_classes = (IsAuthenticated,)
    parser_classes = (FormParser, MultiPartParser)

    @staticmethod
    def post(request: WSGIRequest) -> Response:

        user_id = request.POST.get('user_id')
        if not user_id:
            return Response(
                {'error': 'Follow request\'s user ID not provided.'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user = get_object_or_404(User, id=user_id)
        request.user.unfollow(user)
        return Response({'detail': 'unfollowed'})


class FollowUserAPIView(APIView):

    """
    APIView to make a request (or directly follow is user to be followed
    has a public account) by an authenticated user.
    """

    permission_classes = (IsAuthenticated,)
    parser_classes = (FormParser, MultiPartParser)

    @staticmethod
    def post(request: WSGIRequest) -> Response:

        user_id = request.POST.get('user_id')
        if not user_id:
            return Response(
                {'error': 'Follow request\'s user ID not provided.'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user = get_object_or_404(User, id=user_id)
        request.user.follow(user)
        if user.private:
            return Response({'detail': 'requested'})
        else:
            return Response({'detail': 'followed'})


class FollowRequestListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FollowRequestSerializer

    def get_queryset(self) -> QuerySet:
        return self.request.user.requests.all()


class FollowRequestActionAPIView(APIView):

    """
    APIView to accept or reject a FollowRequest by the person
    who is being requested to act upon said request.
    """

    parser_classes = (MultiPartParser,)
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def post(request: WSGIRequest) -> Response:
        try:
            action = request.POST['action']
            follow_request_id = request.POST['follow_request_id']
        except KeyError as field:
            return Response(
                {'error': f'{str(field)} not provided.'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        follow_request: FollowRequest = get_object_or_404(
            FollowRequest, id=follow_request_id
        )

        resp = {'detail': 'rejected'}

        if action == '1':
            resp['detail'] = 'accepted'
            follow_request.accept()
        else:
            follow_request.reject()

        return Response(resp)
