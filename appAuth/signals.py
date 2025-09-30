from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.shortcuts import redirect
import appAuth
import appAuth.models

@receiver(user_logged_in)
def check_password_change(sender, request, user, **kwargs):
    if not appAuth.models.Employees.password_changed:
        messages.error(request, 'Необходимо сменить пароль.')
        return redirect('auth/change_password.html')