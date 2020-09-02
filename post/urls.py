from django.urls import path

from post.views import CreatePostAPIView, DeletePostAPIView, UpdatePostAPIView

app_name = 'post'

urlpatterns = [
    path('create/', CreatePostAPIView.as_view(), name='create'),
    path('update/<int:pk>/', UpdatePostAPIView.as_view(), name='update'),
    path('delete/<int:pk>/', DeletePostAPIView.as_view(), name='delete'),
]
