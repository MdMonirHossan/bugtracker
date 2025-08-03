from django.apps import AppConfig


class TrackerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tracker'

    # Trigger signals in ready
    def ready(self):
        from .signals import bug_event
