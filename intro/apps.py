from django.apps import AppConfig


class IntroConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'intro'
    def ready(self):
        from . import signals
        return signals