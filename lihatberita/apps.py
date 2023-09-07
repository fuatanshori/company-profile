from django.apps import AppConfig


class LihatberitaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lihatberita'

    def ready(self):
        from . import signals
        return signals