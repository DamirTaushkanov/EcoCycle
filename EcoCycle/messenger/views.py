from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Chat, Message
from django.contrib.auth.decorators import login_required

@login_required
def chat_list(request):
    chats = Chat.objects.filter(participants=request.user)
    return render(request, 'messenger/chat_list.html', {'chats': chats})

@login_required
def chat_detail(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id, participants=request.user)
    return render(request, 'chat/chat_detail.html', {'chat': chat})

@login_required
def send_message(request, chat_id):
    if request.method == 'POST':
        chat = get_object_or_404(Chat, id=chat_id, participants=request.user)
        content = request.POST.get('content')
        if content:
            message = Message.objects.create(chat=chat, sender=request.user, content=content)
            return JsonResponse({'status': 'success', 'message': message.content})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})
