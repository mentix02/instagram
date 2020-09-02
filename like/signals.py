from django.dispatch import receiver
from django.db.models.signals import post_save

from vote.models import Vote

from post.models import Post
from notification.models import Notification


# noinspection PyUnusedLocal
@receiver(post_save, sender=Vote)
def send_post_like_notification(sender, instance: Vote, **kwargs):
    if instance.content_object.user_id == instance.user_id:
        return
    Notification.objects.create(
        action=Notification.LIKED,
        actor_id=instance.user_id,
        post_id=instance.object_id,
        user_id=instance.content_object.user_id,
    )
