import sys
from django.apps import AppConfig

# Configuração inicial do aplicativo Django.
class InitAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src'

    def ready(self):
        if 'runserver' not in sys.argv:
            return True

        from .tasks import get_data_for_stocks
        get_data_for_stocks.delay()
