from rest_framework import serializers

from post.models import Post, Image
from user.serializers import UserListSerializer


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['file']


class PostListSerializer(serializers.ModelSerializer):

    user = UserListSerializer()
    images = ImageListSerializer(many=True)

    class Meta:
        model = Post
        exclude = ['timestamp', 'vote_score', 'num_vote_down']


class PostSerializer(serializers.ModelSerializer):

    user = UserListSerializer()
    images = ImageListSerializer(many=True)
    is_liked = serializers.SerializerMethodField(allow_null=True)
    is_bookmarked = serializers.SerializerMethodField(allow_null=True)

    class Meta:
        model = Post
        exclude = ['timestamp', 'vote_score', 'num_vote_down']

    def get_is_liked(self, post):
        user = None
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            user = request.user
        if user:
            return post.votes.exists(user.id)
        else:
            return None

    def get_is_bookmarked(self, post):
        user = None
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            user = request.user
        if user:
            return post.id in user.bookmarks.values_list('post_id', flat=True)
        else:
            return None


class PostModifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['user', 'caption']
