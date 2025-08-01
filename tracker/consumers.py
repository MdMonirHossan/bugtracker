import json
from channels.generic.websocket import AsyncWebsocketConsumer

class TrackerConsumer(AsyncWebsocketConsumer):
    """
    WebSocket consumer for real-time communication.
    This will manage connections, disconnection, and message broadcasting within a group named project_{id}.
    """
    async def connect(self):
        """
        This method handles new WebSocket connections.
        """
        self.project_id = self.scope['url_route']['kwargs']['project_id']    # Extracts project ID from url
        self.room_group_name = f'project_{self.project_id}'   # create a unique group name
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)   # add the channel to a project group
        await self.accept()   # Accept WebSocket connection (HandShake)

        # Accepts the connections, and sends confirmations message.
        await self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': f'Connected to project {self.project_id}'
        }))

    async def disconnect(self, close_code):
        """
        Handles WebSocket disconnection.
        Removes the channel from project group.
        """
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    
    async def receive(self, text_data):
        """
        Handles message receive from the client over WebSocket
        """
        # Send the received message to all channels in the project group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'broadcast_message',
                'message': json.loads(text_data)
            }
        )
    
    async def broadcast_message(self, event):
        """
        Handles message broadcast
        invoked by group_send 
        send the received message directly to the client connected this consumer
        """
        await self.send(text_data=json.dumps(event['message']))

    

    # This method will be called via channel_layer.group_send
    async def bug_created(self, event):
        await self.send(text_data=json.dumps({
            'type': 'bug_created',
            'message': event['message']
        }))
