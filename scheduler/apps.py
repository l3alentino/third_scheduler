from django.apps import AppConfig
from .tasks import scheduler

class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scheduler'

    def ready(self):
        scheduler.start()