import json
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer


class StreamActivityLogConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()


        await self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': 'Connected to activity log'
        }))

    
    async def disconnect(self, close_code):
        pass

    async def stream_log(self, event):
        await self.send(text_data=json.dumps(event['data']))