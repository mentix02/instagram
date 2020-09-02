from typing import List
from datetime import datetime

from django.db import models
from django.core.exceptions import SuspiciousOperation

from vote.models import VoteModel


class Post(VoteModel, models.Model):

    timestamp: datetime = models.DateTimeField(auto_now_add=True)
    caption: str = models.CharField(max_length=750, null=True, blank=True)
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, related_name='posts',
    )

    @property
    def image_links(self) -> models.QuerySet:
        return self.images.values_list('file', flat=True)

    class Meta:
        indexes: List[models.Index] = [
            models.Index(fields=('user',)),
        ]

    def __str__(self) -> str:
        return self.user.username


class Image(models.Model):

    file = models.ImageField(upload_to='post_images/')
    post: Post = models.ForeignKey(
        'post.Post', on_delete=models.CASCADE, related_name='images',
    )

    def save(self, *args, **kwargs) -> None:
        """ Sanitary check for a post having more than or equal to 5 images. """

        if self.post.images.count() >= 5:
            raise SuspiciousOperation('Post already contains 5 images.')
        else:
            super().save(*args, **kwargs)

    class Meta:
        indexes: List[models.Index] = [
            models.Index(fields=('post',)),
        ]

    def __str__(self) -> str:
        return str(self.post)
