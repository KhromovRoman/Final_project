from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.StartPage.as_view(), name='urlStartPage'),
] 