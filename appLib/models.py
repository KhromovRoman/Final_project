from django.db import models
from django import forms
from appAuth.models import Employees



class FileLibrary(models.Model):
    title = models.CharField('Название', max_length=255)
    description = models.TextField('Краткое описание', blank=True)
    file = models.FileField(upload_to='library_files/', null=True, blank=True, verbose_name='Файл')
    uploaded_by = models.ForeignKey(Employees, on_delete=models.SET_NULL, null=True, verbose_name='Дата публикации',)
    uploaded_at = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'файл'
        verbose_name_plural = 'Библиотека'

