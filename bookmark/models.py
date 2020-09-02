from typing import List, Tuple

from django.db import models


class Bookmark(models.Model):

    post = models.ForeignKey('post.Post', on_delete=models.CASCADE)
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, related_name='bookmarks'
    )

    class Meta:

        ordering = ('-pk',)

        unique_together: List[Tuple[str, str]] = [
            ('post', 'user'),
        ]

        indexes: List[models.Index] = [
            models.Index(fields=('post', 'user')),
        ]
