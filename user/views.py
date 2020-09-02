import time

from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
)

from user.models import User
from post.models import Post
from user.permissions import UserIsOwner
from post.serializers import PostSerializer, PostListSerializer
from user.serializers import UserSerializer, UserListSerializer, UserDetailSerializer


class UserRegistrationAPIView(CreateAPIView):
    serializer_class = UserSerializer


class UserUpdateAPIView(RetrieveUpdateAPIView):
    lookup_url_kwarg = 'username'
    queryset = User.objects.all()
    lookup_field = 'username__iexact'
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, UserIsOwner)


class UserDetailAPIView(RetrieveAPIView):
    lookup_url_kwarg = 'username'
    queryset = User.objects.all()
    lookup_field = 'username__iexact'
    serializer_class = UserDetailSerializer


class UserPostListAPIView(ListAPIView):
    serializer_class = PostListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self) -> QuerySet:
        username = self.kwargs['username']
        user = get_object_or_404(User, username__iexact=username)
        if (
            not user.private
            or user.id == self.request.user.id
            or user.id in self.request.user.following.values_list('id', flat=True)
        ):
            return Post.objects.filter(user__username__iexact=username).order_by(
                '-timestamp'
            )
        else:
            raise PermissionDenied('Follow user to see their posts.')


def user_follow_list_view_factory(following: bool = True):
    class UserFollowListAPIView(ListAPIView):
        lookup_url_kwarg = 'username'
        serializer_class = UserListSerializer
        permission_classes = (IsAuthenticated,)

        def get_queryset(self) -> QuerySet:
            user = get_object_or_404(
                User, username__iexact=self.kwargs.get(self.lookup_url_kwarg)
            )
            if (
                not user.private
                or user.id == self.request.user.id
                or user.id in self.request.user.following.values_list('id', flat=True)
            ):
                if following:
                    return user.following
                else:
                    return user.followers

    return UserFollowListAPIView


UserFollowingListAPIView = user_follow_list_view_factory(True)
UserFollowersListAPIView = user_follow_list_view_factory(False)
