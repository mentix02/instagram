from typing import Dict, Optional

from rest_framework import serializers
from user.exceptions import ConflictException

from user.models import User
from feed.models import FollowRequest


class UserDetailSerializer(serializers.ModelSerializer):

    post_count: int = serializers.IntegerField()
    follower_count: int = serializers.IntegerField(read_only=True)
    following_count: int = serializers.IntegerField(read_only=True)
    being_followed: Optional[bool] = serializers.SerializerMethodField()
    name: str = serializers.CharField(source='get_full_name', read_only=True)

    def get_being_followed(self, user: User) -> Optional[bool]:
        logged_in_user: Optional[User] = None
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            logged_in_user = request.user
        if logged_in_user.is_active:
            if FollowRequest.objects.filter(
                requester=logged_in_user, to_follow=user
            ).exists():
                return None
            else:
                return user.id in logged_in_user.following.values_list('id', flat=True)
        else:
            return False

    class Meta:
        model = User
        fields = [
            'id',
            'bio',
            'name',
            'picture',
            'private',
            'username',
            'post_count',
            'being_followed',
            'follower_count',
            'following_count',
        ]


class UserListSerializer(serializers.ModelSerializer):

    name = serializers.CharField(source='get_full_name')

    class Meta:
        model = User
        fields = ['picture', 'username', 'name']


class UserSerializer(serializers.ModelSerializer):

    last_name: str = serializers.CharField(required=False, write_only=True)
    first_name: str = serializers.CharField(required=False, write_only=True)
    name: str = serializers.CharField(source='get_full_name', read_only=True)
    password: str = serializers.CharField(
        required=True, write_only=True, style={'input_type': 'password'},
    )
    bio: str = serializers.CharField(
        required=False,
        max_length=250,
        help_text='About the user.',
        style={'base_template': 'textarea.html'},
    )

    def create(self, validated_data: Dict[str, str]) -> User:
        try:
            User.objects.get(username__iexact=validated_data.get('username'))
        except User.DoesNotExist:
            user = User.objects.create_user(**validated_data)
            return user
        else:
            raise ConflictException('Username already taken.')

    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'first_name',
            'last_name',
            'email',
            'username',
            'password',
            'picture',
            'private',
            'bio',
        )
