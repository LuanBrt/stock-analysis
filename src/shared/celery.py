from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# Define o módulo de configurações padrão do Django para o Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')

# Inicializa a aplicação Celery
app = Celery('src')

# Configura a aplicação Celery usando as configurações do Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Descobre automaticamente tarefas em todos os aplicativos instalados do Django
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
