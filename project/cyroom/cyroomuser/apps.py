from django.apps import AppConfig


class CyroomuserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cyroomuser'

    def ready(self):
        import cyroomuser.signals

