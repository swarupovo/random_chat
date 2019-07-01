# chat/consumers.py
import pymongo as pymongo
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
import json
from datetime import datetime

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        ip = "127.0.0.1"
        port = "27017"
        database = "my_area_local"
        conn = pymongo.MongoClient('mongodb://{}:{}/{}'.format(ip, port, database))
        db = conn[database]
        rc = db['room_chat']
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name




        )
        if rc.find({"chat_room": self.room_group_name}):
            await self.accept()
        else:
            print("how are you")
            await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        ip = "127.0.0.1"
        port = "27017"
        database = "my_area_local"
        conn = pymongo.MongoClient('mongodb://{}:{}/{}'.format(ip, port, database))
        db = conn[database]
        rc = db['room_chat']
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        dicto = {}
        if message.split("=>")[1] != "":
            # dicto.update({"user": self.room_group_name, "message": message, "time": datetime.now()})
            # rc.insert_one(dicto)

            # Send message to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message
                }
            )


    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        ip = "127.0.0.1"
        port = "27017"
        database = "my_area_local"
        conn = pymongo.MongoClient('mongodb://{}:{}/{}'.format(ip, port, database))
        db = conn[database]
        rc = db['room_chat']
        dicto = {}
        dicto.update({"chat_room": self.room_group_name, "message": message,
                      "time": datetime.now()})
        rc.insert_one(dicto)

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
