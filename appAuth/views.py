
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
import appAuth


class StartPage(View):
    def get (self, request):
        return render (request, 'auth/index.html')
    
class ChangePasswordView(LoginRequiredMixin, FormView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('task/index.html')
    template_name = 'change_password.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        self.request.user.password_changed = True
        self.request.user.save()
        return super().form_valid(form)
