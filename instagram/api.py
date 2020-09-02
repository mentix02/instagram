from django.urls import path, include

urlpatterns = [
    path('feed/', include('feed.urls')),
    path('user/', include('user.urls')),
    path('post/', include('post.urls')),
    path('like/', include('like.urls')),
    path('bookmark/', include('bookmark.urls')),
    path('notifications/', include('notification.urls')),
]
