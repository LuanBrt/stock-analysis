from django.urls import re_path
from . import consumers

# Define as rotas para WebSocket
websocket_urlpatterns = [
    re_path(r'ws/notification', consumers.NotificationConsumer.as_asgi()),
]
