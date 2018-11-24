import json
from channels.generic.websocket import AsyncWebsocketConsumer


class TasksConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """
        Called when the websocket is handshaking as part of initial connection.
        """
        self.group_name = None
        print(self.scope)
        user = self.scope.get("user")
        organization = self.scope.get("organization")
        #print(user, organization)
        if user is None or organization is None:
            await self.close()
        else:
            if user.is_anonymous or organization is None:
                print("Go away anonymous")
                await self.close()
            else:
                print(
                    "I know you, my user",
                    self.scope.get("user"),
                    "from",
                    organization.slug,
                )
                self.group_name = organization.slug
                await self.channel_layer.group_add(self.group_name, self.channel_name)
                await self.accept()

    async def disconnect(self, close_code):
        if self.group_name:
            await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        print("Tasks consumer receive", text_data)
        pass

    async def task_update_message(self, event):
        # Send message to channel
        await self.send(json.dumps(event))
