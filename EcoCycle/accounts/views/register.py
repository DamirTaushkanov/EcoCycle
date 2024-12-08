from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

from ..serializers.user_serializer import UserCreateSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    user = UserCreateSerializer(data=request.data)
    if user.is_valid():
        user.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)