from urllib.parse import parse_qs
import json
from django.contrib.auth.models import AnonymousUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import UntypedToken
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

class ProjectConsumer(AsyncWebsocketConsumer):
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
        
        # add the channel to a project group
        await self.channel_layer.group_add(
            self.room_group_name, 
            self.channel_name
        )
        
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
        await self.channel_layer.group_discard(
            self.room_group_name, 
            self.channel_name
        )

    
    # async def receive(self, text_data):
    #     """
    #     Handles message receive from the client over WebSocket
    #     """
    #     # Send the received message to all channels in the project group
    #     await self.channel_layer.group_send(
    #         self.room_group_name,
    #         {
    #             'type': 'broadcast_message',
    #             'message': json.loads(text_data)
    #         }
    #     )
    
    async def bug_update(self, event):
        """
        Handles message broadcast
        invoked by group_send 
        send the received message directly to the client connected this consumer
        """
        await self.send(text_data=json.dumps(event['data']))


class UserConsumer(AsyncWebsocketConsumer):
    """
    WebSocket consumer for real-time communication.
    This will manage connections, disconnection, and message broadcasting within a group or user named user_{id}.
    """
    async def connect(self):
        """
        This method handles new WebSocket connections as well as extract the 
        requested user.
        """
        # Extract JWT token from query params
        query_string = self.scope['query_string'].decode()
        query_params = parse_qs(query_string)
        token = query_params.get('token', [None])[0]

        # get the user details from provided token
        if token:
            try:
                validate_token = UntypedToken(token)
                jwt_auth = JWTAuthentication()
                user = await sync_to_async(jwt_auth.get_user)(validate_token)
                self.scope['user'] = user
            except Exception as e:
                print('Auth error ; ', str(e))
                self.scope['user'] = AnonymousUser()
        
        self.group_name = None

        self.user_id = self.scope['user'].id

        if self.scope['user'].is_anonymous:
            await self.close()
        else:

            self.group_name = f'user_{self.user_id}'
            
            # add the channel to a project group
            await self.channel_layer.group_add(
                self.group_name,
                self.channel_name
            )

            await self.accept()

        # Accepts the connections, and sends confirmations message.
        await self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': f'Connected to {self.group_name}'
        }))

    
    async def disconnect(self, close_code):
        """
        Handles WebSocket disconnection.
        Removes the channel from user group.
        """
        self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )


    async def comment_notification(self, event):
        """
        Handles message broadcast
        send the received message directly to the client connected this consumer
        """
        await self.send(text_data=json.dumps(event['data']))

