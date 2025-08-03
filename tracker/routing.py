from django.urls import re_path
from .consumers import ProjectConsumer, UserConsumer

# WebSocket Urls
websocket_urlpatterns = [
    re_path(r'ws/project/(?P<project_id>\d+)/$', ProjectConsumer.as_asgi()),   # Project room uri
    re_path(r'ws/user/', UserConsumer.as_asgi()),                              # User uri
]