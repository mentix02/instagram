from typing import List
from datetime import datetime

from django.db import models


class Notification(models.Model):

    LIKED = 'L'
    FOLLOWED = 'F'
    ACCEPTED = 'A'
    COMMENTED = 'C'

    ACTION_CHOICES = (
        (LIKED, 'liked'),
        (FOLLOWED, 'followed'),
        (ACCEPTED, 'accepted'),
        (COMMENTED, 'commented'),
    )

    read: bool = models.BooleanField(default=False)
    timestamp: datetime = models.DateTimeField(auto_now_add=True)
    action: str = models.CharField(choices=ACTION_CHOICES, max_length=5)
    actor = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='+')
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, related_name='notifications'
    )
    post = models.ForeignKey(
        'post.Post', null=True, blank=True, related_name='+', on_delete=models.CASCADE,
    )

    def mark_read(self) -> None:
        self.read = True
        self.save()

    class Meta:
        indexes: List[models.Index] = [
            models.Index(fields=('user',)),
        ]

    def __str__(self) -> str:
        if self.action == self.LIKED:
            return f"{self.actor} liked {self.user}'s post {self.post}"
        elif self.action == self.FOLLOWED:
            return f'{self.actor} followed {self.user}'
        elif self.action == self.ACCEPTED:
            return f"{self.actor} accepted {self.user}'s request"
        elif self.action == self.COMMENTED:
            return f"{self.actor} commented on {self.user}'s post {self.post}"
