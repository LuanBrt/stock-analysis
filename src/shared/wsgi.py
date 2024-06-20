import os
from django.core.wsgi import get_wsgi_application

# Define o módulo de configurações padrão do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')

# Obtém a aplicação WSGI para o projeto
application = get_wsgi_application()
