from tracker.routing import websocket_urlpatterns as tracker_ws
from activity_log.routing import websocket_urlpatterns as log_ws

websocket_urlpatterns = tracker_ws + log_ws