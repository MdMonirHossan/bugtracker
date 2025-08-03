import json
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer


class StreamActivityLogConsumer(AsyncWebsocketConsumer):
    """
    WebSocket consumer for real-time stream logs.
    This will manage connections, disconnection, and stream logs within group activity_log.
    """
    async def connect(self):
        """
        This method handles new WebSocket connections.
        """
        self.group_name = 'activity_log'
        # add the channel to a project group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        # Accept WebSocket connection (HandShake)
        await self.accept()

        # Accepts the connections, and sends confirmations message.
        await self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': 'Connected to activity log'
        }))

    
    async def disconnect(self, close_code):
        """
        Handles WebSocket disconnection.
        Removes the channel from project group.
        """
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def stream_log(self, event):
        await self.send(text_data=json.dumps(event['data']))