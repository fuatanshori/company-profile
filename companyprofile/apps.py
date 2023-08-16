from django.apps import AppConfig


class CompanyprofileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'companyprofile'

    def ready(self):
        from . import signals
        return signals
