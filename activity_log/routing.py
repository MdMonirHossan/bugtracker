from django.urls import re_path
from .consumers import StreamActivityLogConsumer

websocket_urlpatterns = [
    re_path(r'ws/logs/', StreamActivityLogConsumer.as_asgi()),
]