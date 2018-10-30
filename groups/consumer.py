import json
from channels.generic.websocket import AsyncWebsocketConsumer


class LikeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            'likes',
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            'likes',
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        print(data)

        await self.channel_layer.group_send(
            'likes',
            {
                'type': 'msg',
                'ok': True,
            }
        )

    async def send_likes_number(self, event):
        group_id = event['group_id']
        likes_number = event['likes_number']

        await self.send(text_data=json.dumps({
            'action': 'update_likes_number', 'group_id': group_id, 'likes_number': likes_number,
        }))
