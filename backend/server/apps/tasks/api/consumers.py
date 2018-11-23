from channels.generic.websocket import AsyncWebsocketConsumer
import json

class TasksConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        """
        Called when the websocket is handshaking as part of initial connection.
        """
        print(self.scope)
        if self.scope.get('user'):
            if self.scope.get('user').is_anonymous:
                print('Go away anonymous')
                self.group_name = None
                await self.close()
            else:
                print('I know you, my user', self.scope.get('user'))
                self.group_name = 'tasks'
                await self.channel_layer.group_add(self.group_name, self.channel_name)
                await self.accept()

    async def disconnect(self, close_code):
        if self.group_name:
            await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        pass

    async def task_update_message(self, event):
        # Send message to channel
        await self.send(json.dumps(event))
