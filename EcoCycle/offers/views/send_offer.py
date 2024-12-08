from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from chat.models import Message
from chat.serializers.create_message_serializer import MessageCreateSerializer


@api_view(["POST"])
def send_offer(request):
    message = MessageCreateSerializer(data=request.data, context={'request': request})
    if message.is_valid():
        message.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(message.errors, status=status.HTTP_400_BAD_REQUEST)