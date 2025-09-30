from django.db import models
from appAuth.models import Employees

class Message(models.Model):
    sender = models.ForeignKey(Employees, on_delete=models.CASCADE,
    verbose_name='Отправитель', related_name='sent_messages')
    recipient = models.ForeignKey(Employees, on_delete=models.CASCADE, verbose_name='Получатель', related_name='resived_messages')
    text = models.TextField(verbose_name='Текст',blank=True)
    created_at = models.DateTimeField(verbose_name='Дата отправки', auto_now_add=True)
    
    class Meta:
        ordering = ['created_at']

class Attachment(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="files")
    file = models.FileField(verbose_name='Файл',upload_to='chat_attachments/')
    uploaded_at = models.DateTimeField(verbose_name='Загружено', auto_now_add=True)
