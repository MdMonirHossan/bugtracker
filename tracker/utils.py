from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def notify_bug_created(project_id, bug_title):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"project_{project_id}",
        {
            "type": "bug_created",
            "message": f"New bug created: {bug_title}"
        }
    )
