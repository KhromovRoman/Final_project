
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.core.files.base import ContentFile
from io import BytesIO
from urllib.parse import unquote_plus
from .models import Message, Attachment

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        if data.get('type') == 'message':
            message_text = data.get('text')
            attachment = None
            
            if bytes_data is not None:
                filename = unquote_plus(data.get('filename'))
                content_file = ContentFile(bytes_data, name=filename)
                attachment = Attachment(file=content_file)
                attachment.save()
                
            message = Message.objects.create(
                sender=self.scope["user"],
                recipient=data.get('recipient_id'),
                text=message_text
            )
            
            if attachment:
                message.attachments.add(attachment)
        
            await self.send(json.dumps({'type': 'message', 'id': message.id}))