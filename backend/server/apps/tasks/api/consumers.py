from channels.generic.websocket import AsyncWebsocketConsumer
import json

class TasksConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        # One group name for all clients: 'tasks'
        self.group_name = 'tasks'
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        pass

    async def task_update_message(self, event):
        # Send message to channel
        await self.send(json.dumps(event))
