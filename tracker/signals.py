from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Bug
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .serializers import BugSerializer

# Get the default channel layer instance
channel_layer = get_channel_layer()

@receiver(post_save, sender=Bug)
def bug_event(sender, instance, created, **kwargs):
    """
    signal receiver for post_save on the Bug model.
    """
    serializer = BugSerializer(instance)

    # message payload for WebSocket.
    message = {
        'type': 'bug.created' if created else 'bug.updated',
        'data': serializer.data
    }

    # send the message to the relevant WebSocket group using channel layer.
    async_to_sync(channel_layer.group_send)(f'project_{instance.project.id}',{
        'type': 'broadcast_message',
        'message': message
    })