from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'user'

    def ready(self):
        # noinspection PyUnresolvedReferences
        import user.signals
