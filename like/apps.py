from django.apps import AppConfig


class LikeConfig(AppConfig):
    name = 'like'

    def ready(self):
        # noinspection PyUnresolvedReferences
        import like.signals
