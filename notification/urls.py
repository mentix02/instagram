from django.urls import path

from notification.views import NotificationListAPIView

app_name = 'notification'

urlpatterns = [
    path('', NotificationListAPIView.as_view(), name='list'),
]
