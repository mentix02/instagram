from django.urls import path

from feed.views import (
    FeedAPIView,
    FollowUserAPIView,
    UnfollowUserAPIView,
    FollowRequestListAPIView,
    FollowRequestActionAPIView,
)

app_name = 'feed'

urlpatterns = [
    path('posts/', FeedAPIView.as_view(), name='feed'),
    path('follow/', FollowUserAPIView.as_view(), name='follow'),
    path('unfollow/', UnfollowUserAPIView.as_view(), name='unfollow'),
    path('requests/', FollowRequestListAPIView.as_view(), name='list'),
    path('action/', FollowRequestActionAPIView.as_view(), name='action'),
]
