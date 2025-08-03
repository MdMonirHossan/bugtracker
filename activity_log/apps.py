from django.apps import AppConfig


class ActivityLogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'activity_log'

    # Trigger signals in ready
    def ready(self):
        from .signals import stream_logs