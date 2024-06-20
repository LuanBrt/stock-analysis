import os
from django.core.asgi import get_asgi_application

# Define o módulo de configurações padrão do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')

# Obtém a aplicação ASGI para o projeto
application = get_asgi_application()
