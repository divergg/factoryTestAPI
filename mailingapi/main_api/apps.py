from django.apps import AppConfig


class MainApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main_api'

    def ready(self):
        from . import signals