import json
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ActivityLog
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .serializers import ActivityLogSerializer

@receiver(post_save, sender=ActivityLog)
def stream_logs(sender, instance, created, **kwargs):
    """
    signal receiver for post_save on the ActivityLog model.
    This signal triggered upon creating or updating any ActivityLog.
    stream real-time log to the room.
    """
    # Get the default channel layer instance
    channel_layer = get_channel_layer()

    serializer = ActivityLogSerializer(instance)
    # message payload for WebSocket.
    data = {
        'type': 'stream_log',
        'data': {
            'action': 'log_created',
            **serializer.data
        }
    }

    # send the message to the relevant WebSocket for log stream
    async_to_sync(channel_layer.group_send)(
        'activity_log',
        data
    )
