from django.apps import AppConfig


class BabushkaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'babushka'

    def ready(self):
        import babushka.signals
