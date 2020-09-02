from django.urls import path

from like.views import PostLikeAPIView, PostUnlikeAPIView

app_name = 'like'

urlpatterns = [
    path('create/', PostLikeAPIView.as_view(), name='create'),
    path('delete/<int:pk>/', PostUnlikeAPIView.as_view(), name='delete'),
]
