from django.apps import AppConfig


class UersConfig(AppConfig):
    name = 'apps.user'

    def ready(self):
        import apps.user.signals


