import json
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Bug, Comment
from activity_log.models import ActivityLog
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .serializers import BugSerializer, CommentSerializer


@receiver(post_save, sender=Bug)
def bug_event(sender, instance, created, **kwargs):
    """
    signal receiver for post_save on the Bug model.
    This signal triggered upon creating or updating any Bug.
    send real-time update to the project room by project id.
    """
    # Get the default channel layer instance
    channel_layer = get_channel_layer()

    serializer = BugSerializer(instance)

    # message payload for WebSocket.
    action = 'bug.created' if created else 'bug.updated'
    data = {
        'type': 'bug_update',
        'data': {
            'action': action,
            **serializer.data
        }
    }

    # Log and activity when a Bug instance is created or updated
    try:
        desc = f"{instance.created_by.username} {'created' if created else 'updated'} bug: {instance.title}"
        ActivityLog.objects.create( 
            project = instance.project,
            user = instance.created_by,
            action = action,
            description = desc,
            data = json.dumps(data),
            ip_address = channel_layer
        )
    except:
        pass

    # send the message to the relevant WebSocket group using channel layer.
    async_to_sync(channel_layer.group_send)(
        f'project_{instance.project.id}',
        data
    )


@receiver(post_save, sender=Comment)
def comment_event(sender, instance, created, **kwargs):
    """
    Django signal receiver for post_save on the Comment model.
    This signal triggered upon any comment creation.
    Send real-time update to the assigned and created_by users via channel_layer
    """
    # Get the default channel layer instance
    channel_layer = get_channel_layer()

    serializer = CommentSerializer(instance)
    bug = instance.bug

    recipients = set()

    if bug.created_by:
        recipients.add(bug.created_by.id)
    if bug.assigned_to:
        recipients.add(bug.assigned_to.id)
    
    # Log and activity when a Bug instance is created or updated
    try:
        desc = f"{instance.commenter.username} created comment in project : {bug.project.name}"
        activity_log = ActivityLog.objects.create( 
            project = bug.project,
            user = instance.commenter,
            action = 'comment.created',
            description = desc,
            ip_address = channel_layer
        )
    except Exception as e:
        print('excepton in comment ', str(e))

    if recipients:
        # message payload for WebSocket.
        data = {
            'type': 'comment_notification',
            'data': {
                'action': 'comment.create',
                **serializer.data
            }
        }
        try:
            activity_log.data = json.dumps(data)
            activity_log.save()
        except Exception as e:
            print(' excetp ', str(e))
        # send the message to the relevant WebSocket group using channel layer.
        for id in recipients:
            async_to_sync(channel_layer.group_send)(
                f'user_{id}',
                data
            )
