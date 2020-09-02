from __future__ import annotations
from typing import Optional

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (
    AbstractUser,
    UserManager as AbstractUserManager,
)

from post.models import Post
from bookmark.models import Bookmark
from feed.models import FollowRequest


class UserManager(AbstractUserManager):
    def get_by_natural_key(self, username):
        case_insensitive_username_field = '{}__iexact'.format(self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})


class User(AbstractUser):

    PRIVATE = True
    PUBLIC = False

    VISIBILITY_CHOICES = [
        (PRIVATE, 'Private'),
        (PUBLIC, 'Public'),
    ]

    email: str = models.EmailField(_('email address'), unique=True)
    private: bool = models.BooleanField(default=PUBLIC, choices=VISIBILITY_CHOICES)
    bio: str = models.CharField(
        max_length=250, null=True, blank=True, help_text='About the user.'
    )
    picture = models.ImageField(
        null=True,
        blank=True,
        default='default.png',
        upload_to='profile_pictures',
        verbose_name=_('profile picture'),
    )

    _follows = models.ManyToManyField('User', blank=True, related_name='followed_by')

    objects = UserManager()

    REQUIRED_FIELDS = ['email', 'password']

    def bookmark(self, post: Post) -> Optional[Bookmark]:
        if post.user in self.following:
            bookmark, _ = Bookmark.objects.get_or_create(user=self, post=post)
            return bookmark
        else:
            return None

    def remove_bookmark(self, post: Post) -> None:
        pass

    def unfollow(self, user: User) -> None:
        """ Helper function to remove a user from this users following list. """

        # Remove all bookmarks of posts since user now unfollowed.
        Bookmark.objects.filter(user=self, post__user=user).delete()

        self._follows.remove(user)

    def follow(self, user: User, force: bool = False) -> None:
        """ Helper function to add user to a follower list. """

        if user.id == self.id:
            return

        if force:
            self._follows.add(user)
            return

        if user.private:
            FollowRequest.objects.get_or_create(requester=self, to_follow=user)
        else:
            self._follows.add(user)

    def post_count(self) -> int:
        return self.posts.count()

    def follower_count(self) -> int:
        return self.followers.count()

    def following_count(self) -> int:
        return self.following.count()

    @property
    def following(self) -> models.QuerySet:
        """ Returns a QuerySet of Users that this user follows. """
        return self._follows.all()

    @property
    def followers(self) -> models.QuerySet:
        """ Returns a QuerySet of Users following this user. """
        return self.followed_by.all()

    def __str__(self) -> str:
        return self.username
