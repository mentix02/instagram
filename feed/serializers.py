from rest_framework import serializers

from feed.models import FollowRequest
from user.serializers import UserListSerializer


class FollowRequestSerializer(serializers.ModelSerializer):

    requester = UserListSerializer()

    class Meta:
        model = FollowRequest
        fields = ['id', 'requester']
