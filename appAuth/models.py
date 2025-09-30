from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

class StatusChoices(models.TextChoices):

    MAKE_CHOICE = 'MAKE_CHOICE', _('Выберите департамент')
    DEPARTMENT_1 = 'DEPARTMENT_1', _('1-й Департамент')
    DEPARTMENT_2 = 'DEPARTMENT_2', _('2-й Департамент')
    DEPARTMENT_3 = 'DEPARTMENT_3', _('3-й Департамент')
    DEPARTMENT_4 = 'DEPARTMENT_4', _('4-й Департамент')
    DEPARTMENT_5 = 'DEPARTMENT_5', _('5-й Департамент')
    DEPARTMENT_6 = 'DEPARTMENT_6', _('6-й Департамент')
    

class Employees(models.Model):

    title = models.CharField(
        verbose_name='Наименование отдела',
        choices=StatusChoices.choices,
        default=StatusChoices.MAKE_CHOICE 
    )
    second_name=models.CharField(
        verbose_name='Фамилия',
        help_text="Например: Иванов"
    )
    first_name=models.CharField(
        verbose_name='Имя',
        help_text="Например: Иван"
    )
    third_name=models.CharField(
        verbose_name='Отчество',
        help_text="Например: Иванович"
    )
    position=models.TextField(
        verbose_name='Должность'
    )
    phone_number=models.CharField(
        max_length=15,
        verbose_name='Номер телефона',
        help_text="8(903)557-55-44"
        )
    photo=models.ImageField(
        verbose_name='Фото',
        upload_to='photo/',
        null=True,
        blank=True, 
    )
    e_mail=models.EmailField(
        unique=True, 
        help_text="Адрес электронной почты"
    )
    hashed_password = models.CharField(max_length=128, verbose_name='Пароль', default=123456)
   
    password_changed = models.BooleanField(verbose_name='Новый пароль',default=False)
    
    
    status=models.BooleanField(
        verbose_name='Статус',
        default=True
    )
    date_created = models.DateField(
        verbose_name='Дата создания аккаунта',
        auto_now_add=True
    )
    date_updated=models.DateField (
        verbose_name='Дата последнего изменения аккаунта',
        auto_now=True
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


