from tracker.routing import websocket_urlpatterns as tracker_ws
from activity_log.routing import websocket_urlpatterns as log_ws

# concat all WebSocket urls from different apps
websocket_urlpatterns = tracker_ws + log_ws