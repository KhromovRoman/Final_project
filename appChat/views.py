from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Message, Attachment

@csrf_exempt
def upload_attachment(request):
    if request.method == 'POST':
        files = request.FILES.getlist('files[]')
        for f in files:
            att = Attachment(file=f)
            att.save()
        return JsonResponse({"result": "Выполнено"})
@login_required
def chat_view(request):
    return render(request, 'chat/index.html')

