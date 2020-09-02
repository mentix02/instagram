from django.db.models import QuerySet

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from notification.models import Notification
from notification.serializers import NotificationSerializer


class NotificationListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = NotificationSerializer

    def get_queryset(self) -> QuerySet:
        return Notification.objects.filter(user=self.request.user)
