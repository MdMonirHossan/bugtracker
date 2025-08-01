from django.urls import re_path
from .consumers import TrackerConsumer

websocket_urlpatterns = [
    re_path(r'ws/project/(?P<project_id>\d+)/$', TrackerConsumer.as_asgi()),
]