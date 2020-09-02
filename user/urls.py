from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from user.views import (
    UserUpdateAPIView,
    UserDetailAPIView,
    UserPostListAPIView,
    UserRegistrationAPIView,
    UserFollowingListAPIView,
    UserFollowersListAPIView,
)

app_name = 'user'

urlpatterns = [
    path('token/', obtain_auth_token, name='token'),
    path('create/', UserRegistrationAPIView.as_view(), name='create'),
    path('posts/<slug:username>/', UserPostListAPIView.as_view(), name='posts'),
    path('update/<slug:username>/', UserUpdateAPIView.as_view(), name='update'),
    path('detail/<slug:username>/', UserDetailAPIView.as_view(), name='detail'),
    path(
        'following/<slug:username>/',
        UserFollowingListAPIView.as_view(),
        name='following',
    ),
    path(
        'followers/<slug:username>/',
        UserFollowersListAPIView.as_view(),
        name='followers',
    ),
]
